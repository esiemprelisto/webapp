# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0048_auto_20180628_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='tipoDirigente',
            new_name='tipoJefe',
        ),
    ]
