from django.db import models

class Client(models.Model):
    refid = models.CharField(max_length=128,default='')
    updated = models.CharField(max_length=128,default='')
    created = models.CharField(max_length=128,default='' )
    access_token = models.CharField(max_length=128,default='')
    imei_number = models.CharField(max_length=128, default='')