# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-05 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_sales', '0008_merge_20180509_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleshistory',
            name='paid_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True),
        ),
    ]
