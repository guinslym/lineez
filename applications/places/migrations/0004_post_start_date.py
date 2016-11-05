# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20161105_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
