# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linky', '0003_themanwholaugh_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMWL_english',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=50, null=True)),
                ('song', models.CharField(max_length=400, null=True)),
                ('music', models.CharField(max_length=200, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TMWL_japanese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=50, null=True)),
                ('song', models.CharField(max_length=400, null=True)),
                ('music', models.CharField(max_length=200, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TMWL_korean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=50, null=True)),
                ('song', models.CharField(max_length=400, null=True)),
                ('music', models.CharField(max_length=200, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='TheManWhoLaugh',
            new_name='TMWL_chinese',
        ),
    ]
