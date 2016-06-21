# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.AlterField(
            model_name='consumer',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]