# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0007_auto_20161106_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=2),
            preserve_default=False,
        ),
    ]
