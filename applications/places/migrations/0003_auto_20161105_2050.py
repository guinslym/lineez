# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_remove_post_activated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='decription',
            field=models.TextField(null=True, blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True, verbose_name='location'),
        ),
    ]
