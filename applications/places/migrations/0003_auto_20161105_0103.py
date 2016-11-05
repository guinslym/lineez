# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20161105_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='address',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
