# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-27 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app01', '0015_auto_20180827_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicsher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]
