# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170106_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='multiple_answers',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.Poll'),
        ),
    ]
