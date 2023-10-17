# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['forta', 'forta.auth', 'forta.lk', 'forta.odata', 'forta.payout']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.103.2,<0.104.0',
 'nicegui[netifaces]>=1.3.17,<2.0.0',
 'pybrom>=1.1.6',
 'pydantic-settings>=2.0.3',
 'pytest>=7.4.2,<8.0.0',
 'trio>=0.22.2,<0.23.0',
 'typer-config[all]>=1.2.1',
 'typer[all]>=0.9.0']

entry_points = \
{'console_scripts': ['forta = forta.__main__:__main__']}

setup_kwargs = {
    'name': 'forta-gate',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Anton Rastyazhenko',
    'author_email': 'rastyazhenko.anton@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
