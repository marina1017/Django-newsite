# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-30 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180430_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message_bord',
            name='created_at',
        ),
    ]