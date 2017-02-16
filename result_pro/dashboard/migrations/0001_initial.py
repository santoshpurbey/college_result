# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-16 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManageStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('year', models.CharField(choices=[('17', '2017'), ('18', '2018'), ('19', '2019'), ('20', '2020'), ('21', '2021'), ('22', '2022')], max_length=10)),
                ('program', models.CharField(max_length=20)),
            ],
        ),
    ]