# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_auto_20150713_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseresult',
            name='phase',
            field=models.CharField(max_length=100, choices=[(b'phase1', b'Phase I'), (b'phase2', b'Phase II'), (b'phase3', b'Phase III')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exerciseresult',
            name='section',
            field=models.CharField(max_length=100, choices=[(b'pretest', b'Pre-test'), (b'training', b'Training'), (b'posttest1', b'Post-Test I'), (b'posttest2', b'Post-Test II'), (b'posttest3', b'Post-Test III')]),
            preserve_default=True,
        ),
    ]
