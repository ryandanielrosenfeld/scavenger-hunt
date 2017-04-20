# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20170411_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='activate',
        ),
    ]
