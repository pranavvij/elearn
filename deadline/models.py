from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.postgres.fields.jsonb import JSONField as JSF


class College(models.Model):
    refid = models.CharField(max_length=128,default = '')
    college_name = models.TextField(blank = True)
    description = models.TextField(blank = True)
    deadline = models.CharField(max_length=128,default = '')
    created = models.CharField(max_length=128,default = '')
    updated = models.CharField(max_length=128,default = '')
    

class Subjects(models.Model):
    refid = models.CharField(max_length=128,default = '')
    college = models.ForeignKey(College)
    subject_name = models.CharField(max_length = 128,default='')
    subject_description = models.TextField(blank=True)
    subject_deadline = models.CharField(max_length=128,default = '')
    deadline_type = models.CharField(max_length = 128)
    gre_cut_off_verbal = models.CharField(max_length=24,default = '130')
    gre_cut_off_quant = models.CharField(max_length=24,default = '130')
    ug_gpa = models.CharField(max_length=24,default = '3')
    work_exp = models.CharField(max_length=24,default = '1')
    created = models.CharField(max_length=128,default = '')
    updated = models.CharField(max_length=128,default = '')