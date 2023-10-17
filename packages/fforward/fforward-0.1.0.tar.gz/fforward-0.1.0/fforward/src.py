import re
import inspect
from typing import Any, Type, TypeVar, TypeAlias, Generic
from typing import Callable
from uuid import UUID, uuid4
from collections import defaultdict

from pydantic import BaseModel
from fastapi import status, HTTPException, APIRouter
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    mapped_column,
    Session,
)
from sqlalchemy import (
    String,
    UUID as SQL_UUID,
    TypeDecorator,
)
from sqlalchemy.engine.interfaces import Dialect
from functools import wraps


RT = TypeVar("RT")


def snakecasify(pascal_str: str = ""):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", pascal_str).lower()


class StrUUID(TypeDecorator):
    impl = String
    cache_ok = True

    def process_bind_param(self, value: Any | None, dialect: Dialect) -> str | None:
        if value is not None:
            return str(value)
        return None

    def process_result_value(self, value: Any | None, dialect: Dialect) -> UUID | None:
        if value is not None:
            return UUID(value)
        return None

    def copy(self, **kw):
        return StrUUID(self.impl.length)


class Message(BaseModel):
    pass


class Event(Message):
    pass


class Command(Message):
    pass


HT = dict[Type[Command], Callable[..., None]]
ST = dict[Type[Event], list[Callable[..., None]]]


class Entity(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(
        SQL_UUID().with_variant(StrUUID(), "sqlite"), primary_key=True, default=uuid4
    )
    events: list[Event] = []

    def fire_event(self, event) -> None:
        self.events.append(event)

    def dump(self):
        dct = self.__dict__.copy()
        dct.pop("_sa_instance_state", None)
        return dct


EntityType = TypeVar("EntityType", bound=Entity)


class EntityCreated(Event, Generic[EntityType]):
    type: Type[EntityType]
    id: UUID


class EntityUpdated(Event, Generic[EntityType]):
    type: Type[EntityType]
    id: UUID


class EntityDeleted(Event, Generic[EntityType]):
    type: Type[EntityType]
    id: UUID


class TransactionFailed(Exception):
    pass


SessionMaker = Callable[[], Session]


class Transaction:
    __seen: set[Entity] = set()

    def __init__(self, session_maker: SessionMaker) -> None:
        self._session: Session = session_maker()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self._session.rollback()
        self._session.close()

    def __del__(self):
        self._session.rollback()
        self._session.close()

    def get(self, entity_type: Type[EntityType], id: UUID) -> EntityType | None:
        entity = self._session.get(entity_type, id)
        if entity:
            self.__seen.add(entity)
        return entity

    def persist(self, entity: EntityType) -> None:
        if entity.id:
            self.get(type(entity), entity.id)
            self._session.merge(entity)
            entity.fire_event(EntityUpdated(type=type(entity), id=entity.id))
        else:
            self._session.add(entity)
            self._session.flush()
            entity.fire_event(EntityCreated(type=type(entity), id=entity.id))
        self.__seen.add(entity)

    def delete(self, entity: EntityType) -> None:
        self._session.delete(entity)
        entity.fire_event(EntityDeleted(type=type(entity), id=entity.id))

    def commit(self):
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise TransactionFailed

    def stream_events(self):
        while self.__seen:
            entity = self.__seen.pop()
            while entity.events:
                event = entity.events.pop(0)
                yield event

    @property
    def history(self):
        return list(self.__seen)


class MessageBus:
    def __init__(self, tx: Transaction, subscribers: ST, handlers: HT):
        self.tx = tx
        self._subscribers: ST = subscribers
        self._handlers = handlers
        self._queue: list[Message] = []

    def process(self, message: Message):
        self._queue = [message]
        while self._queue:
            msg = self._queue.pop(0)
            print(f"process message {msg.__class__.__name__} {msg}")
            if isinstance(msg, Event):
                self.process_event(msg)
            elif isinstance(msg, Command):
                self.process_command(msg)
            else:
                raise ValueError("invalid bus message")

    def process_event(self, event: Event):
        for subscriber in self._subscribers.get(type(event), []):
            try:
                subscriber(event)
                self._queue.extend(self.tx.stream_events())
            except Exception:
                continue

    def process_command(self, cmd: Command):
        handler = self._handlers.get(type(cmd), None)
        if handler:
            handler(cmd)
            self._queue.extend(self.tx.stream_events())


class _Dependency:
    __registry: dict[str, Any] = {}
    __cache: dict[str, Any] = {}

    @classmethod
    def register(cls, fn: Callable[..., RT]):
        cls.__registry[str(fn.__name__).lower()] = fn
        return fn

    def build(self):
        for name, builder in self.__registry.items():
            if inspect.isclass(builder):
                self.__cache[name] = builder()

    @classmethod
    def inject(cls, fn: Callable[..., RT]):
        params = inspect.signature(fn).parameters
        deps = {}
        for name, builder in cls.__registry.items():
            if name in params:
                if inspect.isfunction(builder):
                    deps[name] = builder()
                elif inspect.isclass(builder):
                    if name not in cls.__cache:
                        cls.__cache[name] = builder()
                    deps[name] = cls.__cache[name]

        def injected(*args, **kwargs) -> RT:
            return fn(*args, **{**deps, **kwargs})

        return injected

    @property
    def dependencies(self):
        return {
            **self.__registry,
            **self.__cache,
        }

    def __getitem__(self, key):
        if key in self.__cache:
            return self.__cache[key]
        if key in self.__registry:
            return self.__registry[key]
        raise KeyError

    def __setitem__(self, key, value):
        self.__cache.pop(key, None)
        self.__registry[key] = value


Dependency = _Dependency()

DT = Callable[..., RT]


def dependency(fn: DT) -> DT:
    return Dependency.register(fn)


class Request(BaseModel):
    pass


class View(BaseModel):
    pass


class CreateEntity(Command):
    type: Type[Entity]
    data: dict[str, Any]


def create(cmd: CreateEntity, tx: Transaction):
    entity = cmd.type(**cmd.data)
    tx.persist(entity)
    tx.commit()


class UpdateEntity(Command):
    entity_id: UUID
    type: Type[Entity]
    data: dict[str, Any]


def update(cmd: UpdateEntity, tx: Transaction):
    entity = tx.get(cmd.type, cmd.entity_id)
    if entity:
        for name, value in cmd.data.items():
            if hasattr(entity, name):
                setattr(entity, name, value)

        tx.persist(entity)
        tx.commit()


class DeleteEntity(Command):
    entity_id: UUID
    type: Type[Entity]


def delete(cmd: DeleteEntity, tx: Transaction):
    entity = tx.get(cmd.type, cmd.entity_id)
    if entity:
        tx.delete(entity)
        tx.commit()


class GetEntity(Request):
    type: Type[Entity]
    id: UUID


class GetEntities(Command):
    type: Type[Entity]
    filters: dict[str, Any]


class App:
    __handlers: HT = {}
    __subscribers: ST = defaultdict(list)
    __queries: dict[Type[Request], Callable[..., RT]] = {}

    def __init__(self, session_maker: SessionMaker) -> None:
        class TxFactory:
            def __new__(cls):
                return Transaction(session_maker)

        Dependency["tx"] = TxFactory
        Dependency["session"] = session_maker
        Dependency.build()

        self.tx: Transaction = Dependency["tx"]
        self.command_handler(CreateEntity)(create)
        self.command_handler(UpdateEntity)(update)
        self.command_handler(DeleteEntity)(delete)

    def process_message(self, msg: Message):
        bus = MessageBus(self.tx, self.__subscribers, self.__handlers)
        bus.process(msg)

    def process_query(self, request: Request):
        view = self.__queries[type(request)]
        return view(request)

    def command_handler(self, cmd: Type[Command]):
        def decorator(fn):
            self.__handlers[cmd] = Dependency.inject(fn)
            return fn

        return decorator

    def event_subscriber(self, event: Type[Event]):
        def decorator(fn):
            self.__subscribers[event].append(Dependency.inject(fn))
            return fn

        return decorator

    def view_handler(self, request: type[Request]):
        def decorator(fn: Callable[..., RT]):
            self.__queries[request] = Dependency.inject(fn)
            return fn

        return decorator


class APIResponse(BaseModel):
    pass


class APIRequest(BaseModel):
    pass


RequestType = TypeVar("RequestType", bound=APIRequest)


class EntityCreatedResponse(APIResponse):
    status: str = "CREATED"


class EntityUpdatedResponse(APIResponse):
    status: str = "UPDATED"


class EntityDeletedResponse(APIResponse):
    status: str = "DELETED"


CREATED = EntityCreatedResponse()
UPDATED = EntityUpdatedResponse()
DELETED = EntityDeletedResponse()


class CreateEntityRequest(APIRequest):
    data: dict[str, Any]


class UpdateEntityRequest(APIRequest):
    id: UUID
    data: dict[str, Any]


class DeleteEntityRequest(APIRequest):
    id: UUID


class IdPayload(APIRequest):
    id: UUID


class EntityApi:
    def __init__(
        self,
        app: App,
        entity: Type[EntityType],
        payload_cls: Type[RequestType],
        view: View | None = None,
        **kwargs,
    ):
        self.app = app
        self.entity = entity
        self.router = APIRouter(tags=[f"{entity.__name__}"], **kwargs)
        self.payload_cls = payload_cls

        self.build_controllers(entity)

    def _build_create_controller(
        self,
        entity_cls: Type[Entity],
    ) -> tuple[Callable[..., EntityCreatedResponse], int, str, str]:
        summary = f"Create {entity_cls.__name__}"

        CreatePayload: Type[APIRequest] = type(
            f"Create{entity_cls.__name__}Payload", (self.payload_cls,), {}
        )

        def controller(payload: CreatePayload):  # type: ignore
            try:
                self.app.process_message(
                    CreateEntity(type=entity_cls, data=payload.model_dump())  # type: ignore
                )
            except Exception as e:
                raise HTTPException(400)
            return CREATED

        return controller, status.HTTP_201_CREATED, "POST", summary

    def _build_update_controller(
        self,
        entity_cls: Type[Entity],
    ) -> tuple[Callable[..., EntityUpdatedResponse], int, str, str]:
        summary = f"Update {entity_cls.__name__} by id"

        UpdatePayload = type(
            f"Update{entity_cls.__name__}Payload", (IdPayload, self.payload_cls), {}
        )

        def controller(payload: UpdatePayload):  # type: ignore
            try:
                self.app.process_message(
                    UpdateEntity(
                        type=entity_cls, entity_id=payload.id, data=payload.model_dump()  # type: ignore
                    )
                )
            except TransactionFailed as e:
                print(str(e))
                raise HTTPException(400)
            return UPDATED

        return controller, status.HTTP_200_OK, "PATCH", summary

    def _build_delete_controller(
        self,
        entity_cls: Type[Entity],
    ):
        summary = f"Delete {entity_cls.__name__} by id"

        def controller(payload: DeleteEntityRequest):
            try:
                self.app.process_message(
                    DeleteEntity(type=entity_cls, entity_id=payload.id)
                )
            except TransactionFailed as e:
                print(str(e))
                raise HTTPException(400)
            return DELETED

        return controller, status.HTTP_200_OK, "DELETE", summary

    def entity_controller_builders(self):
        return [
            self._build_create_controller,
            self._build_update_controller,
            self._build_delete_controller,
        ]

    def build_controllers(self, entity: Type[Entity]):
        endpoint = f"/{snakecasify(entity.__name__)}"
        for build_entity_controller in self.entity_controller_builders():
            controller, status_code, method, summary = build_entity_controller(entity)
            self.router.api_route(
                endpoint,
                status_code=status_code,
                methods=[method],
                summary=summary,
            )(controller)
