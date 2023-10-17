# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fforward']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.103.2,<0.104.0', 'sqlalchemy>=2.0.22,<3.0.0']

setup_kwargs = {
    'name': 'fforward',
    'version': '0.1.2',
    'description': '',
    'long_description': '# forward\nForward\n',
    'author': 'TheGreen',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
