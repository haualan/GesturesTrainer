#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

phase_choices = (
      ('phase1', 'Phase 1'),
      ('phase2', 'Phase 2'),
      ('phase3', 'Phase 3'),
  )
section_choices = (
      ('pretest', 'Pre-test'),
      ('training1', 'Training 1'),
      ('training2', 'Training 2'),
      ('training3', 'Training 3'),
      ('training4', 'Training 4'),
      ('posttest1', 'Post-Test 1'),
      ('posttest2', 'Post-Test 2'),
      ('posttest3', 'Post-Test 3'),
    )

response_choices = (
    ('angry', 'angry'),
    ('awesome', 'awesome'),
    ('drive','drive'),
    ('eat','eat'),
    ('bird','bird'),
    ('goodbye','goodbye'),
    ('hello','hello'),
    ('hug','hug'),
    ('hungry','hungry'),
    ('mine','mine'),
    ('notAllowed','notAllowed'),
    ('yes','yes'),
    ('annoyed','annoyed'),
    ('baby','baby'),
    ('come','come'),
    ('wait','wait'),
    ('walk','walk'),
    ('welcome','welcome'),
    ('where','where'),
    ('wrong','wrong'),
    ('timedOut', 'No response made within time limit'),
    ('noResponseRequired', 'No response required for section'),
    ('dontKnow', 'User doesnt know response'),
    ('correct', 'correct response'),
    ('incorrect', 'incorrect response'),
    ('dummyData', 'dummyData'),
  )

class Phase(models.Model):
  phase = models.CharField(max_length = 100)
  order = models.IntegerField()

  def __str__(self):            
    return self.phase

class Section(models.Model):
  section = models.CharField(max_length = 100)
  order = models.IntegerField()

  def __str__(self):            
    return self.section

class PhaseSection(models.Model):
  phase = models.CharField(max_length = 100)
  section = models.CharField(max_length = 100)
  start_date = models.DateTimeField(blank=True)


class ExerciseResult(models.Model):
  created = models.DateTimeField(default=timezone.now, blank=True)
  owner = models.ForeignKey('auth.User')
  phase = models.CharField(max_length= 100, choices = phase_choices)
  # phase = models.ForeignKey('Phase', related_name='ExerciseResults')
  section = models.CharField(max_length= 100, choices = section_choices)
  # section = models.ForeignKey('Section', related_name='ExerciseResults')
  # # cycle describes how many times the section has been performed on user
  # cycle = models.IntegerField(default = 1)
  gestureTested = models.CharField(max_length = 100)
  response = models.CharField(max_length = 100, choices = response_choices )

  class Meta:
    unique_together = ('owner', 'phase', 'section', 'gestureTested')


# p1_assessment_prefix = '/media/phase1/assessment/'
# p1_feedback_prefix = '/media/phase1/feedback/'
# p1_training_prefix = '/media/phase1/training/'

# p2_assessment_prefix = '/media/phase2/assessment/'
# p2_feedback_prefix = '/media/phase2/feedback/'
# p2_training_prefix = '/media/phase2/training/'

# p3_assessment_prefix = '/media/phase3/assessment/'
# p3_feedback_prefix = '/media/phase3/feedback/'
# p3_training_prefix = '/media/phase3/training/'

# p1_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase1/assessment/'
# p1_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase1/feedback/'
# p1_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase1/training/'

# p2_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase2/assessment/'
# p2_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase2/feedback/'
# p2_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase2/training/'

# p3_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase3/assessment/'
# p3_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase3/feedback/'
# p3_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase3/training/'


# s2p676t87j2cwx.cloudfront.net
# "rtmp://RTMP-DISTRIBUTION-DOMAIN-NAME/cfx/st/VIDEO-FILE-NAME"
# cloudfront for distro
# p1_assessment_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase1/assessment/'
# p1_feedback_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase1/feedback/'
# p1_training_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase1/training/'

# p2_assessment_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase2/assessment/'
# p2_feedback_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase2/feedback/'
# p2_training_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase2/training/'

# p3_assessment_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase3/assessment/'
# p3_feedback_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase3/feedback/'
# p3_training_prefix = 'rtmp://s2p676t87j2cwx.cloudfront.net/cfx/st/mp4:phase3/training/'


# new awsand cloudfront
p1_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'
p1_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'
p1_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'

p2_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'
p2_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'
p2_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'

p3_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'
p3_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'
p3_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmediav2/'




p1_assessment_prefix = 'rtmp://s1walhiktvwlah.cloudfront.net/cfx/st/mp4:'
p1_feedback_prefix = p1_assessment_prefix
p1_training_prefix = p1_assessment_prefix

p2_assessment_prefix = p1_assessment_prefix
p2_feedback_prefix = p1_assessment_prefix
p2_training_prefix = p1_assessment_prefix

p3_assessment_prefix = p1_assessment_prefix
p3_feedback_prefix = p1_assessment_prefix
p3_training_prefix = p1_assessment_prefix



# cloudinary, for each filename no spaces allowed
p1_assessment_prefix = 'http://res.cloudinary.com/qwertyuiop/video/upload/'
p1_feedback_prefix = p1_assessment_prefix
p1_training_prefix = p1_assessment_prefix

p2_assessment_prefix = p1_assessment_prefix
p2_feedback_prefix = p1_assessment_prefix
p2_training_prefix = p1_assessment_prefix

p3_assessment_prefix = p1_assessment_prefix
p3_feedback_prefix = p1_assessment_prefix
p3_training_prefix = p1_assessment_prefix


# phase 3 had video issues where the scenarios are not uniform in length so the buttons don't light up correctly. 
# Each video must now have its own cutoff time
P3_VIDEO_CUTOFF = {
  'angry' : ( 20  , 21  , 22  , 22  ) ,
  'awesome' : ( 22  , 23  , 23  , 23  ) ,
  'drive' : ( 20  , 20  , 21  , 22  ) ,
  'eat' : ( 19  , 20  , 19  , 20  ) ,
  'bird'  : ( 20  , 20  , 20  , 20  ) ,
  'goodbye'  : ( 23  , 24  , 21  , 23  ) ,
  'hello' : ( 23  , 23  , 23  , 22  ) ,
  'hug' : ( 21  , 21  , 21  , 20  ) ,
  'hungry'  : ( 20  , 20  , 21  , 20  ) ,
  'mine'  : ( 19  , 19  , 19  , 19  ) ,
  'notAllowed'  : ( 20  , 20  , 19  , 19  ) ,
  'yes' : ( 23  , 23  , 22  , 22  ) ,
  'annoyed' : ( 22  , 21  , 22  , 22  ) ,
  'baby'  : ( 20  , 19  , 20  , 19  ) ,
  'come'  : ( 19  , 19  , 19  , 19  ) ,
  'wait'  : ( 22  , 20  , 20  , 21  ) ,
  'walk'  : ( 19  , 20  , 19  , 19  ) ,
  'welcome' : ( 19  , 20  , 19  , 20  ) ,
  'where' : ( 19  , 20  , 20  , 20  ) ,
  'wrong' : ( 20  , 22  , 20  , 21  ) ,
}

VIDEOS = {      
  # video played at beginning of the assessment / pretest / posttest, general greetings and instructions
  # 你好呀， 小朋友！今日好開心可以見到你。 跟住落嚟我會向你示範一D手勢。請你話比我知你覺得呢D手勢係代表咩意思。
  'p1_assessment_greetingAndInstruction': '{}Phase I assessment_greeting and instruction.mp4'.format(p1_assessment_prefix),

  # video that asks if user understands the instructions
  'p1_assessment_doYouUnderstand': '{}do you understand.mp4'.format(p1_assessment_prefix),

  # video that plays before each question is asked -- "Let's take a look at this gesture. What does it mean?"
  # 你覺得呢個手勢係代表咩意思呢？
  'p1_assessment_instructionPreGesture': '{}Phase I assessment_gesture instruction 1.mp4'.format(p1_assessment_prefix),

  # video demontrating the gestures and asking what does user think it means:
  'p1_assessment_angryGesture' :  '{}Phase I assessment_gesture instruction 2_angry.mp4'.format(p1_assessment_prefix),
  'p1_assessment_awesomeGesture':  '{}Phase I assessment_gesture instruction 2_clapping.mp4'.format(p1_assessment_prefix),
  'p1_assessment_driveGesture':  '{}Phase I assessment_gesture instruction 2_driving.mp4'.format(p1_assessment_prefix),
  'p1_assessment_eatGesture':  '{}Phase I assessment_gesture instruction 2_eating3.mp4'.format(p1_assessment_prefix),
  'p1_assessment_birdGesture':  '{}Phase I assessment_gesture instruction 2_flying.mp4'.format(p1_assessment_prefix),
  'p1_assessment_goodbyeGesture':  '{}Phase I assessment_gesture instruction 2_goodbye.mp4'.format(p1_assessment_prefix),
  'p1_assessment_helloGesture':  '{}Phase I assessment_gesture instruction 2_handshake3.mp4'.format(p1_assessment_prefix),
  'p1_assessment_hugGesture':  '{}Phase I assessment_gesture instruction 2_hugging.mp4'.format(p1_assessment_prefix),
  'p1_assessment_hungryGesture':  '{}Phase I assessment_gesture instruction 2_hungry.mp4'.format(p1_assessment_prefix),
  'p1_assessment_mineGesture':  '{}Phase I assessment_gesture instruction 2_myself.mp4'.format(p1_assessment_prefix),
  'p1_assessment_notAllowedGesture':  '{}Phase I assessment_gesture instruction 2_no2.mp4'.format(p1_assessment_prefix),
  'p1_assessment_yesGesture':  '{}Phase I assessment_gesture instruction 2_nodding.mp4'.format(p1_assessment_prefix),
  'p1_assessment_annoyedGesture':  '{}Phase I assessment_gesture instruction 2_puzzled.mp4'.format(p1_assessment_prefix),
  'p1_assessment_babyGesture':  '{}Phase I assessment_gesture instruction 2_rocking baby BB.mp4'.format(p1_assessment_prefix),
  'p1_assessment_comeGesture':  '{}Phase I assessment_gesture instruction 2_show direction.mp4'.format(p1_assessment_prefix),
  'p1_assessment_waitGesture':  '{}Phase I assessment_gesture instruction 2_wait long.mp4'.format(p1_assessment_prefix),
  'p1_assessment_walkGesture':  '{}Phase I assessment_gesture instruction 2_walking5.mp4'.format(p1_assessment_prefix),
  'p1_assessment_welcomeGesture':  '{}Phase I assessment_gesture instruction 2_welcome.mp4'.format(p1_assessment_prefix),
  'p1_assessment_whereGesture':  '{}Phase I assessment_gesture instruction 2_where2.mp4'.format(p1_assessment_prefix),
  'p1_assessment_wrongGesture':  '{}Phase I assessment_gesture instruction 2_wrong4.mp4'.format(p1_assessment_prefix),

  # video that plays after the gesture is demonstrated, but stages for the choices coming ahead:
  # 你覺得佢嘅意思係
  'p1_assessment_instructionPostGesture':   '{}Phase I assessment_gesture instruction 3.mp4'.format(p1_assessment_prefix),



  # video with speech only, spoken without gestures just to list out the available choices
  'p1_assessment_angryChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_angry.mp4'.format(p1_assessment_prefix),
  'p1_assessment_awesomeChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_clapping.mp4'.format(p1_assessment_prefix),
  'p1_assessment_driveChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_driving.mp4'.format(p1_assessment_prefix),
  'p1_assessment_eatChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_eating3.mp4'.format(p1_assessment_prefix),
  'p1_assessment_birdChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_flying.mp4'.format(p1_assessment_prefix),
  'p1_assessment_goodbyeChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_goodbye.mp4'.format(p1_assessment_prefix),
  'p1_assessment_helloChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_handshake3.mp4'.format(p1_assessment_prefix),
  'p1_assessment_hugChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_hugging.mp4'.format(p1_assessment_prefix),
  'p1_assessment_hungryChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_hungry.mp4'.format(p1_assessment_prefix),
  'p1_assessment_mineChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_myself.mp4'.format(p1_assessment_prefix),
  'p1_assessment_notAllowedChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_no2.mp4'.format(p1_assessment_prefix),
  'p1_assessment_yesChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_nodding.mp4'.format(p1_assessment_prefix),
  'p1_assessment_annoyedChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_puzzled.mp4'.format(p1_assessment_prefix),
  'p1_assessment_babyChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_rocking baby BB.mp4'.format(p1_assessment_prefix),
  'p1_assessment_comeChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_show direction.mp4'.format(p1_assessment_prefix),
  'p1_assessment_waitChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_wait long.mp4'.format(p1_assessment_prefix),
  'p1_assessment_walkChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_walking5.mp4'.format(p1_assessment_prefix),
  'p1_assessment_welcomeChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_welcome.mp4'.format(p1_assessment_prefix),
  'p1_assessment_whereChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_where2.mp4'.format(p1_assessment_prefix),
  'p1_assessment_wrongChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_wrong4.mp4'.format(p1_assessment_prefix),

  # video with speech only to prompt user to make a choice
  # 請你將你覺得啱嘅答案講出嚟或者指比老師睇。(all three answers are staying on the screen)
  'p1_assessment_makeAChoiceNow':   '{}Phase I assessment_gesture instruction 4.mp4'.format(p1_assessment_prefix),

  # Thank you video for any repsonse chosen during pretest, this is a short thankyou Response
  'p1_feedback_thankyou':   '{}Phase I assessment_gesture feedback_thank youv2.mp4'.format(p1_feedback_prefix),

  # This is a longer response given when user makes a correct choice given during posttest
  'p1_feedback_correct':    '{}Phase I assessment_gesture feedback_correct.mp4'.format(p1_feedback_prefix),

  # these are feedback videos if the incorrect gestures are made, the video demonstrates the correct gesture
  'p1_feedback_angryIncorrect':     '{}Phase I assessment_gesture feedback_incorrect_angry.mp4'.format(p1_feedback_prefix),
  'p1_feedback_awesomeIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_clapping.mp4'.format(p1_feedback_prefix),
  'p1_feedback_driveIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_driving.mp4'.format(p1_feedback_prefix),
  'p1_feedback_eatIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_eating3.mp4'.format(p1_feedback_prefix),
  'p1_feedback_birdIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_flying.mp4'.format(p1_feedback_prefix),
  'p1_feedback_goodbyeIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_goodbye.mp4'.format(p1_feedback_prefix),
  'p1_feedback_helloIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_handshake3.mp4'.format(p1_feedback_prefix),
  'p1_feedback_hugIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_hugging.mp4'.format(p1_feedback_prefix),
  'p1_feedback_hungryIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_hungry.mp4'.format(p1_feedback_prefix),
  'p1_feedback_mineIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_myself.mp4'.format(p1_feedback_prefix),
  'p1_feedback_notAllowedIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_no2.mp4'.format(p1_feedback_prefix),
  'p1_feedback_yesIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_nodding.mp4'.format(p1_feedback_prefix),
  'p1_feedback_annoyedIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_puzzled.mp4'.format(p1_feedback_prefix),
  'p1_feedback_babyIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_rocking baby BB.mp4'.format(p1_feedback_prefix),
  'p1_feedback_comeIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_show direction.mp4'.format(p1_feedback_prefix),
  'p1_feedback_waitIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_wait long.mp4'.format(p1_feedback_prefix),
  'p1_feedback_walkIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_walking5.mp4'.format(p1_feedback_prefix),
  'p1_feedback_welcomeIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_welcome.mp4'.format(p1_feedback_prefix),
  'p1_feedback_whereIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_where2.mp4'.format(p1_feedback_prefix),
  'p1_feedback_wrongIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_wrong4.mp4'.format(p1_feedback_prefix),

  # greeting and instructions for the training section
  'p1_training_greetingAndInstruction': '{}Phase I training_greeting and instruction.mp4'.format(p1_training_prefix),

  # video that asks if user understands the instructions, specifcally for the training section
  'p1_training_doYouUnderstand': '{}do you understand.mp4'.format(p1_training_prefix),

  # these training videos demonstrate the gestures to the user, no response is expected from the user on the training sections
  'p1_training_angryTraining':     '{}Phase I training_gesture_angry_combined.mp4'.format(p1_training_prefix),
  'p1_training_awesomeTraining':  '{}Phase I training_gesture_clapping_combined.mp4'.format(p1_training_prefix),
  'p1_training_driveTraining':  '{}Phase I training_gesture_driving_combined.mp4'.format(p1_training_prefix),
  'p1_training_eatTraining':  '{}Phase I training_gesture_eating3_combined.mp4'.format(p1_training_prefix),
  'p1_training_birdTraining':  '{}Phase I training_gesture_flying_combined.mp4'.format(p1_training_prefix),
  'p1_training_goodbyeTraining':  '{}Phase I training_gesture_goodbye_combined.mp4'.format(p1_training_prefix),
  'p1_training_helloTraining':  '{}Phase I training_gesture_handshake3_combined.mp4'.format(p1_training_prefix),
  'p1_training_hugTraining':  '{}Phase I training_gesture_hugging_combined.mp4'.format(p1_training_prefix),
  'p1_training_hungryTraining':  '{}Phase I training_gesture_hungry_combined.mp4'.format(p1_training_prefix),
  'p1_training_mineTraining':  '{}Phase I training_gesture_myself_combined.mp4'.format(p1_training_prefix),
  'p1_training_notAllowedTraining':  '{}Phase I training_gesture_no2_combined.mp4'.format(p1_training_prefix),
  'p1_training_yesTraining':  '{}Phase I training_gesture_nodding_combined.mp4'.format(p1_training_prefix),
  'p1_training_annoyedTraining':  '{}Phase I training_gesture_puzzled_combined.mp4'.format(p1_training_prefix),
  'p1_training_babyTraining':  '{}Phase I training_gesture_rocking baby BB_combined.mp4'.format(p1_training_prefix),
  'p1_training_comeTraining':  '{}Phase I training_gesture_show direction_combined.mp4'.format(p1_training_prefix),
  'p1_training_waitTraining':  '{}Phase I training_gesture_wait long_combined.mp4'.format(p1_training_prefix),
  'p1_training_walkTraining':  '{}Phase I training_gesture_walking5_combined.mp4'.format(p1_training_prefix),
  'p1_training_welcomeTraining':  '{}Phase I training_gesture_welcome_combined.mp4'.format(p1_training_prefix),
  'p1_training_whereTraining':  '{}Phase I training_gesture_where2_combined.mp4'.format(p1_training_prefix),
  'p1_training_wrongTraining':  '{}Phase I training_gesture_wrong4_combined.mp4'.format(p1_training_prefix),

  # video played at beginning of the assessment / pretest / posttest, general greetings and instructions
  # "I am going to say a word to you. Can you do the gesture the word for me?
  # 跟住落嚟我會講一個詞語比你聽，然後請你向我做出呢個詞語嘅手勢。
  'p2_assessment_greetingAndInstruction': '{}Phase II assessment_greeting and instruction.mp4'.format(p2_assessment_prefix),

  # video that asks if user understands the instructions
  'p2_assessment_doYouUnderstand': '{}do you understand.mp4'.format(p2_assessment_prefix),

  #   "Let's listen to the word that I am going to say. What is this gesture?" Say the word. "What is this gesture?" Teacher / parent provides feedback to the system
  # 請你聽下我之後所講嘅詞語，然後向我做出呢個詞語嘅手勢。
  'p2_assessment_instructionPreGesture': '{}Phase II assessment_gesture instruction 1.mp4'.format(p2_assessment_prefix),

  # video demontrating the gestures and asking what does user think it means:
  'p2_assessment_angryGesture' :  '{}Phase II assessment_gesture instruction 2_angry.mp4'.format(p2_assessment_prefix),
  'p2_assessment_awesomeGesture':  '{}Phase II assessment_gesture instruction 2_clapping.mp4'.format(p2_assessment_prefix),
  'p2_assessment_driveGesture':  '{}Phase II assessment_gesture instruction 2_driving.mp4'.format(p2_assessment_prefix),
  'p2_assessment_eatGesture':  '{}Phase II assessment_gesture instruction 2_eating3.mp4'.format(p2_assessment_prefix),
  'p2_assessment_birdGesture':  '{}Phase II assessment_gesture instruction 2_flying.mp4'.format(p2_assessment_prefix),
  'p2_assessment_goodbyeGesture':  '{}Phase II assessment_gesture instruction 2_goodbye.mp4'.format(p2_assessment_prefix),
  'p2_assessment_helloGesture':  '{}Phase II assessment_gesture instruction 2_handshake3.mp4'.format(p2_assessment_prefix),
  'p2_assessment_hugGesture':  '{}Phase II assessment_gesture instruction 2_hugging.mp4'.format(p2_assessment_prefix),
  'p2_assessment_hungryGesture':  '{}Phase II assessment_gesture instruction 2_hungry.mp4'.format(p2_assessment_prefix),
  'p2_assessment_mineGesture':  '{}Phase II assessment_gesture instruction 2_myself.mp4'.format(p2_assessment_prefix),
  'p2_assessment_notAllowedGesture':  '{}Phase II assessment_gesture instruction 2_no2.mp4'.format(p2_assessment_prefix),
  'p2_assessment_yesGesture':  '{}Phase II assessment_gesture instruction 2_nodding.mp4'.format(p2_assessment_prefix),
  'p2_assessment_annoyedGesture':  '{}Phase II assessment_gesture instruction 2_puzzled.mp4'.format(p2_assessment_prefix),
  'p2_assessment_babyGesture':  '{}Phase II assessment_gesture instruction 2_rocking baby BB.mp4'.format(p2_assessment_prefix),
  'p2_assessment_comeGesture':  '{}Phase II assessment_gesture instruction 2_show direction.mp4'.format(p2_assessment_prefix),
  'p2_assessment_waitGesture':  '{}Phase II assessment_gesture instruction 2_wait long.mp4'.format(p2_assessment_prefix),
  'p2_assessment_walkGesture':  '{}Phase II assessment_gesture instruction 2_walking5.mp4'.format(p2_assessment_prefix),
  'p2_assessment_welcomeGesture':  '{}Phase II assessment_gesture instruction 2_welcome.mp4'.format(p2_assessment_prefix),
  'p2_assessment_whereGesture':  '{}Phase II assessment_gesture instruction 2_where2.mp4'.format(p2_assessment_prefix),
  'p2_assessment_wrongGesture':  '{}Phase II assessment_gesture instruction 2_wrong4.mp4'.format(p2_assessment_prefix),

  # Thank you video for any repsonse chosen during pretest, this is a short thankyou Response
  'p2_feedback_thankyou':   '{}Phase II assessment_gesture feedback_thank you (pretest)v2.mp4'.format(p2_feedback_prefix),

  # greeting and instructions for the training section
  'p2_training_greetingAndInstruction': '{}Phase II training_greeting and instruction.mp4'.format(p2_training_prefix),

  # video that asks if user understands the instructions, specifcally for the training section
  'p2_training_doYouUnderstand': '{}do you understand.mp4'.format(p2_training_prefix),




  # these training videos demonstrate the gestures to the user, no response is expected from the user on the training sections
  'p2_training_angryTraining_1':     '{}Phase II training_gesture_angry_1st.mp4'.format(p2_training_prefix),
  'p2_training_awesomeTraining_1':  '{}Phase II training_gesture_clapping_1st.mp4'.format(p2_training_prefix),
  'p2_training_driveTraining_1':  '{}Phase II training_gesture_driving_1st.mp4'.format(p2_training_prefix),
  'p2_training_eatTraining_1':  '{}Phase II training_gesture_eating3_1st.mp4'.format(p2_training_prefix),
  'p2_training_birdTraining_1':  '{}Phase II training_gesture_flying_1st.mp4'.format(p2_training_prefix),
  'p2_training_goodbyeTraining_1':  '{}Phase II training_gesture_goodbye_1st.mp4'.format(p2_training_prefix),
  'p2_training_helloTraining_1':  '{}Phase II training_gesture_handshake3_1st.mp4'.format(p2_training_prefix),
  'p2_training_hugTraining_1':  '{}Phase II training_gesture_hugging_1st.mp4'.format(p2_training_prefix),
  'p2_training_hungryTraining_1':  '{}Phase II training_gesture_hungry_1st.mp4'.format(p2_training_prefix),
  'p2_training_mineTraining_1':  '{}Phase II training_gesture_myself_1st.mp4'.format(p2_training_prefix),
  'p2_training_notAllowedTraining_1':  '{}Phase II training_gesture_no2_1st.mp4'.format(p2_training_prefix),
  'p2_training_yesTraining_1':  '{}Phase II training_gesture_nodding_1st.mp4'.format(p2_training_prefix),
  'p2_training_annoyedTraining_1':  '{}Phase II training_gesture_puzzled_1st.mp4'.format(p2_training_prefix),
  'p2_training_babyTraining_1':  '{}Phase II training_gesture_rocking baby BB_1st.mp4'.format(p2_training_prefix),
  'p2_training_comeTraining_1':  '{}Phase II training_gesture_show direction_1st.mp4'.format(p2_training_prefix),
  'p2_training_waitTraining_1':  '{}Phase II training_gesture_wait long_1st.mp4'.format(p2_training_prefix),
  'p2_training_walkTraining_1':  '{}Phase II training_gesture_walking5_1st.mp4'.format(p2_training_prefix),
  'p2_training_welcomeTraining_1':  '{}Phase II training_gesture_welcome_1st.mp4'.format(p2_training_prefix),
  'p2_training_whereTraining_1':  '{}Phase II training_gesture_where2_1st.mp4'.format(p2_training_prefix),
  'p2_training_wrongTraining_1':  '{}Phase II training_gesture_wrong4_1st.mp4'.format(p2_training_prefix),

  'p2_training_angryTraining_2':     '{}Phase II training_gesture_angry_2nd.mp4'.format(p2_training_prefix),
  'p2_training_awesomeTraining_2':  '{}Phase II training_gesture_clapping_2nd.mp4'.format(p2_training_prefix),
  'p2_training_driveTraining_2':  '{}Phase II training_gesture_driving_2nd.mp4'.format(p2_training_prefix),
  'p2_training_eatTraining_2':  '{}Phase II training_gesture_eating3_2nd.mp4'.format(p2_training_prefix),
  'p2_training_birdTraining_2':  '{}Phase II training_gesture_flying_2nd.mp4'.format(p2_training_prefix),
  'p2_training_goodbyeTraining_2':  '{}Phase II training_gesture_goodbye_2nd.mp4'.format(p2_training_prefix),
  'p2_training_helloTraining_2':  '{}Phase II training_gesture_handshake3_2nd.mp4'.format(p2_training_prefix),
  'p2_training_hugTraining_2':  '{}Phase II training_gesture_hugging_2nd.mp4'.format(p2_training_prefix),
  'p2_training_hungryTraining_2':  '{}Phase II training_gesture_hungry_2nd.mp4'.format(p2_training_prefix),
  'p2_training_mineTraining_2':  '{}Phase II training_gesture_myself_2nd.mp4'.format(p2_training_prefix),
  'p2_training_notAllowedTraining_2':  '{}Phase II training_gesture_no2_2nd.mp4'.format(p2_training_prefix),
  'p2_training_yesTraining_2':  '{}Phase II training_gesture_nodding_2nd.mp4'.format(p2_training_prefix),
  'p2_training_annoyedTraining_2':  '{}Phase II training_gesture_puzzled_2nd.mp4'.format(p2_training_prefix),
  'p2_training_babyTraining_2':  '{}Phase II training_gesture_rocking baby BB_2nd.mp4'.format(p2_training_prefix),
  'p2_training_comeTraining_2':  '{}Phase II training_gesture_show direction_2nd.mp4'.format(p2_training_prefix),
  'p2_training_waitTraining_2':  '{}Phase II training_gesture_wait long_2nd.mp4'.format(p2_training_prefix),
  'p2_training_walkTraining_2':  '{}Phase II training_gesture_walking5_2nd.mp4'.format(p2_training_prefix),
  'p2_training_welcomeTraining_2':  '{}Phase II training_gesture_welcome_2nd.mp4'.format(p2_training_prefix),
  'p2_training_whereTraining_2':  '{}Phase II training_gesture_where2_2nd.mp4'.format(p2_training_prefix),
  'p2_training_wrongTraining_2':  '{}Phase II training_gesture_wrong4_2nd.mp4'.format(p2_training_prefix),

  # This is a longer response given when user makes a correct choice given during posttest
  'p2_feedback_correct':    '{}Phase II training _ assessment_gesture feedback_correct.mp4'.format(p2_feedback_prefix),

  # these are feedback videos if the incorrect gestures are made, the video demonstrates the correct gesture
  'p2_feedback_angryIncorrect':     '{}Phase II training _ assessment_gesture feedback_incorrect_angry.mp4'.format(p2_feedback_prefix),
  'p2_feedback_awesomeIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_clapping.mp4'.format(p2_feedback_prefix),
  'p2_feedback_driveIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_driving.mp4'.format(p2_feedback_prefix),
  'p2_feedback_eatIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_eating3.mp4'.format(p2_feedback_prefix),
  'p2_feedback_birdIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_flying.mp4'.format(p2_feedback_prefix),
  'p2_feedback_goodbyeIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_goodbye.mp4'.format(p2_feedback_prefix),
  'p2_feedback_helloIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_handshake3.mp4'.format(p2_feedback_prefix),
  'p2_feedback_hugIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_hugging.mp4'.format(p2_feedback_prefix),
  'p2_feedback_hungryIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_hungry.mp4'.format(p2_feedback_prefix),
  'p2_feedback_mineIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_myself.mp4'.format(p2_feedback_prefix),
  'p2_feedback_notAllowedIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_no2.mp4'.format(p2_feedback_prefix),
  'p2_feedback_yesIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_nodding.mp4'.format(p2_feedback_prefix),
  'p2_feedback_annoyedIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_puzzled.mp4'.format(p2_feedback_prefix),
  'p2_feedback_babyIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_rocking baby BB.mp4'.format(p2_feedback_prefix),
  'p2_feedback_comeIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_show direction.mp4'.format(p2_feedback_prefix),
  'p2_feedback_waitIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_wait long.mp4'.format(p2_feedback_prefix),
  'p2_feedback_walkIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_walking5.mp4'.format(p2_feedback_prefix),
  'p2_feedback_welcomeIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_welcome.mp4'.format(p2_feedback_prefix),
  'p2_feedback_whereIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_where2.mp4'.format(p2_feedback_prefix),
  'p2_feedback_wrongIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_wrong4.mp4'.format(p2_feedback_prefix),

  # video played at beginning of the assessment / pretest / posttest, general greetings and instructions
  #   "I am going to ask you what gestures should be produced in certain circumstances"
  # 跟住落嚟我想請問你，喺以下嘅故事裏面，應該做D咩手勢。
  'p3_assessment_greetingAndInstruction': '{}Phase III assessment_greeting and instruction.mp4'.format(p3_assessment_prefix),

  # video that asks if user understands the instructions
  'p3_assessment_doYouUnderstand': '{}do you understand (new nao).mp4'.format(p3_assessment_prefix),

  # video demontrating the gestures and asking what does user think it means:
  'p3_assessment_pretest_angryGesture' :  '{}Phase III assessment_pretest_angry.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_awesomeGesture':  '{}Phase III assessment_pretest_clapping.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_driveGesture':  '{}Phase III assessment_pretest_driving.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_eatGesture':  '{}Phase III assessment_pretest_eating.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_birdGesture':  '{}Phase III assessment_pretest_flying.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_goodbyeGesture':  '{}Phase III assessment_pretest_goodbye.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_helloGesture':  '{}Phase III assessment_pretest_handshake.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_hugGesture':  '{}Phase III assessment_pretest_hugging.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_hungryGesture':  '{}Phase III assessment_pretest_hungry.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_mineGesture':  '{}Phase III assessment_pretest_myself.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_notAllowedGesture':  '{}Phase III assessment_pretest_no.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_yesGesture':  '{}Phase III assessment_pretest_nodding.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_annoyedGesture':  '{}Phase III assessment_pretest_puzzled.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_babyGesture':  '{}Phase III assessment_pretest_rocking baby BB.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_comeGesture':  '{}Phase III assessment_pretest_show direction.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_waitGesture':  '{}Phase III assessment_pretest_wait long.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_walkGesture':  '{}Phase III assessment_pretest_walking.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_welcomeGesture':  '{}Phase III assessment_pretest_welcome.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_whereGesture':  '{}Phase III assessment_pretest_where.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_wrongGesture':  '{}Phase III assessment_pretest_wrong.mp4'.format(p3_assessment_prefix),

  'p3_assessment_posttest1_angryGesture' :  '{}Phase III assessment_posttest 1_angry.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_awesomeGesture':  '{}Phase III assessment_posttest 1_clapping.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_driveGesture':  '{}Phase III assessment_posttest 1_driving.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_eatGesture':  '{}Phase III assessment_posttest 1_eating.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_birdGesture':  '{}Phase III assessment_posttest 1_flying.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_goodbyeGesture':  '{}Phase III assessment_posttest 1_goodbye.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_helloGesture':  '{}Phase III assessment_posttest 1_handshake.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_hugGesture':  '{}Phase III assessment_posttest 1_hugging.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_hungryGesture':  '{}Phase III assessment_posttest 1_hungry.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_mineGesture':  '{}Phase III assessment_posttest 1_myself.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_notAllowedGesture':  '{}Phase III assessment_posttest 1_no.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_yesGesture':  '{}Phase III assessment_posttest 1_nodding.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_annoyedGesture':  '{}Phase III assessment_posttest 1_puzzled.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_babyGesture':  '{}Phase III assessment_posttest 1_rocking baby BB.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_comeGesture':  '{}Phase III assessment_posttest 1_show direction.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_waitGesture':  '{}Phase III assessment_posttest 1_wait long.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_walkGesture':  '{}Phase III assessment_posttest 1_walking.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_welcomeGesture':  '{}Phase III assessment_posttest 1_welcome.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_whereGesture':  '{}Phase III assessment_posttest 1_where.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_wrongGesture':  '{}Phase III assessment_posttest 1_wrong.mp4'.format(p3_assessment_prefix),

  'p3_assessment_posttest2_angryGesture' :  '{}Phase III assessment_posttest 2_angry.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_awesomeGesture':  '{}Phase III assessment_posttest 2_clapping.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_driveGesture':  '{}Phase III assessment_posttest 2_driving.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_eatGesture':  '{}Phase III assessment_posttest 2_eating.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_birdGesture':  '{}Phase III assessment_posttest 2_flying.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_goodbyeGesture':  '{}Phase III assessment_posttest 2_goodbye.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_helloGesture':  '{}Phase III assessment_posttest 2_handshake.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_hugGesture':  '{}Phase III assessment_posttest 2_hugging.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_hungryGesture':  '{}Phase III assessment_posttest 2_hungry.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_mineGesture':  '{}Phase III assessment_posttest 2_myself.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_notAllowedGesture':  '{}Phase III assessment_posttest 2_no.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_yesGesture':  '{}Phase III assessment_posttest 2_nodding.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_annoyedGesture':  '{}Phase III assessment_posttest 2_puzzled.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_babyGesture':  '{}Phase III assessment_posttest 2_rocking baby BB.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_comeGesture':  '{}Phase III assessment_posttest 2_show direction.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_waitGesture':  '{}Phase III assessment_posttest 2_wait long.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_walkGesture':  '{}Phase III assessment_posttest 2_walking.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_welcomeGesture':  '{}Phase III assessment_posttest 2_welcome.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_whereGesture':  '{}Phase III assessment_posttest 2_where.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_wrongGesture':  '{}Phase III assessment_posttest 2_wrong.mp4'.format(p3_assessment_prefix),

  'p3_assessment_posttest3_angryGesture' :  '{}Phase III assessment_posttest 3_angry.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_awesomeGesture':  '{}Phase III assessment_posttest 3_clapping.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_driveGesture':  '{}Phase III assessment_posttest 3_driving.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_eatGesture':  '{}Phase III assessment_posttest 3_eating.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_birdGesture':  '{}Phase III assessment_posttest 3_flying.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_goodbyeGesture':  '{}Phase III assessment_posttest 3_goodbye.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_helloGesture':  '{}Phase III assessment_posttest 3_handshake.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_hugGesture':  '{}Phase III assessment_posttest 3_hugging.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_hungryGesture':  '{}Phase III assessment_posttest 3_hungry.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_mineGesture':  '{}Phase III assessment_posttest 3_myself.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_notAllowedGesture':  '{}Phase III assessment_posttest 3_no.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_yesGesture':  '{}Phase III assessment_posttest 3_nodding.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_annoyedGesture':  '{}Phase III assessment_posttest 3_puzzled.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_babyGesture':  '{}Phase III assessment_posttest 3_rocking baby BB.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_comeGesture':  '{}Phase III assessment_posttest 3_show direction.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_waitGesture':  '{}Phase III assessment_posttest 3_wait long.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_walkGesture':  '{}Phase III assessment_posttest 3_walking.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_welcomeGesture':  '{}Phase III assessment_posttest 3_welcome.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_whereGesture':  '{}Phase III assessment_posttest 3_where.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_wrongGesture':  '{}Phase III assessment_posttest 3_wrong.mp4'.format(p3_assessment_prefix),



  # Thank you video for any repsonse chosen during pretest, this is a short thankyou Response
  'p3_feedback_thankyou':   '{}Phase III training _ assessment_gesture feedback_thank you (pretest)v2.mp4'.format(p3_feedback_prefix),

  # greeting and instructions for the training section
  'p3_training_greetingAndInstruction': '{}Phase III training_greeting and instruction.mp4'.format(p3_training_prefix),

  # video that asks if user understands the instructions, specifcally for the training section
  'p3_training_doYouUnderstand': '{}do you understand (new nao).mp4'.format(p3_training_prefix),

  # these training videos demonstrate the gestures to the user, no response is expected from the user on the training sections
  'p3_training_angryTraining_1':     '{}Phase III training_gesture_angry_1st.mp4'.format(p3_training_prefix),
  'p3_training_awesomeTraining_1':  '{}Phase III training_gesture_clapping_1st.mp4'.format(p3_training_prefix),
  'p3_training_driveTraining_1':  '{}Phase III training_gesture_driving_1st.mp4'.format(p3_training_prefix),
  'p3_training_eatTraining_1':  '{}Phase III training_gesture_eating_1st.mp4'.format(p3_training_prefix),
  'p3_training_birdTraining_1':  '{}Phase III training_gesture_flying_1st.mp4'.format(p3_training_prefix),
  'p3_training_goodbyeTraining_1':  '{}Phase III training_gesture_goodbye_1st.mp4'.format(p3_training_prefix),
  'p3_training_helloTraining_1':  '{}Phase III training_gesture_handshake_1st.mp4'.format(p3_training_prefix),
  'p3_training_hugTraining_1':  '{}Phase III training_gesture_hugging_1st.mp4'.format(p3_training_prefix),
  'p3_training_hungryTraining_1':  '{}Phase III training_gesture_hungry_1st.mp4'.format(p3_training_prefix),
  'p3_training_mineTraining_1':  '{}Phase III training_gesture_myself_1st.mp4'.format(p3_training_prefix),
  'p3_training_notAllowedTraining_1':  '{}Phase III training_gesture_no_1st.mp4'.format(p3_training_prefix),
  'p3_training_yesTraining_1':  '{}Phase III training_gesture_nodding_1st.mp4'.format(p3_training_prefix),
  'p3_training_annoyedTraining_1':  '{}Phase III training_gesture_puzzled_1st.mp4'.format(p3_training_prefix),
  'p3_training_babyTraining_1':  '{}Phase III training_gesture_rocking baby BB_1st.mp4'.format(p3_training_prefix),
  'p3_training_comeTraining_1':  '{}Phase III training_gesture_show direction_1st.mp4'.format(p3_training_prefix),
  'p3_training_waitTraining_1':  '{}Phase III training_gesture_wait long_1st.mp4'.format(p3_training_prefix),
  'p3_training_walkTraining_1':  '{}Phase III training_gesture_walking_1st.mp4'.format(p3_training_prefix),
  'p3_training_welcomeTraining_1':  '{}Phase III training_gesture_welcome_1st.mp4'.format(p3_training_prefix),
  'p3_training_whereTraining_1':  '{}Phase III training_gesture_where_1st.mp4'.format(p3_training_prefix),
  'p3_training_wrongTraining_1':  '{}Phase III training_gesture_wrong_1st.mp4'.format(p3_training_prefix),

  'p3_training_angryTraining_2':     '{}Phase III training_gesture_angry_2nd.mp4'.format(p3_training_prefix),
  'p3_training_awesomeTraining_2':  '{}Phase III training_gesture_clapping_2nd.mp4'.format(p3_training_prefix),
  'p3_training_driveTraining_2':  '{}Phase III training_gesture_driving_2nd.mp4'.format(p3_training_prefix),
  'p3_training_eatTraining_2':  '{}Phase III training_gesture_eating_2nd.mp4'.format(p3_training_prefix),
  'p3_training_birdTraining_2':  '{}Phase III training_gesture_flying_2nd.mp4'.format(p3_training_prefix),
  'p3_training_goodbyeTraining_2':  '{}Phase III training_gesture_goodbye_2nd.mp4'.format(p3_training_prefix),
  'p3_training_helloTraining_2':  '{}Phase III training_gesture_handshake_2nd.mp4'.format(p3_training_prefix),
  'p3_training_hugTraining_2':  '{}Phase III training_gesture_hugging_2nd.mp4'.format(p3_training_prefix),
  'p3_training_hungryTraining_2':  '{}Phase III training_gesture_hungry_2nd.mp4'.format(p3_training_prefix),
  'p3_training_mineTraining_2':  '{}Phase III training_gesture_myself_2nd.mp4'.format(p3_training_prefix),
  'p3_training_notAllowedTraining_2':  '{}Phase III training_gesture_no_2nd.mp4'.format(p3_training_prefix),
  'p3_training_yesTraining_2':  '{}Phase III training_gesture_nodding_2nd.mp4'.format(p3_training_prefix),
  'p3_training_annoyedTraining_2':  '{}Phase III training_gesture_puzzled_2nd.mp4'.format(p3_training_prefix),
  'p3_training_babyTraining_2':  '{}Phase III training_gesture_rocking baby BB_2nd.mp4'.format(p3_training_prefix),
  'p3_training_comeTraining_2':  '{}Phase III training_gesture_show direction_2nd.mp4'.format(p3_training_prefix),
  'p3_training_waitTraining_2':  '{}Phase III training_gesture_wait long_2nd.mp4'.format(p3_training_prefix),
  'p3_training_walkTraining_2':  '{}Phase III training_gesture_walking_2nd.mp4'.format(p3_training_prefix),
  'p3_training_welcomeTraining_2':  '{}Phase III training_gesture_welcome_2nd.mp4'.format(p3_training_prefix),
  'p3_training_whereTraining_2':  '{}Phase III training_gesture_where_2nd.mp4'.format(p3_training_prefix),
  'p3_training_wrongTraining_2':  '{}Phase III training_gesture_wrong_2nd.mp4'.format(p3_training_prefix),

  # This is a longer response given when user makes a correct choice given during posttest
  'p3_feedback_correct':    '{}Phase III training _ assessment_gesture feedback_correct.mp4'.format(p3_feedback_prefix),

  # these are feedback videos if the incorrect gestures are made, the video demonstrates the correct gesture
  'p3_feedback_angryIncorrect':     '{}Phase III training _ assessment_gesture feedback_incorrect_angry.mp4'.format(p3_feedback_prefix),
  'p3_feedback_awesomeIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_clapping.mp4'.format(p3_feedback_prefix),
  'p3_feedback_driveIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_driving.mp4'.format(p3_feedback_prefix),
  'p3_feedback_eatIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_eating.mp4'.format(p3_feedback_prefix),
  'p3_feedback_birdIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_flying.mp4'.format(p3_feedback_prefix),
  'p3_feedback_goodbyeIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_goodbye.mp4'.format(p3_feedback_prefix),
  'p3_feedback_helloIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_handshake.mp4'.format(p3_feedback_prefix),
  'p3_feedback_hugIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_hugging.mp4'.format(p3_feedback_prefix),
  'p3_feedback_hungryIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_hungry.mp4'.format(p3_feedback_prefix),
  'p3_feedback_mineIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_myself.mp4'.format(p3_feedback_prefix),
  'p3_feedback_notAllowedIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_no.mp4'.format(p3_feedback_prefix),
  'p3_feedback_yesIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_nodding.mp4'.format(p3_feedback_prefix),
  'p3_feedback_annoyedIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_puzzled.mp4'.format(p3_feedback_prefix),
  'p3_feedback_babyIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_rocking baby BB.mp4'.format(p3_feedback_prefix),
  'p3_feedback_comeIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_show direction.mp4'.format(p3_feedback_prefix),
  'p3_feedback_waitIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_wait long.mp4'.format(p3_feedback_prefix),
  'p3_feedback_walkIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_walking.mp4'.format(p3_feedback_prefix),
  'p3_feedback_welcomeIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_welcome.mp4'.format(p3_feedback_prefix),
  'p3_feedback_whereIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_where.mp4'.format(p3_feedback_prefix),
  'p3_feedback_wrongIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_wrong.mp4'.format(p3_feedback_prefix),



  
}

for i in VIDEOS:
  VIDEOS[i] = VIDEOS[i].replace(' ', '_')
  
QUESTIONS = {
  'angry' : {'choices': ['hungry', 'angry', 'come']}, 
  'awesome': {'choices': ['goodbye','hug','awesome']}, 
  'drive': {'choices': ['mine','drive','yes']},
  'eat': {'choices': ['hello','notAllowed','eat']},
  'bird': {'choices': ['annoyed','bird','eat']},
  'goodbye': {'choices': ['goodbye','welcome','where']},
  'hello': {'choices': ['hungry','walk','hello']},
  'hug': {'choices': ['wrong','hug','annoyed']},
  'hungry': {'choices': ['hungry','walk','drive']},
  'mine': {'choices': ['mine','eat','where']},
  'notAllowed': {'choices': ['angry','notAllowed','come']},
  'yes': {'choices': ['hungry','awesome','yes']},
  'annoyed': {'choices': ['bird','annoyed','mine']},
  'baby': {'choices': ['baby','wait','angry']},
  'come': {'choices': ['mine','notAllowed','come']},
  'wait': {'choices': ['hungry','awesome','wait']},
  'walk': {'choices': ['walk','hug','annoyed']},
  'welcome': {'choices': ['hungry','angry','welcome']},
  'where': {'choices': ['mine','where','yes']},
  'wrong': {'choices': ['wrong','welcome','eat']},
}

# test videolinks for validity
# import requests
# def testLink(vidKeylink):
#   r = requests.get(vidKeylink[1])
#   return (r.status_code, vidKeylink[0])

# from multiprocessing import Pool
# p = Pool(40)

# all_responses = list(p.map(testLink, VIDEOS.items()))
# summary = {}
# for i in all_responses:
#   if i[0] not in summary:
#     summary[i[0]] = []
# summary[i[0]].append(i[1])

# print summary


START_DATE = '09/18/1986'

# 1 好嬲 肚餓       好嬲        過嚟

# 2 好嘢 拜拜       抱抱        好嘢 

# 3 揸車 自己       揸車        可以 

# 4 食嘢 你好       唔准        食嘢 

# 5 雀仔 好煩       雀仔        等等 

# 6 拜拜 拜拜       歡迎        邊度 

# 7 你好 肚餓       行路        你好 

# 8 抱抱 錯嘅       抱抱        好煩 

# 9 肚餓 肚餓       行路        揸車 

# 10 自己 自己       食嘢        邊度 

# 11 唔准 好嬲       唔准        過嚟 

# 12 可以 肚餓       好嘢        可以 

# 13 好煩 雀仔       好煩        自己 

# 14 BB BB         等等        好嬲 

# 15 過嚟 自己       唔准        過嚟 

# 16 等等 肚餓       好嘢        等等 

# 17 行路 行路       抱抱        好煩 

# 18 歡迎 肚餓       好嬲        歡迎 

# 19 邊度 自己       邊度        可以

# 20 錯嘅 錯嘅       歡迎        食嘢








    