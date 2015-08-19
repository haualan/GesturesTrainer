import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils import timezone

from exercises.models import *

User = get_user_model()

all_users = ( 'user121' , 
  'user122' , 
  'user123' , 
  'user124' , 
  'user125' , 
  'user126' , 
  'user128' , 
  'user130' , 
  'user131' , 
  'user132' , 
  'user133' , 
  'user134' , 
  'user135' , 
  'user136' , 
  'user137' , 
  'user138' , 
  'user139' , 
  'user140' , 
  'user141' , 
  'user142' , 
  'user143' , 
  'user144' , 
  'user145' , 
  'user146' , 
  'user208' , 
  'user209' , 
  'user210' , 
  'user211' , 
  'user212' , 
  'user213' , 
  'user214' , 
  'user215' , 
  'user216' , 
  'user217' , 
  'user218' , 
  'user219' , 
  'user220' , 
  'user221' , 
)

def deleteData(username):
  try:
    print 'delete user data:', username
    user = User.objects.get(username = username)
    inst = ExerciseResult.objects.filter(owner = user)
    inst.delete()
  except:
      print 'There was a problem. Error: {}.' \
          .format(sys.exc_info()[1])

if __name__ == '__main__':
  for i in all_users:
    deleteData(i)