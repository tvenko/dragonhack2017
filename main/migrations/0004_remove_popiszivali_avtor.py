# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170521_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popiszivali',
            name='avtor',
        ),
    ]
