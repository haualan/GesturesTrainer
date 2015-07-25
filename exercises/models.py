#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=100, blank=True, default='')
  code = models.TextField()
  linenos = models.BooleanField(default=False)
  language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
  style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
  owner = models.ForeignKey('auth.User', related_name='snippets')
  highlighted = models.TextField()

  def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = self.linenos and 'table' or False
    options = self.title and {'title': self.title} or {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Snippet, self).save(*args, **kwargs)

  class Meta:
      ordering = ('created',)


phase_choices = (
      ('phase1', 'Phase I'),
      ('phase2', 'Phase II'),
      ('phase3', 'Phase III'),
  )
section_choices = (
      ('pretest', 'Pre-test'),
      ('training', 'Training'),
      ('posttest1', 'Post-Test I'),
      ('posttest2', 'Post-Test II'),
      ('posttest3', 'Post-Test III'),
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
  created = models.DateTimeField(auto_now_add = True)
  owner = models.ForeignKey('auth.User')
  phase = models.CharField(max_length= 100, choices = phase_choices)
  # phase = models.ForeignKey('Phase', related_name='ExerciseResults')
  section = models.CharField(max_length= 100, choices = section_choices)
  # section = models.ForeignKey('Section', related_name='ExerciseResults')
  # # cycle describes how many times the section has been performed on user
  # cycle = models.IntegerField()
  gestureTested = models.CharField(max_length = 100)
  response = models.CharField(max_length = 100, choices = response_choices )

# https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase1/assessment/Phase+I+assessment_gesture+instruction+1.mp4

# p1_assessment_prefix = '/media/phase1/assessment/'
# p1_feedback_prefix = '/media/phase1/feedback/'
# p1_training_prefix = '/media/phase1/training/'

# p2_assessment_prefix = '/media/phase2/assessment/'
# p2_feedback_prefix = '/media/phase2/feedback/'
# p2_training_prefix = '/media/phase2/training/'

# p3_assessment_prefix = '/media/phase3/assessment/'
# p3_feedback_prefix = '/media/phase3/feedback/'
# p3_training_prefix = '/media/phase3/training/'

p1_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase1/assessment/'
p1_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase1/feedback/'
p1_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase1/training/'

p2_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase2/assessment/'
p2_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase2/feedback/'
p2_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase2/training/'

p3_assessment_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase3/assessment/'
p3_feedback_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase3/feedback/'
p3_training_prefix = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/phase3/training/'


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
  'p1_assessment_angryGesture' :  '{}Phase I assessment_gesture instruction 2_angry 好嬲.mp4'.format(p1_assessment_prefix),
  'p1_assessment_awesomeGesture':  '{}Phase I assessment_gesture instruction 2_clapping 好嘢.mp4'.format(p1_assessment_prefix),
  'p1_assessment_driveGesture':  '{}Phase I assessment_gesture instruction 2_driving 揸車.mp4'.format(p1_assessment_prefix),
  'p1_assessment_eatGesture':  '{}Phase I assessment_gesture instruction 2_eating3 食嘢.mp4'.format(p1_assessment_prefix),
  'p1_assessment_birdGesture':  '{}Phase I assessment_gesture instruction 2_flying 雀仔.mp4'.format(p1_assessment_prefix),
  'p1_assessment_goodbyeGesture':  '{}Phase I assessment_gesture instruction 2_goodbye 拜拜.mp4'.format(p1_assessment_prefix),
  'p1_assessment_helloGesture':  '{}Phase I assessment_gesture instruction 2_handshake3 你好.mp4'.format(p1_assessment_prefix),
  'p1_assessment_hugGesture':  '{}Phase I assessment_gesture instruction 2_hugging 抱抱.mp4'.format(p1_assessment_prefix),
  'p1_assessment_hungryGesture':  '{}Phase I assessment_gesture instruction 2_hungry 肚餓.mp4'.format(p1_assessment_prefix),
  'p1_assessment_mineGesture':  '{}Phase I assessment_gesture instruction 2_myself 自己.mp4'.format(p1_assessment_prefix),
  'p1_assessment_notAllowedGesture':  '{}Phase I assessment_gesture instruction 2_no2 唔准.mp4'.format(p1_assessment_prefix),
  'p1_assessment_yesGesture':  '{}Phase I assessment_gesture instruction 2_nodding 可以.mp4'.format(p1_assessment_prefix),
  'p1_assessment_annoyedGesture':  '{}Phase I assessment_gesture instruction 2_puzzled 好煩.mp4'.format(p1_assessment_prefix),
  'p1_assessment_babyGesture':  '{}Phase I assessment_gesture instruction 2_rocking baby BB.mp4'.format(p1_assessment_prefix),
  'p1_assessment_comeGesture':  '{}Phase I assessment_gesture instruction 2_show direction 過嚟.mp4'.format(p1_assessment_prefix),
  'p1_assessment_waitGesture':  '{}Phase I assessment_gesture instruction 2_wait long 等等.mp4'.format(p1_assessment_prefix),
  'p1_assessment_walkGesture':  '{}Phase I assessment_gesture instruction 2_walking5 行路.mp4'.format(p1_assessment_prefix),
  'p1_assessment_welcomeGesture':  '{}Phase I assessment_gesture instruction 2_welcome 歡迎.mp4'.format(p1_assessment_prefix),
  'p1_assessment_whereGesture':  '{}Phase I assessment_gesture instruction 2_where2 邊度.mp4'.format(p1_assessment_prefix),
  'p1_assessment_wrongGesture':  '{}Phase I assessment_gesture instruction 2_wrong4 錯嘅.mp4'.format(p1_assessment_prefix),

  # video that plays after the gesture is demonstrated, but stages for the choices coming ahead:
  # 你覺得佢嘅意思係
  'p1_assessment_instructionPostGesture':   '{}Phase I assessment_gesture instruction 3.mp4'.format(p1_assessment_prefix),



  # video with speech only, spoken without gestures just to list out the available choices
  'p1_assessment_angryChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_angry 好嬲.mp4'.format(p1_assessment_prefix),
  'p1_assessment_awesomeChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_clapping 好嘢.mp4'.format(p1_assessment_prefix),
  'p1_assessment_driveChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_driving 揸車.mp4'.format(p1_assessment_prefix),
  'p1_assessment_eatChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_eating3 食嘢.mp4'.format(p1_assessment_prefix),
  'p1_assessment_birdChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_flying 雀仔.mp4'.format(p1_assessment_prefix),
  'p1_assessment_goodbyeChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_goodbye 拜拜.mp4'.format(p1_assessment_prefix),
  'p1_assessment_helloChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_handshake3 你好.mp4'.format(p1_assessment_prefix),
  'p1_assessment_hugChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_hugging 抱抱.mp4'.format(p1_assessment_prefix),
  'p1_assessment_hungryChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_hungry 肚餓.mp4'.format(p1_assessment_prefix),
  'p1_assessment_mineChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_myself 自己.mp4'.format(p1_assessment_prefix),
  'p1_assessment_notAllowedChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_no2 唔准.mp4'.format(p1_assessment_prefix),
  'p1_assessment_yesChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_nodding 可以.mp4'.format(p1_assessment_prefix),
  'p1_assessment_annoyedChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_puzzled 好煩.mp4'.format(p1_assessment_prefix),
  'p1_assessment_babyChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_rocking baby BB.mp4'.format(p1_assessment_prefix),
  'p1_assessment_comeChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_show direction 過嚟.mp4'.format(p1_assessment_prefix),
  'p1_assessment_waitChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_wait long 等等.mp4'.format(p1_assessment_prefix),
  'p1_assessment_walkChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_walking5 行路.mp4'.format(p1_assessment_prefix),
  'p1_assessment_welcomeChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_welcome 歡迎.mp4'.format(p1_assessment_prefix),
  'p1_assessment_whereChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_where2 邊度.mp4'.format(p1_assessment_prefix),
  'p1_assessment_wrongChoice':  '{}Phase I assessment_gesture instruction 3_ans choice_wrong4 錯嘅.mp4'.format(p1_assessment_prefix),

  # video with speech only to prompt user to make a choice
  # 請你將你覺得啱嘅答案講出嚟或者指比老師睇。(all three answers are staying on the screen)
  'p1_assessment_makeAChoiceNow':   '{}Phase I assessment_gesture instruction 4.mp4'.format(p1_assessment_prefix),

  # Thank you video for any repsonse chosen during pretest, this is a short thankyou Response
  'p1_feedback_thankyou':   '{}Phase I assessment_gesture feedback_thank you.mp4'.format(p1_feedback_prefix),

  # This is a longer response given when user makes a correct choice given during posttest
  'p1_feedback_correct':    '{}Phase I assessment_gesture feedback_correct.mp4'.format(p1_feedback_prefix),

  # these are feedback videos if the incorrect gestures are made, the video demonstrates the correct gesture
  'p1_feedback_angryIncorrect':     '{}Phase I assessment_gesture feedback_incorrect_angry 好嬲.mp4'.format(p1_feedback_prefix),
  'p1_feedback_awesomeIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_clapping 好嘢.mp4'.format(p1_feedback_prefix),
  'p1_feedback_driveIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_driving 揸車.mp4'.format(p1_feedback_prefix),
  'p1_feedback_eatIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_eating3 食嘢.mp4'.format(p1_feedback_prefix),
  'p1_feedback_birdIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_flying 雀仔.mp4'.format(p1_feedback_prefix),
  'p1_feedback_goodbyeIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_goodbye 拜拜.mp4'.format(p1_feedback_prefix),
  'p1_feedback_helloIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_handshake3 你好.mp4'.format(p1_feedback_prefix),
  'p1_feedback_hugIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_hugging 抱抱.mp4'.format(p1_feedback_prefix),
  'p1_feedback_hungryIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_hungry 肚餓.mp4'.format(p1_feedback_prefix),
  'p1_feedback_mineIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_myself 自己.mp4'.format(p1_feedback_prefix),
  'p1_feedback_notAllowedIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_no2 唔准.mp4'.format(p1_feedback_prefix),
  'p1_feedback_yesIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_nodding 可以.mp4'.format(p1_feedback_prefix),
  'p1_feedback_annoyedIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_puzzled 好煩.mp4'.format(p1_feedback_prefix),
  'p1_feedback_babyIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_rocking baby BB.mp4'.format(p1_feedback_prefix),
  'p1_feedback_comeIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_show direction 過嚟.mp4'.format(p1_feedback_prefix),
  'p1_feedback_waitIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_wait long 等等.mp4'.format(p1_feedback_prefix),
  'p1_feedback_walkIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_walking5 行路.mp4'.format(p1_feedback_prefix),
  'p1_feedback_welcomeIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_welcome 歡迎.mp4'.format(p1_feedback_prefix),
  'p1_feedback_whereIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_where2 邊度.mp4'.format(p1_feedback_prefix),
  'p1_feedback_wrongIncorrect':  '{}Phase I assessment_gesture feedback_incorrect_wrong4 錯嘅.mp4'.format(p1_feedback_prefix),

  # greeting and instructions for the training section
  'p1_training_greetingAndInstruction': '{}Phase I training_greeting and instruction.mp4'.format(p1_training_prefix),

  # video that asks if user understands the instructions, specifcally for the training section
  'p1_training_doYouUnderstand': '{}do you understand.mp4'.format(p1_training_prefix),

  # these training videos demonstrate the gestures to the user, no response is expected from the user on the training sections
  'p1_training_angryTraining':     '{}Phase I training_gesture_angry 好嬲_combined.mp4'.format(p1_training_prefix),
  'p1_training_awesomeTraining':  '{}Phase I training_gesture_clapping 好嘢_combined.mp4'.format(p1_training_prefix),
  'p1_training_driveTraining':  '{}Phase I training_gesture_driving 揸車_combined.mp4'.format(p1_training_prefix),
  'p1_training_eatTraining':  '{}Phase I training_gesture_eating3 食嘢_combined.mp4'.format(p1_training_prefix),
  'p1_training_birdTraining':  '{}Phase I training_gesture_flying 雀仔_combined.mp4'.format(p1_training_prefix),
  'p1_training_goodbyeTraining':  '{}Phase I training_gesture_goodbye 拜拜_combined.mp4'.format(p1_training_prefix),
  'p1_training_helloTraining':  '{}Phase I training_gesture_handshake3 你好_combined.mp4'.format(p1_training_prefix),
  'p1_training_hugTraining':  '{}Phase I training_gesture_hugging 抱抱_combined.mp4'.format(p1_training_prefix),
  'p1_training_hungryTraining':  '{}Phase I training_gesture_hungry 肚餓_combined.mp4'.format(p1_training_prefix),
  'p1_training_mineTraining':  '{}Phase I training_gesture_myself 自己_combined.mp4'.format(p1_training_prefix),
  'p1_training_notAllowedTraining':  '{}Phase I training_gesture_no2 唔准_combined.mp4'.format(p1_training_prefix),
  'p1_training_yesTraining':  '{}Phase I training_gesture_nodding 可以_combined.mp4'.format(p1_training_prefix),
  'p1_training_annoyedTraining':  '{}Phase I training_gesture_puzzled 好煩_combined.mp4'.format(p1_training_prefix),
  'p1_training_babyTraining':  '{}Phase I training_gesture_rocking baby BB_combined.mp4'.format(p1_training_prefix),
  'p1_training_comeTraining':  '{}Phase I training_gesture_show direction 過嚟_combined.mp4'.format(p1_training_prefix),
  'p1_training_waitTraining':  '{}Phase I training_gesture_wait long 等等_combined.mp4'.format(p1_training_prefix),
  'p1_training_walkTraining':  '{}Phase I training_gesture_walking5 行路_combined.mp4'.format(p1_training_prefix),
  'p1_training_welcomeTraining':  '{}Phase I training_gesture_welcome 歡迎_combined.mp4'.format(p1_training_prefix),
  'p1_training_whereTraining':  '{}Phase I training_gesture_where2 邊度_combined.mp4'.format(p1_training_prefix),
  'p1_training_wrongTraining':  '{}Phase I training_gesture_wrong4 錯嘅_combined.mp4'.format(p1_training_prefix),

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
  'p2_assessment_angryGesture' :  '{}Phase II assessment_gesture instruction 2_angry 好嬲.mp4'.format(p2_assessment_prefix),
  'p2_assessment_awesomeGesture':  '{}Phase II assessment_gesture instruction 2_clapping 好嘢.mp4'.format(p2_assessment_prefix),
  'p2_assessment_driveGesture':  '{}Phase II assessment_gesture instruction 2_driving 揸車.mp4'.format(p2_assessment_prefix),
  'p2_assessment_eatGesture':  '{}Phase II assessment_gesture instruction 2_eating3 食嘢.mp4'.format(p2_assessment_prefix),
  'p2_assessment_birdGesture':  '{}Phase II assessment_gesture instruction 2_flying 雀仔.mp4'.format(p2_assessment_prefix),
  'p2_assessment_goodbyeGesture':  '{}Phase II assessment_gesture instruction 2_goodbye 拜拜.mp4'.format(p2_assessment_prefix),
  'p2_assessment_helloGesture':  '{}Phase II assessment_gesture instruction 2_handshake3 你好.mp4'.format(p2_assessment_prefix),
  'p2_assessment_hugGesture':  '{}Phase II assessment_gesture instruction 2_hugging 抱抱.mp4'.format(p2_assessment_prefix),
  'p2_assessment_hungryGesture':  '{}Phase II assessment_gesture instruction 2_hungry 肚餓.mp4'.format(p2_assessment_prefix),
  'p2_assessment_mineGesture':  '{}Phase II assessment_gesture instruction 2_myself 自己.mp4'.format(p2_assessment_prefix),
  'p2_assessment_notAllowedGesture':  '{}Phase II assessment_gesture instruction 2_no2 唔准.mp4'.format(p2_assessment_prefix),
  'p2_assessment_yesGesture':  '{}Phase II assessment_gesture instruction 2_nodding 可以.mp4'.format(p2_assessment_prefix),
  'p2_assessment_annoyedGesture':  '{}Phase II assessment_gesture instruction 2_puzzled 好煩.mp4'.format(p2_assessment_prefix),
  'p2_assessment_babyGesture':  '{}Phase II assessment_gesture instruction 2_rocking baby BB.mp4'.format(p2_assessment_prefix),
  'p2_assessment_comeGesture':  '{}Phase II assessment_gesture instruction 2_show direction 過嚟.mp4'.format(p2_assessment_prefix),
  'p2_assessment_waitGesture':  '{}Phase II assessment_gesture instruction 2_wait long 等等.mp4'.format(p2_assessment_prefix),
  'p2_assessment_walkGesture':  '{}Phase II assessment_gesture instruction 2_walking5 行路.mp4'.format(p2_assessment_prefix),
  'p2_assessment_welcomeGesture':  '{}Phase II assessment_gesture instruction 2_welcome 歡迎.mp4'.format(p2_assessment_prefix),
  'p2_assessment_whereGesture':  '{}Phase II assessment_gesture instruction 2_where2 邊度.mp4'.format(p2_assessment_prefix),
  'p2_assessment_wrongGesture':  '{}Phase II assessment_gesture instruction 2_wrong4 錯嘅.mp4'.format(p2_assessment_prefix),

  # Thank you video for any repsonse chosen during pretest, this is a short thankyou Response
  'p2_feedback_thankyou':   '{}Phase II assessment_gesture feedback_thank you (pretest).mp4'.format(p2_feedback_prefix),

  # greeting and instructions for the training section
  'p2_training_greetingAndInstruction': '{}Phase II training_greeting and instruction.mp4'.format(p2_training_prefix),

  # video that asks if user understands the instructions, specifcally for the training section
  'p2_training_doYouUnderstand': '{}do you understand.mp4'.format(p2_training_prefix),

  # these training videos demonstrate the gestures to the user, no response is expected from the user on the training sections
  'p2_training_angryTraining_1':     '{}Phase II training_gesture_angry 好嬲_1st.mp4'.format(p2_training_prefix),
  'p2_training_awesomeTraining_1':  '{}Phase II training_gesture_clapping 好嘢_1st.mp4'.format(p2_training_prefix),
  'p2_training_driveTraining_1':  '{}Phase II training_gesture_driving 揸車_1st.mp4'.format(p2_training_prefix),
  'p2_training_eatTraining_1':  '{}Phase II training_gesture_eating3 食嘢_1st.mp4'.format(p2_training_prefix),
  'p2_training_birdTraining_1':  '{}Phase II training_gesture_flying 雀仔_1st.mp4'.format(p2_training_prefix),
  'p2_training_goodbyeTraining_1':  '{}Phase II training_gesture_goodbye 拜拜_1st.mp4'.format(p2_training_prefix),
  'p2_training_helloTraining_1':  '{}Phase II training_gesture_handshake3 你好_1st.mp4'.format(p2_training_prefix),
  'p2_training_hugTraining_1':  '{}Phase II training_gesture_hugging 抱抱_1st.mp4'.format(p2_training_prefix),
  'p2_training_hungryTraining_1':  '{}Phase II training_gesture_hungry 肚餓_1st.mp4'.format(p2_training_prefix),
  'p2_training_mineTraining_1':  '{}Phase II training_gesture_myself 自己_1st.mp4'.format(p2_training_prefix),
  'p2_training_notAllowedTraining_1':  '{}Phase II training_gesture_no2 唔准_1st.mp4'.format(p2_training_prefix),
  'p2_training_yesTraining_1':  '{}Phase II training_gesture_nodding 可以_1st.mp4'.format(p2_training_prefix),
  'p2_training_annoyedTraining_1':  '{}Phase II training_gesture_puzzled 好煩_1st.mp4'.format(p2_training_prefix),
  'p2_training_babyTraining_1':  '{}Phase II training_gesture_rocking baby BB_1st.mp4'.format(p2_training_prefix),
  'p2_training_comeTraining_1':  '{}Phase II training_gesture_show direction 過嚟_1st.mp4'.format(p2_training_prefix),
  'p2_training_waitTraining_1':  '{}Phase II training_gesture_wait long 等等_1st.mp4'.format(p2_training_prefix),
  'p2_training_walkTraining_1':  '{}Phase II training_gesture_walking5 行路_1st.mp4'.format(p2_training_prefix),
  'p2_training_welcomeTraining_1':  '{}Phase II training_gesture_welcome 歡迎_1st.mp4'.format(p2_training_prefix),
  'p2_training_whereTraining_1':  '{}Phase II training_gesture_where2 邊度_1st.mp4'.format(p2_training_prefix),
  'p2_training_wrongTraining_1':  '{}Phase II training_gesture_wrong4 錯嘅_1st.mp4'.format(p2_training_prefix),

  'p2_training_angryTraining_2':     '{}Phase II training_gesture_angry 好嬲_2nd.mp4'.format(p2_training_prefix),
  'p2_training_awesomeTraining_2':  '{}Phase II training_gesture_clapping 好嘢_2nd.mp4'.format(p2_training_prefix),
  'p2_training_driveTraining_2':  '{}Phase II training_gesture_driving 揸車_2nd.mp4'.format(p2_training_prefix),
  'p2_training_eatTraining_2':  '{}Phase II training_gesture_eating3 食嘢_2nd.mp4'.format(p2_training_prefix),
  'p2_training_birdTraining_2':  '{}Phase II training_gesture_flying 雀仔_2nd.mp4'.format(p2_training_prefix),
  'p2_training_goodbyeTraining_2':  '{}Phase II training_gesture_goodbye 拜拜_2nd.mp4'.format(p2_training_prefix),
  'p2_training_helloTraining_2':  '{}Phase II training_gesture_handshake3 你好_2nd.mp4'.format(p2_training_prefix),
  'p2_training_hugTraining_2':  '{}Phase II training_gesture_hugging 抱抱_2nd.mp4'.format(p2_training_prefix),
  'p2_training_hungryTraining_2':  '{}Phase II training_gesture_hungry 肚餓_2nd.mp4'.format(p2_training_prefix),
  'p2_training_mineTraining_2':  '{}Phase II training_gesture_myself 自己_2nd.mp4'.format(p2_training_prefix),
  'p2_training_notAllowedTraining_2':  '{}Phase II training_gesture_no2 唔准_2nd.mp4'.format(p2_training_prefix),
  'p2_training_yesTraining_2':  '{}Phase II training_gesture_nodding 可以_2nd.mp4'.format(p2_training_prefix),
  'p2_training_annoyedTraining_2':  '{}Phase II training_gesture_puzzled 好煩_2nd.mp4'.format(p2_training_prefix),
  'p2_training_babyTraining_2':  '{}Phase II training_gesture_rocking baby BB_2nd.mp4'.format(p2_training_prefix),
  'p2_training_comeTraining_2':  '{}Phase II training_gesture_show direction 過嚟_2nd.mp4'.format(p2_training_prefix),
  'p2_training_waitTraining_2':  '{}Phase II training_gesture_wait long 等等_2nd.mp4'.format(p2_training_prefix),
  'p2_training_walkTraining_2':  '{}Phase II training_gesture_walking5 行路_2nd.mp4'.format(p2_training_prefix),
  'p2_training_welcomeTraining_2':  '{}Phase II training_gesture_welcome 歡迎_2nd.mp4'.format(p2_training_prefix),
  'p2_training_whereTraining_2':  '{}Phase II training_gesture_where2 邊度_2nd.mp4'.format(p2_training_prefix),
  'p2_training_wrongTraining_2':  '{}Phase II training_gesture_wrong4 錯嘅_2nd.mp4'.format(p2_training_prefix),

  # This is a longer response given when user makes a correct choice given during posttest
  'p2_feedback_correct':    '{}Phase II training _ assessment_gesture feedback_correct.mp4'.format(p2_feedback_prefix),

  # these are feedback videos if the incorrect gestures are made, the video demonstrates the correct gesture
  'p2_feedback_angryIncorrect':     '{}Phase II training _ assessment_gesture feedback_incorrect_angry 好嬲.mp4'.format(p2_feedback_prefix),
  'p2_feedback_awesomeIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_clapping 好嘢.mp4'.format(p2_feedback_prefix),
  'p2_feedback_driveIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_driving 揸車.mp4'.format(p2_feedback_prefix),
  'p2_feedback_eatIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_eating3 食嘢.mp4'.format(p2_feedback_prefix),
  'p2_feedback_birdIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_flying 雀仔.mp4'.format(p2_feedback_prefix),
  'p2_feedback_goodbyeIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_goodbye 拜拜.mp4'.format(p2_feedback_prefix),
  'p2_feedback_helloIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_handshake3 你好.mp4'.format(p2_feedback_prefix),
  'p2_feedback_hugIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_hugging 抱抱.mp4'.format(p2_feedback_prefix),
  'p2_feedback_hungryIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_hungry 肚餓.mp4'.format(p2_feedback_prefix),
  'p2_feedback_mineIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_myself 自己.mp4'.format(p2_feedback_prefix),
  'p2_feedback_notAllowedIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_no2 唔准.mp4'.format(p2_feedback_prefix),
  'p2_feedback_yesIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_nodding 可以.mp4'.format(p2_feedback_prefix),
  'p2_feedback_annoyedIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_puzzled 好煩.mp4'.format(p2_feedback_prefix),
  'p2_feedback_babyIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_rocking baby BB.mp4'.format(p2_feedback_prefix),
  'p2_feedback_comeIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_show direction 過嚟.mp4'.format(p2_feedback_prefix),
  'p2_feedback_waitIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_wait long 等等.mp4'.format(p2_feedback_prefix),
  'p2_feedback_walkIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_walking5 行路.mp4'.format(p2_feedback_prefix),
  'p2_feedback_welcomeIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_welcome 歡迎.mp4'.format(p2_feedback_prefix),
  'p2_feedback_whereIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_where2 邊度.mp4'.format(p2_feedback_prefix),
  'p2_feedback_wrongIncorrect':  '{}Phase II training _ assessment_gesture feedback_incorrect_wrong4 錯嘅.mp4'.format(p2_feedback_prefix),

  # video played at beginning of the assessment / pretest / posttest, general greetings and instructions
  #   "I am going to ask you what gestures should be produced in certain circumstances"
  # 跟住落嚟我想請問你，喺以下嘅故事裏面，應該做D咩手勢。
  'p3_assessment_greetingAndInstruction': '{}Phase III assessment_greeting and instruction.mp4'.format(p3_assessment_prefix),

  # video that asks if user understands the instructions
  'p3_assessment_doYouUnderstand': '{}do you understand (new nao).mp4'.format(p3_assessment_prefix),

  # video demontrating the gestures and asking what does user think it means:
  'p3_assessment_pretest_angryGesture' :  '{}Phase III assessment_pretest_angry 好嬲.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_awesomeGesture':  '{}Phase III assessment_pretest_clapping 好嘢.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_driveGesture':  '{}Phase III assessment_pretest_driving 揸車.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_eatGesture':  '{}Phase III assessment_pretest_eating 食嘢.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_birdGesture':  '{}Phase III assessment_pretest_flying 雀仔.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_goodbyeGesture':  '{}Phase III assessment_pretest_goodbye 拜拜.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_helloGesture':  '{}Phase III assessment_pretest_handshake 你好.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_hugGesture':  '{}Phase III assessment_pretest_hugging 抱抱.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_hungryGesture':  '{}Phase III assessment_pretest_hungry 肚餓.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_mineGesture':  '{}Phase III assessment_pretest_myself 自己.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_notAllowedGesture':  '{}Phase III assessment_pretest_no 唔准.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_yesGesture':  '{}Phase III assessment_pretest_nodding 可以.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_annoyedGesture':  '{}Phase III assessment_pretest_puzzled 好煩.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_babyGesture':  '{}Phase III assessment_pretest_rocking baby BB.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_comeGesture':  '{}Phase III assessment_pretest_show direction 過嚟.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_waitGesture':  '{}Phase III assessment_pretest_wait long 等等.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_walkGesture':  '{}Phase III assessment_pretest_walking 行路.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_welcomeGesture':  '{}Phase III assessment_pretest_welcome 歡迎.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_whereGesture':  '{}Phase III assessment_pretest_where 邊度.mp4'.format(p3_assessment_prefix),
  'p3_assessment_pretest_wrongGesture':  '{}Phase III assessment_pretest_wrong 錯嘅.mp4'.format(p3_assessment_prefix),

  'p3_assessment_posttest1_angryGesture' :  '{}Phase III assessment_posttest 1_angry 好嬲.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_awesomeGesture':  '{}Phase III assessment_posttest 1_clapping 好嘢.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_driveGesture':  '{}Phase III assessment_posttest 1_driving 揸車.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_eatGesture':  '{}Phase III assessment_posttest 1_eating 食嘢.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_birdGesture':  '{}Phase III assessment_posttest 1_flying 雀仔.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_goodbyeGesture':  '{}Phase III assessment_posttest 1_goodbye 拜拜.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_helloGesture':  '{}Phase III assessment_posttest 1_handshake 你好.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_hugGesture':  '{}Phase III assessment_posttest 1_hugging 抱抱.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_hungryGesture':  '{}Phase III assessment_posttest 1_hungry 肚餓.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_mineGesture':  '{}Phase III assessment_posttest 1_myself 自己.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_notAllowedGesture':  '{}Phase III assessment_posttest 1_no 唔准.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_yesGesture':  '{}Phase III assessment_posttest 1_nodding 可以.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_annoyedGesture':  '{}Phase III assessment_posttest 1_puzzled 好煩.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_babyGesture':  '{}Phase III assessment_posttest 1_rocking baby BB.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_comeGesture':  '{}Phase III assessment_posttest 1_show direction 過嚟.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_waitGesture':  '{}Phase III assessment_posttest 1_wait long 等等.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_walkGesture':  '{}Phase III assessment_posttest 1_walking 行路.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_welcomeGesture':  '{}Phase III assessment_posttest 1_welcome 歡迎.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_whereGesture':  '{}Phase III assessment_posttest 1_where 邊度.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest1_wrongGesture':  '{}Phase III assessment_posttest 1_wrong 錯嘅.mp4'.format(p3_assessment_prefix),

  'p3_assessment_posttest2_angryGesture' :  '{}Phase III assessment_posttest 2_angry 好嬲.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_awesomeGesture':  '{}Phase III assessment_posttest 2_clapping 好嘢.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_driveGesture':  '{}Phase III assessment_posttest 2_driving 揸車.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_eatGesture':  '{}Phase III assessment_posttest 2_eating 食嘢.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_birdGesture':  '{}Phase III assessment_posttest 2_flying 雀仔.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_goodbyeGesture':  '{}Phase III assessment_posttest 2_goodbye 拜拜.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_helloGesture':  '{}Phase III assessment_posttest 2_handshake 你好.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_hugGesture':  '{}Phase III assessment_posttest 2_hugging 抱抱.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_hungryGesture':  '{}Phase III assessment_posttest 2_hungry 肚餓.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_mineGesture':  '{}Phase III assessment_posttest 2_myself 自己.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_notAllowedGesture':  '{}Phase III assessment_posttest 2_no 唔准.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_yesGesture':  '{}Phase III assessment_posttest 2_nodding 可以.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_annoyedGesture':  '{}Phase III assessment_posttest 2_puzzled 好煩.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_babyGesture':  '{}Phase III assessment_posttest 2_rocking baby BB.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_comeGesture':  '{}Phase III assessment_posttest 2_show direction 過嚟.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_waitGesture':  '{}Phase III assessment_posttest 2_wait long 等等.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_walkGesture':  '{}Phase III assessment_posttest 2_walking 行路.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_welcomeGesture':  '{}Phase III assessment_posttest 2_welcome 歡迎.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_whereGesture':  '{}Phase III assessment_posttest 2_where 邊度.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest2_wrongGesture':  '{}Phase III assessment_posttest 2_wrong 錯嘅.mp4'.format(p3_assessment_prefix),

  'p3_assessment_posttest3_angryGesture' :  '{}Phase III assessment_posttest 3_angry 好嬲.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_awesomeGesture':  '{}Phase III assessment_posttest 3_clapping 好嘢.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_driveGesture':  '{}Phase III assessment_posttest 3_driving 揸車.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_eatGesture':  '{}Phase III assessment_posttest 3_eating 食嘢.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_birdGesture':  '{}Phase III assessment_posttest 3_flying 雀仔.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_goodbyeGesture':  '{}Phase III assessment_posttest 3_goodbye 拜拜.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_helloGesture':  '{}Phase III assessment_posttest 3_handshake 你好.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_hugGesture':  '{}Phase III assessment_posttest 3_hugging 抱抱.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_hungryGesture':  '{}Phase III assessment_posttest 3_hungry 肚餓.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_mineGesture':  '{}Phase III assessment_posttest 3_myself 自己.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_notAllowedGesture':  '{}Phase III assessment_posttest 3_no 唔准.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_yesGesture':  '{}Phase III assessment_posttest 3_nodding 可以.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_annoyedGesture':  '{}Phase III assessment_posttest 3_puzzled 好煩.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_babyGesture':  '{}Phase III assessment_posttest 3_rocking baby BB.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_comeGesture':  '{}Phase III assessment_posttest 3_show direction 過嚟.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_waitGesture':  '{}Phase III assessment_posttest 3_wait long 等等.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_walkGesture':  '{}Phase III assessment_posttest 3_walking 行路.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_welcomeGesture':  '{}Phase III assessment_posttest 3_welcome 歡迎.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_whereGesture':  '{}Phase III assessment_posttest 3_where 邊度.mp4'.format(p3_assessment_prefix),
  'p3_assessment_posttest3_wrongGesture':  '{}Phase III assessment_posttest _wrong 錯嘅.mp4'.format(p3_assessment_prefix),



  # Thank you video for any repsonse chosen during pretest, this is a short thankyou Response
  'p3_feedback_thankyou':   '{}Phase III training _ assessment_gesture feedback_thank you (pretest).mp4'.format(p3_feedback_prefix),

  # greeting and instructions for the training section
  'p3_training_greetingAndInstruction': '{}Phase III training_greeting and instruction.mp4'.format(p3_training_prefix),

  # video that asks if user understands the instructions, specifcally for the training section
  'p3_training_doYouUnderstand': '{}do you understand (new nao).mp4'.format(p3_training_prefix),

  # these training videos demonstrate the gestures to the user, no response is expected from the user on the training sections
  'p3_training_angryTraining_1':     '{}Phase III training_gesture_angry 好嬲_1st.mp4'.format(p3_training_prefix),
  'p3_training_awesomeTraining_1':  '{}Phase III training_gesture_clapping 好嘢_1st.mp4'.format(p3_training_prefix),
  'p3_training_driveTraining_1':  '{}Phase III training_gesture_driving 揸車_1st.mp4'.format(p3_training_prefix),
  'p3_training_eatTraining_1':  '{}Phase III training_gesture_eating 食嘢_1st.mp4'.format(p3_training_prefix),
  'p3_training_birdTraining_1':  '{}Phase III training_gesture_flying 雀仔_1st.mp4'.format(p3_training_prefix),
  'p3_training_goodbyeTraining_1':  '{}Phase III training_gesture_goodbye 拜拜_1st.mp4'.format(p3_training_prefix),
  'p3_training_helloTraining_1':  '{}Phase III training_gesture_handshake 你好_1st.mp4'.format(p3_training_prefix),
  'p3_training_hugTraining_1':  '{}Phase III training_gesture_hugging 抱抱_1st.mp4'.format(p3_training_prefix),
  'p3_training_hungryTraining_1':  '{}Phase III training_gesture_hungry 肚餓_1st.mp4'.format(p3_training_prefix),
  'p3_training_mineTraining_1':  '{}Phase III training_gesture_myself 自己_1st.mp4'.format(p3_training_prefix),
  'p3_training_notAllowedTraining_1':  '{}Phase III training_gesture_no 唔准_1st.mp4'.format(p3_training_prefix),
  'p3_training_yesTraining_1':  '{}Phase III training_gesture_nodding 可以_1st.mp4'.format(p3_training_prefix),
  'p3_training_annoyedTraining_1':  '{}Phase III training_gesture_puzzled 好煩_1st.mp4'.format(p3_training_prefix),
  'p3_training_babyTraining_1':  '{}Phase III training_gesture_rocking baby BB_1st.mp4'.format(p3_training_prefix),
  'p3_training_comeTraining_1':  '{}Phase III training_gesture_show direction 過嚟_1st.mp4'.format(p3_training_prefix),
  'p3_training_waitTraining_1':  '{}Phase III training_gesture_wait long 等等_1st.mp4'.format(p3_training_prefix),
  'p3_training_walkTraining_1':  '{}Phase III training_gesture_walking 行路_1st.mp4'.format(p3_training_prefix),
  'p3_training_welcomeTraining_1':  '{}Phase III training_gesture_welcome 歡迎_1st.mp4'.format(p3_training_prefix),
  'p3_training_whereTraining_1':  '{}Phase III training_gesture_where 邊度_1st.mp4'.format(p3_training_prefix),
  'p3_training_wrongTraining_1':  '{}Phase III training_gesture_wrong 錯嘅_1st.mp4'.format(p3_training_prefix),

  'p3_training_angryTraining_2':     '{}Phase III training_gesture_angry 好嬲_2nd.mp4'.format(p3_training_prefix),
  'p3_training_awesomeTraining_2':  '{}Phase III training_gesture_clapping 好嘢_2nd.mp4'.format(p3_training_prefix),
  'p3_training_driveTraining_2':  '{}Phase III training_gesture_driving 揸車_2nd.mp4'.format(p3_training_prefix),
  'p3_training_eatTraining_2':  '{}Phase III training_gesture_eating 食嘢_2nd.mp4'.format(p3_training_prefix),
  'p3_training_birdTraining_2':  '{}Phase III training_gesture_flying 雀仔_2nd.mp4'.format(p3_training_prefix),
  'p3_training_goodbyeTraining_2':  '{}Phase III training_gesture_goodbye 拜拜_2nd.mp4'.format(p3_training_prefix),
  'p3_training_helloTraining_2':  '{}Phase III training_gesture_handshake 你好_2nd.mp4'.format(p3_training_prefix),
  'p3_training_hugTraining_2':  '{}Phase III training_gesture_hugging 抱抱_2nd.mp4'.format(p3_training_prefix),
  'p3_training_hungryTraining_2':  '{}Phase III training_gesture_hungry 肚餓_2nd.mp4'.format(p3_training_prefix),
  'p3_training_mineTraining_2':  '{}Phase III training_gesture_myself 自己_2nd.mp4'.format(p3_training_prefix),
  'p3_training_notAllowedTraining_2':  '{}Phase III training_gesture_no 唔准_2nd.mp4'.format(p3_training_prefix),
  'p3_training_yesTraining_2':  '{}Phase III training_gesture_nodding 可以_2nd.mp4'.format(p3_training_prefix),
  'p3_training_annoyedTraining_2':  '{}Phase III training_gesture_puzzled 好煩_2nd.mp4'.format(p3_training_prefix),
  'p3_training_babyTraining_2':  '{}Phase III training_gesture_rocking baby BB_2nd.mp4'.format(p3_training_prefix),
  'p3_training_comeTraining_2':  '{}Phase III training_gesture_show direction 過嚟_2nd.mp4'.format(p3_training_prefix),
  'p3_training_waitTraining_2':  '{}Phase III training_gesture_wait long 等等_2nd.mp4'.format(p3_training_prefix),
  'p3_training_walkTraining_2':  '{}Phase III training_gesture_walking 行路_2nd.mp4'.format(p3_training_prefix),
  'p3_training_welcomeTraining_2':  '{}Phase III training_gesture_welcome 歡迎_2nd.mp4'.format(p3_training_prefix),
  'p3_training_whereTraining_2':  '{}Phase III training_gesture_where 邊度_2nd.mp4'.format(p3_training_prefix),
  'p3_training_wrongTraining_2':  '{}Phase III training_gesture_wrong 錯嘅_2nd.mp4'.format(p3_training_prefix),

  # This is a longer response given when user makes a correct choice given during posttest
  'p3_feedback_correct':    '{}Phase III training _ assessment_gesture feedback_correct.mp4'.format(p3_feedback_prefix),

  # these are feedback videos if the incorrect gestures are made, the video demonstrates the correct gesture
  'p3_feedback_angryIncorrect':     '{}Phase III training _ assessment_gesture feedback_incorrect_angry 好嬲.mp4'.format(p3_feedback_prefix),
  'p3_feedback_awesomeIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_clapping 好嘢.mp4'.format(p3_feedback_prefix),
  'p3_feedback_driveIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_driving 揸車.mp4'.format(p3_feedback_prefix),
  'p3_feedback_eatIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_eating 食嘢.mp4'.format(p3_feedback_prefix),
  'p3_feedback_birdIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_flying 雀仔.mp4'.format(p3_feedback_prefix),
  'p3_feedback_goodbyeIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_goodbye 拜拜.mp4'.format(p3_feedback_prefix),
  'p3_feedback_helloIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_handshake 你好.mp4'.format(p3_feedback_prefix),
  'p3_feedback_hugIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_hugging 抱抱.mp4'.format(p3_feedback_prefix),
  'p3_feedback_hungryIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_hungry 肚餓.mp4'.format(p3_feedback_prefix),
  'p3_feedback_mineIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_myself 自己.mp4'.format(p3_feedback_prefix),
  'p3_feedback_notAllowedIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_no 唔准.mp4'.format(p3_feedback_prefix),
  'p3_feedback_yesIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_nodding 可以.mp4'.format(p3_feedback_prefix),
  'p3_feedback_annoyedIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_puzzled 好煩.mp4'.format(p3_feedback_prefix),
  'p3_feedback_babyIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_rocking baby BB.mp4'.format(p3_feedback_prefix),
  'p3_feedback_comeIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_show direction 過嚟.mp4'.format(p3_feedback_prefix),
  'p3_feedback_waitIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_wait long 等等.mp4'.format(p3_feedback_prefix),
  'p3_feedback_walkIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_walking 行路.mp4'.format(p3_feedback_prefix),
  'p3_feedback_welcomeIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_welcome 歡迎.mp4'.format(p3_feedback_prefix),
  'p3_feedback_whereIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_where 邊度.mp4'.format(p3_feedback_prefix),
  'p3_feedback_wrongIncorrect':  '{}Phase III training _ assessment_gesture feedback_incorrect_wrong 錯嘅.mp4'.format(p3_feedback_prefix),



  
}

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








    