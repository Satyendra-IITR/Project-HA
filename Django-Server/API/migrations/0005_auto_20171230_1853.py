# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-30 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_usermodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date published'),
        ),
    ]
