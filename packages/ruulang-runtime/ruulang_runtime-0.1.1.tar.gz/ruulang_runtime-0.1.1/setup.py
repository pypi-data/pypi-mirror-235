# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ruulang_runtime']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=2.4.2,<3.0.0']

setup_kwargs = {
    'name': 'ruulang-runtime',
    'version': '0.1.1',
    'description': 'The python runtime library for the RuuLang project',
    'long_description': None,
    'author': 'Zach',
    'author_email': 'zach@dttw.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
