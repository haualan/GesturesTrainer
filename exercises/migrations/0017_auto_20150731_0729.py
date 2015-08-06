# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0016_auto_20150730_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseresult',
            name='section',
            field=models.CharField(max_length=100, choices=[(b'pretest', b'Pre-test'), (b'training1', b'Training'), (b'training2', b'Training'), (b'training3', b'Training'), (b'training4', b'Training'), (b'posttest1', b'Post-Test I'), (b'posttest2', b'Post-Test II'), (b'posttest3', b'Post-Test III')]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='exerciseresult',
            unique_together=set([('owner', 'phase', 'section', 'gestureTested')]),
        ),
    ]
