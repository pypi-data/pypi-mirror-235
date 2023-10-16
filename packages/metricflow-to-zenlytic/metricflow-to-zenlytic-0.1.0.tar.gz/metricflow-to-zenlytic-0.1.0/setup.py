# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metricflow_to_zenlytic']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'click>=8.0,<9.0']

entry_points = \
{'console_scripts': ['metricflow_to_zenlytic = '
                     'metricflow_to_zenlytic:cli_group']}

setup_kwargs = {
    'name': 'metricflow-to-zenlytic',
    'version': '0.1.0',
    'description': 'Adapters for Zenyltic',
    'long_description': "# Zenlytic Adapters\n\nUtilities for converting semantic layer YAML files to Zenlytic's format.\n\n## Steps for usage:\n1. Clone this repo in a valid dbt project\n1. Run `dbt parse` to generate model yaml files in Metricflow format, if you haven't already. They should live in your dbt project's `models` directory.\n1. `cd` into the newly cloned repo\n1. Run `python3 -m pip install .`\n1. `cd` back into the dbt project\n1. Run `mf_to_zen --project_name .`\n1. You should now see a `views` directory in your dbt project containing your Metricflow semantic models represented as Zenlytic views.\n\n## To test\n`pytest`",
    'author': 'Paul Blankley',
    'author_email': 'paul@zenlytic.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Zenlytic/zenlytic-adapters',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<3.12',
}


setup(**setup_kwargs)
