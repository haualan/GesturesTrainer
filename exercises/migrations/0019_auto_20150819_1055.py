# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0018_auto_20150819_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseresult',
            name='gestureTested',
            field=models.CharField(blank=True, max_length=100, choices=[(b'angry', b'angry'), (b'awesome', b'awesome'), (b'drive', b'drive'), (b'eat', b'eat'), (b'bird', b'bird'), (b'goodbye', b'goodbye'), (b'hello', b'hello'), (b'hug', b'hug'), (b'hungry', b'hungry'), (b'mine', b'mine'), (b'notAllowed', b'notAllowed'), (b'yes', b'yes'), (b'annoyed', b'annoyed'), (b'baby', b'baby'), (b'come', b'come'), (b'wait', b'wait'), (b'walk', b'walk'), (b'welcome', b'welcome'), (b'where', b'where'), (b'wrong', b'wrong'), (b'timedOut', b'No response made within time limit'), (b'noResponseRequired', b'No response required for section'), (b'dontKnow', b'User doesnt know response'), (b'correct', b'correct response'), (b'incorrect', b'incorrect response'), (b'dummyData', b'dummyData')]),
        ),
    ]
