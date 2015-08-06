# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_auto_20150702_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseresult',
            name='phase',
            field=models.ForeignKey(to='exercises.Phase'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exerciseresult',
            name='section',
            field=models.ForeignKey(to='exercises.Section'),
            preserve_default=True,
        ),
    ]
