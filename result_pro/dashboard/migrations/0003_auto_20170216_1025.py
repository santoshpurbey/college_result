# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-16 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170216_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managestudent',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Program'),
        ),
    ]