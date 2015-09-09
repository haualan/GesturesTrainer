# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0019_auto_20150819_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='phasesection',
            name='days_apart',
            field=models.IntegerField(default=7),
        ),
    ]
