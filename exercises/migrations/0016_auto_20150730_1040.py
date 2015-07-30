# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0015_auto_20150730_0726'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exerciseresult',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='exerciseresult',
            name='cycle',
        ),
    ]
