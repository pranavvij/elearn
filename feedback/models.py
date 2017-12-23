# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class FeedBack(models.Model):
    refid = models.CharField(content_length = 128,default = '')
    
