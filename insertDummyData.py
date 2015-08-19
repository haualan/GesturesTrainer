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
      
      ('user122', 'phase1', 'pretest'),
      ('user122', 'phase1', 'training1'),
      ('user122', 'phase1', 'training2'),
      ('user122', 'phase1', 'training3'),
    )

  for i in payload:
    insertSectionDummy(*i)
