# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('phase', models.CharField(max_length=100, choices=[(b'phase1', b'Phase I'), (b'phase2', b'Phase II'), (b'phase3', b'Phase III')])),
                ('section', models.CharField(max_length=100, choices=[(b'pretest', b'Pre-test'), (b'training', b'Training'), (b'posttest1', b'Post-Test I'), (b'posttest2', b'Post-Test II'), (b'posttest3', b'Post-Test III')])),
                ('gestureTested', models.CharField(max_length=100)),
                ('response', models.CharField(max_length=100, choices=[(b'angry', b'angry'), (b'awesome', b'awesome'), (b'drive', b'drive'), (b'eat', b'eat'), (b'bird', b'bird'), (b'goodbye', b'goodbye'), (b'hello', b'hello'), (b'hug', b'hug'), (b'hungry', b'hungry'), (b'mine', b'mine'), (b'notAllowed', b'notAllowed'), (b'yes', b'yes'), (b'annoyed', b'annoyed'), (b'baby', b'baby'), (b'come', b'come'), (b'wait', b'wait'), (b'walk', b'walk'), (b'welcome', b'welcome'), (b'where', b'where'), (b'wrong', b'wrong'), (b'timedOut', b'No response made within time limit'), (b'noResponseRequired', b'No response made for example a training section, where it is not required')])),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
