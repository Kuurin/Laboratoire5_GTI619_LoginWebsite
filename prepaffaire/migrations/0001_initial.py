# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prepaffaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.TextField(db_column='Prenom')),
                ('nom', models.TextField(db_column='Nom')),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
                ('phone', models.TextField(blank=True, db_column='Phone', null=True)),
            ],
        ),
    ]
