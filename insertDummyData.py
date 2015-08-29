import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils import timezone

from exercises.models import *

User = get_user_model()

def insertSingleDummy(username, phase, section, gestureTested ):
  try:
    print 'inserting dummyData:', username, phase, section, gestureTested
    user = User.objects.get(username = username)
    inst = ExerciseResult(owner = user, 
                          phase = phase, 
                          section = section, 
                          gestureTested = gestureTested,
                          response = 'dummyData')
    inst.save()
  except:
      print 'There was a problem. Error: {}.' \
          .format(sys.exc_info()[1])

def insertSectionDummy(username, phase, section, *args):
  for gesture in QUESTIONS:
    insertSingleDummy(username, phase, section, gesture )


if __name__ == '__main__':
  payload = (
      ('user121', 'phase1', 'pretest'),
('user121', 'phase1', 'training1'),
('user121', 'phase1', 'training2'),
('user121', 'phase1', 'training3'),
('user121', 'phase1', 'training4'),
('user121', 'phase1', 'posttest1'),

('user125', 'phase1', 'pretest'),
('user125', 'phase1', 'training1'),
('user125', 'phase1', 'training2'),
('user125', 'phase1', 'training3'),
('user125', 'phase1', 'training4'),
('user125', 'phase1', 'posttest1'),
('user125', 'phase1', 'posttest2'),

('user128', 'phase1', 'pretest'),
('user128', 'phase1', 'training1'),
('user128', 'phase1', 'training2'),
('user128', 'phase1', 'training3'),
('user128', 'phase1', 'training4'),
('user128', 'phase1', 'posttest1'),
('user128', 'phase1', 'posttest2'),

('user131', 'phase1', 'pretest'),
('user131', 'phase1', 'training1'),
('user131', 'phase1', 'training2'),
('user131', 'phase1', 'training3'),
('user131', 'phase1', 'training4'),
('user131', 'phase1', 'posttest1'),
('user131', 'phase1', 'posttest2'),

('user132', 'phase1', 'pretest'),
('user132', 'phase1', 'training1'),
('user132', 'phase1', 'training2'),
('user132', 'phase1', 'training3'),
('user132', 'phase1', 'training4'),
('user132', 'phase1', 'posttest1'),
('user132', 'phase1', 'posttest2'),

('user134', 'phase1', 'pretest'),
('user134', 'phase1', 'training1'),
('user134', 'phase1', 'training2'),
('user134', 'phase1', 'training3'),
('user134', 'phase1', 'training4'),
('user134', 'phase1', 'posttest1'),
('user134', 'phase1', 'posttest2'),

('user136', 'phase1', 'pretest'),
('user136', 'phase1', 'training1'),
('user136', 'phase1', 'training2'),
('user136', 'phase1', 'training3'),
('user136', 'phase1', 'training4'),
('user136', 'phase1', 'posttest1'),
('user136', 'phase1', 'posttest2'),

('user138', 'phase1', 'pretest'),
('user138', 'phase1', 'training1'),
('user138', 'phase1', 'training2'),
('user138', 'phase1', 'training3'),
('user138', 'phase1', 'training4'),
('user138', 'phase1', 'posttest1'),

('user139', 'phase1', 'pretest'),
('user139', 'phase1', 'training1'),
('user139', 'phase1', 'training2'),
('user139', 'phase1', 'training3'),
('user139', 'phase1', 'training4'),
('user139', 'phase1', 'posttest1'),
('user139', 'phase1', 'posttest2'),

('user141', 'phase1', 'pretest'),
('user141', 'phase1', 'training1'),
('user141', 'phase1', 'training2'),
('user141', 'phase1', 'training3'),
('user141', 'phase1', 'training4'),
('user141', 'phase1', 'posttest1'),
('user141', 'phase1', 'posttest2'),

('user143', 'phase1', 'pretest'),
('user143', 'phase1', 'training1'),
('user143', 'phase1', 'training2'),
('user143', 'phase1', 'training3'),
('user143', 'phase1', 'training4'),
('user143', 'phase1', 'posttest1'),

('user144', 'phase1', 'pretest'),
('user144', 'phase1', 'training1'),
('user144', 'phase1', 'training2'),
('user144', 'phase1', 'training3'),
('user144', 'phase1', 'training4'),
('user144', 'phase1', 'posttest1'),
('user144', 'phase1', 'posttest2'),

('user145', 'phase1', 'pretest'),
('user145', 'phase1', 'training1'),
('user145', 'phase1', 'training2'),
('user145', 'phase1', 'training3'),
('user145', 'phase1', 'training4'),
('user145', 'phase1', 'posttest1'),
('user145', 'phase1', 'posttest2'),

('user208', 'phase1', 'pretest'),
('user208', 'phase1', 'training1'),
('user208', 'phase1', 'training2'),
('user208', 'phase1', 'training3'),
('user208', 'phase1', 'training4'),
('user208', 'phase1', 'posttest1'),
('user208', 'phase1', 'posttest2'),

('user210', 'phase1', 'pretest'),
('user210', 'phase1', 'training1'),
('user210', 'phase1', 'training2'),
('user210', 'phase1', 'training3'),
('user210', 'phase1', 'training4'),
('user210', 'phase1', 'posttest1'),

('user211', 'phase1', 'pretest'),

('user212', 'phase1', 'pretest'),
('user212', 'phase1', 'training1'),
('user212', 'phase1', 'training2'),
('user212', 'phase1', 'training3'),
('user212', 'phase1', 'training4'),
('user212', 'phase1', 'posttest1'),

('user214', 'phase1', 'pretest'),
('user214', 'phase1', 'training1'),
('user214', 'phase1', 'training2'),
('user214', 'phase1', 'training3'),
('user214', 'phase1', 'training4'),
('user214', 'phase1', 'posttest1'),
('user214', 'phase1', 'posttest2'),

('user215', 'phase1', 'pretest'),
('user215', 'phase1', 'training1'),
('user215', 'phase1', 'training2'),
('user215', 'phase1', 'training3'),
('user215', 'phase1', 'training4'),
('user215', 'phase1', 'posttest1'),
('user215', 'phase1', 'posttest2'),

('user218', 'phase1', 'pretest'),
('user218', 'phase1', 'training1'),
('user218', 'phase1', 'training2'),
('user218', 'phase1', 'training3'),
('user218', 'phase1', 'training4'),

('user219', 'phase1', 'pretest'),
('user219', 'phase1', 'training1'),
('user219', 'phase1', 'training2'),
('user219', 'phase1', 'training3'),
('user219', 'phase1', 'training4'),
('user219', 'phase1', 'posttest1'),
('user219', 'phase1', 'posttest2'),

('user220', 'phase1', 'pretest'),
('user220', 'phase1', 'training1'),
('user220', 'phase1', 'training2'),
('user220', 'phase1', 'training3'),
('user220', 'phase1', 'training4'),
('user220', 'phase1', 'posttest1'),
('user220', 'phase1', 'posttest2'),

('user221', 'phase1', 'pretest'),
('user221', 'phase1', 'training1'),
('user221', 'phase1', 'training2'),
('user221', 'phase1', 'training3'),
('user221', 'phase1', 'training4'),
('user221', 'phase1', 'posttest1'),
('user221', 'phase1', 'posttest2'),

    )

  for i in payload:
    insertSectionDummy(*i)
