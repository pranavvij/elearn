# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-28 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20171128_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocab',
            name='word',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
