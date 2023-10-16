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
    'version': '0.1.2',
    'description': 'Adapter for Metricflow to Zenlytic',
    'long_description': '# Zenlytic Adapters\n\nUtilities for converting semantic layer YAML files to Zenlytic\'s format.\n\n## Steps for usage:\n1. Run `pip install metricflow-to-zenlytic`\n2. `$ metricflow_to_zenlytic [DIRECTORY]` from the command line, where `[DIRECTORY]` is the directory your `dbt_project.yml` file is in.\n\n## Usage in Python\n\nTo run the function in python you can do so like this:\n\n```\nfrom metricflow_to_zenlytic.metricflow_to_zenlytic import (\n    load_mf_project,\n    convert_mf_project_to_zenlytic_project,\n)\n\n# Load the metricflow project\nmetricflow_project = load_mf_project(metricflow_folder)\n\n# Convert to Zenyltic models and views\nmodels, views = convert_mf_project_to_zenlytic_project(metricflow_project, "my_model", "my_company")\n\n# Save as yaml files\nout_directory = \'/save/to/here/\'\nzenlytic_views_to_yaml(models, views, out_directory)\n\n```\n\n## Testing\n\n`$ pytest`\n',
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
