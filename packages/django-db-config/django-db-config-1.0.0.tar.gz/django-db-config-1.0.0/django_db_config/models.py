__all__ = [
    "Config",
]

from django.db import models


class Config(models.Model):
    key = models.CharField(unique=True, max_length=255)
    value = models.TextField(null=True)

    class Meta:
        db_table = "config"
