# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-16 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ip_range',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('start_ip_address', models.GenericIPAddressField()),
                ('end_ip_address', models.GenericIPAddressField()),
            ],
        ),
    ]
