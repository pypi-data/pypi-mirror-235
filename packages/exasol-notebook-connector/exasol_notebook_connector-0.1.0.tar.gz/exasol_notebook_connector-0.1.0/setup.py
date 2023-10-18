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
    'name': 'exasol-notebook-connector',
    'version': '0.1.0',
    'description': 'Components, tools, APIs, and configurations in order to connect Jupyter notebooks to Exasol and various other systems.',
    'long_description': '# notebook-connector\nConnection configuration management and additional tools for Jupyter notebooks.\n',
    'author': 'Christoph Kuhnke',
    'author_email': 'christoph.kuhnke@exasol.com',
    'maintainer': 'Christoph Kuhnke',
    'maintainer_email': 'christoph.kuhnke@exasol.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0',
}


setup(**setup_kwargs)
