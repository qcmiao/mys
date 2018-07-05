# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-03 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=64)),
            ],
        ),
    ]
