# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_remove_siteuser_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='activate1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='activate2',
            field=models.BooleanField(default=False),
        ),
    ]
