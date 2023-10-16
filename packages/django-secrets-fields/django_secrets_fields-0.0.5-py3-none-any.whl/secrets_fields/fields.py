"""
Django encrypted model field that fetches the value from AWS Secrets Manager
"""

import django.db.models
from django.conf import settings
from .util import get_client


class SecretsManagerMixin(object):
    def to_python(self, value: str):
        if value is None:
            return value

        # fetch from secrets manager
        role_arn = getattr(settings, "DJANGO_SECRET_FIELDS_AWS_ROLE_ARN_RO", None)
        client = get_client(role_arn=role_arn)
        secret = client.get_secret_value(SecretId=value)

        return super(SecretsManagerMixin, self).to_python(secret["SecretString"])

    def from_db_value(self, value, *args, **kwargs):
        return self.to_python(value)

    def get_db_prep_save(self, value, connection):
        # saving only updates the path to the secret in secrets manager
        value = super(SecretsManagerMixin, self).get_db_prep_save(value, connection)

        return value

    def get_internal_type(self):
        return "TextField"


class SecretTextField(SecretsManagerMixin, django.db.models.TextField):
    pass
