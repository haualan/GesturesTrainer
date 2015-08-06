# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_phasesection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phasesection',
            name='order',
        ),
        migrations.AlterField(
            model_name='phasesection',
            name='start_date',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]
