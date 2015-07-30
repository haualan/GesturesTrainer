# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0012_auto_20150730_0700'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exerciseresult',
            unique_together=set([('owner', 'phase', 'section', 'gestureTested')]),
        ),
    ]
