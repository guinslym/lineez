# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('title', models.CharField(verbose_name='title', max_length=60)),
                ('decription', models.TextField(verbose_name='description')),
                ('photo', models.ImageField(upload_to='delivrem/%Y/%m/%d', help_text='Show us wadiyabi', verbose_name='pics')),
                ('slug', models.CharField(blank=True, null=True, max_length=220)),
                ('price', models.DecimalField(default=0, blank=True, null=True, decimal_places=2, max_digits=16)),
                ('activated', models.BooleanField(default=False)),
                ('sale', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
