# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-24 04:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boletin', '0014_programa_seccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
