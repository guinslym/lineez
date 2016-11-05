# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(max_length=100, null=True, blank=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='post',
            name='decription',
            field=models.TextField(null=True, blank=True, verbose_name='description'),
        ),
    ]
