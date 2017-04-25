# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 17:24
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_remove_siteuser_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]