# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-07 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20161106_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='decription',
            new_name='description',
        ),
    ]
