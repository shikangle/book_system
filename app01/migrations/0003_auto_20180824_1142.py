# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-24 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180824_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]