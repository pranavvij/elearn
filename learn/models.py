
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.contrib.postgres.fields.jsonb import JSONField as JSF

class Vocab(models.Model):
    refid = models.CharField(max_length = 128)
    word = models.CharField(max_length = 200)
    definition = models.TextField(default = "")
    synonyms = JSONField(default = {})
    examples = JSONField(default = {})
    frequency = models.FloatField(default = 0.0)
    