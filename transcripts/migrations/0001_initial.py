# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-22 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deadline', '0002_subjects_deadline_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refid', models.CharField(max_length=128)),
                ('url', models.TextField(blank=True, null=True)),
                ('type', models.CharField(default='SOP', max_length=128)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deadline.College')),
            ],
        ),
    ]
