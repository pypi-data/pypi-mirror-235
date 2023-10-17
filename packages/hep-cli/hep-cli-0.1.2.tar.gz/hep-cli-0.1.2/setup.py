# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hep_cli']

package_data = \
{'': ['*']}

install_requires = \
['rich>=13.6.0,<14.0.0']

entry_points = \
{'console_scripts': ['hep-cli = hep_cli.cli:run_app']}

setup_kwargs = {
    'name': 'hep-cli',
    'version': '0.1.2',
    'description': 'A basic CLI app',
    'long_description': '# python-cli-template\nA template repository for creating CLI apps \n\n\n## Dependencies\n\n- poetry https://python-poetry.org/\n- typer https://typer.tiangolo.com/\n\n\n## Commands\n\n```bash\npoetry new <package-name>\n\npoetry add <dep-package-name>\n```',
    'author': 'Oguzhan Yilmaz',
    'author_email': 'oguzhan@hepapi.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.13',
}


setup(**setup_kwargs)
