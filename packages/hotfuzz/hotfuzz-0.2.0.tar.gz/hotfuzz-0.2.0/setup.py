# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hotfuzz']

package_data = \
{'': ['*']}

install_requires = \
['PyQt6>=6.5.2,<7.0.0', 'fuzzyfinder>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'hotfuzz',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'megahomyak',
    'author_email': 'g.megahomyak@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
