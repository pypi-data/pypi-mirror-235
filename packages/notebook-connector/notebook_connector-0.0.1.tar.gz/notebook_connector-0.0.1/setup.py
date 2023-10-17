# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exasol']

package_data = \
{'': ['*']}

install_requires = \
['exasol-toolbox>=0.5.0,<0.6.0', 'sqlcipher3-binary>=0.5.0']

entry_points = \
{'console_scripts': ['tbx = exasol.toolbox.tools.tbx:CLI']}

setup_kwargs = {
    'name': 'notebook-connector',
    'version': '0.0.1',
    'description': 'Components, tools, APIs, and configurations in order to connect Jupyter notebooks to various other systems.',
    'long_description': 'None',
    'author': 'Christoph Kuhnke',
    'author_email': 'christoph.kuhnke@exasol.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0',
}


setup(**setup_kwargs)
