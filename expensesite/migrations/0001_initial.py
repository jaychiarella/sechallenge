# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=150)),
                ('employee_name', models.CharField(default='', max_length=50)),
                ('employee_address', models.CharField(default='', max_length=200)),
                ('expense_description', models.CharField(default='', max_length=200)),
                ('pre_tax_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('tax_name', models.CharField(default='', max_length=30)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
