# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_auto_20150702_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseresult',
            name='phase',
            field=models.ForeignKey(related_name='ExerciseResults', to='exercises.Phase'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exerciseresult',
            name='section',
            field=models.ForeignKey(related_name='ExerciseResults', to='exercises.Section'),
            preserve_default=True,
        ),
    ]
