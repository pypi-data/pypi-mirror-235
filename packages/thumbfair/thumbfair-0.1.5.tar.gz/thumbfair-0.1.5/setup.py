# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thumbfair']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'thumbfair',
    'version': '0.1.5',
    'description': '',
    'long_description': '# Thumbfair\nCollection of scripts to quickly generate thumbnails for SSBU tournaments.',
    'author': 'Impasse52',
    'author_email': 'giuseppe.termerissa@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
