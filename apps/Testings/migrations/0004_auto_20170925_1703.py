# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Testings', '0003_collection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='products',
            new_name='product',
        ),
    ]
