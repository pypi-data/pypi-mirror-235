# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hotfuzz_control_panel']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0', 'hotfuzz>=0.2.0,<0.3.0']

setup_kwargs = {
    'name': 'hotfuzz-control-panel',
    'version': '0.4.0',
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
