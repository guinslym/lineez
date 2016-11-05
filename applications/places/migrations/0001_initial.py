# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('location', models.CharField(max_length=100, blank=True, null=True, verbose_name='address')),
                ('start_date', models.DateTimeField(null=True, auto_now=True)),
                ('before_start', models.CharField(max_length=10, choices=[('1', '1'), ('2', '2')], default='Time in day')),
                ('price', models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=16, default=0)),
                ('activated', models.BooleanField(default=False)),
                ('sale', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
