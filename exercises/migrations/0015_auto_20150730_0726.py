# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0014_auto_20150730_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
    ]
