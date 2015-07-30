# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0013_auto_20150730_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseresult',
            name='cycle',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='exerciseresult',
            unique_together=set([('owner', 'phase', 'section', 'gestureTested', 'cycle')]),
        ),
    ]
