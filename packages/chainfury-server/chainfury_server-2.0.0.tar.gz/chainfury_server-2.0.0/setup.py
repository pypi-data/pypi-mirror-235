# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chainfury_server', 'chainfury_server.api', 'chainfury_server.engines']

package_data = \
{'': ['*'],
 'chainfury_server': ['examples/*',
                      'static/*',
                      'static/assets/*',
                      'static/script/*']}

install_requires = \
['PyJWT[crypto]==2.6.0',
 'PyMySQL==1.0.3',
 'SQLAlchemy==1.4.47',
 'black==23.3.0',
 'chainfury',
 'fastapi==0.95.2',
 'fire==0.5.0',
 'passlib==1.7.4',
 'requests>=2.31.0,<3.0.0',
 'uvicorn==0.20.0']

entry_points = \
{'console_scripts': ['cf_server = chainfury_server.server:main',
                     'chainfury_server = chainfury_server.server:main']}

setup_kwargs = {
    'name': 'chainfury-server',
    'version': '2.0.0',
    'description': 'ChainFury Server is the open source server for running ChainFury Engine!',
    'long_description': '# ChainFury Server\n\nThis is a package separate from `chainfury` which provides the python execution engine.\n',
    'author': 'NimbleBox Engineering',
    'author_email': 'engineering@nimblebox.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NimbleBoxAI/ChainFury',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
