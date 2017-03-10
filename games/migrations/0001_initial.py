# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import games.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=games.models.image_game_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.IntegerField(default=0)),
                ('website', models.URLField()),
                ('release_date', models.DateField()),
                ('engine', models.CharField(max_length=40)),
                ('type_game', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=games.models.image_platform_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]