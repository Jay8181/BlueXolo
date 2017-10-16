# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('requirement', models.BooleanField(default=False)),
                ('needs_value', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'argument',
                'verbose_name_plural': 'arguments',
                'db_table': 'arguments',
            },
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='command')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('arguments', models.ManyToManyField(blank=True, to='Products.Argument')),
            ],
            options={
                'verbose_name': 'command',
                'verbose_name_plural': 'commands',
                'db_table': 'commands',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='source name')),
                ('version', models.CharField(max_length=30, verbose_name='version')),
                ('category', models.IntegerField(choices=[(1, 'Flow Sentences'), (2, 'OS'), (3, 'Product'), (4, 'Robot Framework'), (5, 'External Libraries')], verbose_name='category')),
                ('depends', models.ManyToManyField(blank=True, to='Products.Source')),
            ],
            options={
                'verbose_name': 'source',
                'verbose_name_plural': 'sources',
                'db_table': 'sources',
            },
        ),
        migrations.AddField(
            model_name='command',
            name='source',
            field=models.ManyToManyField(blank=True, to='Products.Source'),
        ),
    ]
