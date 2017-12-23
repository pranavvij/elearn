from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.contrib.postgres.fields.jsonb import JSONField as JSF

from deadline.models import College 


class Transcript(models.Model):
    refid = models.CharField(max_length = 128)
    url = models.TextField(blank=True,null=True)
    college = models.ForeignKey(College)
    type = models.CharField(max_length = 128,default = 'SOP')

