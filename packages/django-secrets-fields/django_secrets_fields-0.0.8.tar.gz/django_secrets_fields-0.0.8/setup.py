# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['secrets_fields',
 'secrets_fields.backends',
 'secrets_fields.management',
 'secrets_fields.management.commands']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.28.63,<2.0.0', 'django>3']

setup_kwargs = {
    'name': 'django-secrets-fields',
    'version': '0.0.8',
    'description': 'Django encrypted model field that fetches the value from multiple sources',
    'long_description': '# Django secrets fields\n\n## Supported backends\n- AWS Secrets Manager\n\n## Installation\n```bash\npip install django-secrets-fields\n```\n',
    'author': 'Ryan shaw',
    'author_email': 'ryan.shaw@min.vc',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
