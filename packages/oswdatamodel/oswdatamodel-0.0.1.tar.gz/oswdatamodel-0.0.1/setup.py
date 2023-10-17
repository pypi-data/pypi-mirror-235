# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oswdatamodel',
 'oswdatamodel.fea',
 'oswdatamodel.geometry',
 'oswdatamodel.results']

package_data = \
{'': ['*']}

install_requires = \
['black>=23.9.1,<24.0.0', 'pydantic>=2.4.2,<3.0.0', 'pytest>=7.4.2,<8.0.0']

setup_kwargs = {
    'name': 'oswdatamodel',
    'version': '0.0.1',
    'description': 'Offshore wind turbine structure datamodel written in pydantic.',
    'long_description': '![Test status](https://github.com/beancandesign/oswdatamodel/actions/workflows/test.yml/badge.svg?event=push)\n\n# oswdatamodel\nOffshore wind turbine structure datamodel written in pydantic.',
    'author': 'Ben Cannell',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
