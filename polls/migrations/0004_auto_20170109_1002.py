# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-09 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170106_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoolStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='poll',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]