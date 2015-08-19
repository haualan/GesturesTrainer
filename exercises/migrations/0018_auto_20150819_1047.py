# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0017_auto_20150731_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseresult',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='exerciseresult',
            name='gestureTested',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='exerciseresult',
            name='phase',
            field=models.CharField(max_length=100, choices=[(b'phase1', b'Phase 1'), (b'phase2', b'Phase 2'), (b'phase3', b'Phase 3')]),
        ),
        migrations.AlterField(
            model_name='exerciseresult',
            name='response',
            field=models.CharField(max_length=100, choices=[(b'angry', b'angry'), (b'awesome', b'awesome'), (b'drive', b'drive'), (b'eat', b'eat'), (b'bird', b'bird'), (b'goodbye', b'goodbye'), (b'hello', b'hello'), (b'hug', b'hug'), (b'hungry', b'hungry'), (b'mine', b'mine'), (b'notAllowed', b'notAllowed'), (b'yes', b'yes'), (b'annoyed', b'annoyed'), (b'baby', b'baby'), (b'come', b'come'), (b'wait', b'wait'), (b'walk', b'walk'), (b'welcome', b'welcome'), (b'where', b'where'), (b'wrong', b'wrong'), (b'timedOut', b'No response made within time limit'), (b'noResponseRequired', b'No response required for section'), (b'dontKnow', b'User doesnt know response'), (b'correct', b'correct response'), (b'incorrect', b'incorrect response'), (b'dummyData', b'dummyData')]),
        ),
        migrations.AlterField(
            model_name='exerciseresult',
            name='section',
            field=models.CharField(max_length=100, choices=[(b'pretest', b'Pre-test'), (b'training1', b'Training 1'), (b'training2', b'Training 2'), (b'training3', b'Training 3'), (b'training4', b'Training 4'), (b'posttest1', b'Post-Test 1'), (b'posttest2', b'Post-Test 2'), (b'posttest3', b'Post-Test 3')]),
        ),
    ]
