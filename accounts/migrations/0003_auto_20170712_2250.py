# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='media/avatars/'),
        ),
    ]
