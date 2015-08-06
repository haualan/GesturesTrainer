# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_phase_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
