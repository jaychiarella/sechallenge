# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensesite', '0003_auto_20170126_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='pre_tax_amount',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='name',
            name='tax_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
