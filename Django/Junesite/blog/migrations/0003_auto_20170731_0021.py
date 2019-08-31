# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170730_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Draft', '미완성'), ('Published', '공개'), ('Withdraw', '폐지 예정')], max_length=10),
        ),
    ]