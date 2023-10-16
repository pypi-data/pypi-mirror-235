# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dalle3']

package_data = \
{'': ['*']}

install_requires = \
['requests', 'selenium', 'undetected-chromedriver']

setup_kwargs = {
    'name': 'dalle3',
    'version': '0.0.1',
    'description': 'dalle3 - Pytorch',
    'long_description': "[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Python Package Template\nA easy, reliable, fluid template for python packages complete with docs, testing suites, readme's, github workflows, linting and much much more\n\n\n## DALLE-3 API\n`pip install dalle3`\n\n\n\n# License\nMIT\n\n\n\n",
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/paper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
