# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='activate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='task_num',
            field=models.IntegerField(default=0),
        ),
    ]
