# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-02-06 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pis_com', '0010_auto_20190202_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
