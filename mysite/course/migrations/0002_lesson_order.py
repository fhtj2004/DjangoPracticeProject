# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-04 10:03
from __future__ import unicode_literals

import course.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='order',
            field=course.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
