# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-30 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message_bord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_message', models.TextField(null=True)),
            ],
        ),
    ]
