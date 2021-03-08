# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 06:17
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150716_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
