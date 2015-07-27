from exercises.models import Snippet, ExerciseResult, Phase, Section, PhaseSection, QUESTIONS, VIDEOS, P3_VIDEO_CUTOFF
from exercises.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views import generic
from django.shortcuts import render
from django.db.models import Avg, Max, Min, Count
from django.http import HttpResponse

from exercises.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from random import sample
import json, ast
from datetime import date, timedelta, datetime
from django.utils import timezone


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


def logged_in_and_in_group(user):
  r = False
  if user.is_authenticated():
    # current requirement only requires user to be authenticated to be able to use the site
    r = True

    # # group that user needs to be in
    # if user.groups.filter(name='patientGroup').exists():
    #   r = True
  return r

class GroupRequiredMixin(object): 
  # path to be redirected when user is not logged in yet
  login_url = '/'
  
  @method_decorator(user_passes_test(logged_in_and_in_group, login_url=login_url))
  def dispatch(self, *args, **kwargs):
    return super(GroupRequiredMixin, self).dispatch(*args, **kwargs)

class DashboardView(GroupRequiredMixin, generic.View):
  """
  DashboardView is the first view after login the user sees, which contains all the sections available as buttons
  All exercises should be displayed as buttons
  Only exercises that are accessible should be enabled
  Otherwise, exercises that are not accessible should be disabled


  """



  all_sections = [
        {'name': 'phase1-pretest', 'is_enabled': True},
        {'name': 'phase1-training', 'is_enabled': False},
        {'name': 'phase1-posttest1', 'is_enabled': False},
        {'name': 'phase1-posttest2', 'is_enabled': False},

    ]



  def get(self, request):


    a = Exercise(user = request.user)

    sectionsAvailable =  a.sectionsAvailable()
    response = {"all_sections": sectionsAvailable}
    
    if request.user.groups.filter(name='debug').exists():
            response['debug'] = True



    return render(request,'exercises/dashboard.html', 
         response
      )

class UserResponseView(GroupRequiredMixin, generic.View):
    """
    UserResponseView handles user response when user picks a choice on ExerciseView
    """

    def post(self, request):

        # print 'response posted......', request.POST.get('phase'), request.POST.get('section'), request.POST.get('target'),request.POST.get('choice')
        # insert data into models
        try:
            data = ExerciseResult(
                                owner= request.user,
                                phase = request.POST.get('phase'),
                                section = request.POST.get('section'),
                                gestureTested = request.POST.get('target'),
                                response = request.POST.get('choice'),
                                    )
            data.save()
        except Exception,e: 
            print str(e)
            return HttpResponse(status=500)

        return HttpResponse(status=201)

    def get(self, request):
        # checks user's progess and whether they should exit the section
        a = Exercise(user = request.user)
        phase = request.GET.get('phase')
        section = request.GET.get('section')

        return HttpResponse(json.dumps({'response': a.endCurrentSection(phase, section)}), content_type='application/json')


class ExerciseView(GroupRequiredMixin, generic.View):
    """
    ExerciseView is the actual view that delivers the videos and question choices for the users
    """

    def post(self, request):
        response = {}
        
        a = Exercise(user = request.user)

        print 'dashbtn:', request.POST.get('dashbtn', False)

        phase_section = request.POST.get('dashbtn', False)
        if phase_section:
            phase_section = phase_section.split(',')
            phase = phase_section[0]
            section = phase_section[1]
            self.request.session['dashbtn'] = {'phase':phase, 'section': section}
        else:
            # phase_section = ast.literal_eval(request.POST.get('dashbtn', 'False'))
            phase_section = self.request.session['dashbtn'] 
            phase = phase_section['phase']
            section = phase_section['section']


        # if user clicked understandBtn, user understands the instruction video, update cookies and proceed to questions
        if request.POST.get('understandBtn', False) == '1':
            self.request.session['watched_instruction_already_{}_{}'.format(phase, section)] = True


        print 'phase_section: ', phase_section, phase, section

        print 'request.session', self.request.session

        greetings_and_instruction = None
        generateQuestion = None


        if 'watched_instruction_already_{}_{}'.format(phase, section) in self.request.session.keys() and self.request.session['watched_instruction_already_{}_{}'.format(phase, section)] == True:
            # user has watched instruction and greeting videos, proceed to generating question
            response['watched_instruction_already'] = True
            response['generateQuestion'] = a.generateQuestion(phase, section)
        else:
            # user hasn't watched instructions yet, redirect to instruction and greeting videos
            response['watched_instruction_already'] = False
            response['generateInstruction'] = a.generateInstruction(phase, section)
            




        response['request'] = self.request.session.keys()
        response['phase'] = phase
        response['section'] = section
        response['robothead_small_image'] = 'https://s3-ap-southeast-1.amazonaws.com/gesturetrainingmedia/robothead_small.png'

        if request.user.groups.filter(name='debug').exists():
            response['debug'] = True

        return render(request,'exercises/exercise.html', 
        response
          )



phase_ordered_list = [
    'phase1',
    'phase2',
    'phase3',
]

section_ordered_list = [
    'pretest',
    'training',
    'posttest1',
    'posttest2',
    'posttest3',
]

class Exercise(object):
    """Abstract class for a exercise or question"""
    def __init__(self, user):
        self.user = user


    def sectionsAvailable(self):
        """
        returns sections <array> that are open to the user based on the progress of the user
        """

        q = ExerciseResult.objects.filter(owner = self.user)
        # select count from exercises where user = user, group by section
        q = q.values('phase','section').annotate(Count('owner')).values_list('phase','section', 'owner__count')
 
        # initialize user progress with all 0s, place it in <dict> for easy update
        user_progress = {}
        for i in phase_ordered_list:
            user_progress[i] = {}
            for j in section_ordered_list:
                user_progress[i][j] = 0



        # update count from DB
        for i in q:
            user_progress[i[0]][i[1]] = i[2]

        # generate a list of dicts and determine whether section should be enabled
        today_date = timezone.now()
        previous_section_complete = True

        results = []
        found_next_section = False
        for i in phase_ordered_list:
            for j in section_ordered_list:
                result = {}
                result['phase'] = i
                result['section'] = j
                result['name'] = i + '_' +j
                result['user_progress'] = user_progress[i][j]

                phaseSection_start_date = PhaseSection.objects.filter(phase = i, section = j).values_list('start_date')[0][0]
                result['phaseSection_start_date'] = phaseSection_start_date
                
                # is today greater than section startdate?
                if today_date > phaseSection_start_date:
                    # what section is it?
                    if j == 'training':
                        if user_progress[i][j] < 40:
                            # is previous section complete?
                            if previous_section_complete:
                                result['is_enabled'] = True
                                previous_section_complete = False


                        elif user_progress[i][j] >=40 and user_progress[i][j] < 80:
                            # has it been one week after start_date
                            secondCycleCompleteDateTime = ExerciseResult.objects.filter(phase = i, section = j).values_list('created').order_by('created')[40-1][0]
                            if (today_date > phaseSection_start_date + timedelta(weeks = 1)) and (today_date > secondCycleCompleteDateTime + timedelta(weeks = 1)):
                                # is previous section complete?
                                if previous_section_complete:
                                    result['is_enabled'] = True
                                    previous_section_complete = False
                                else:
                                    result['is_enabled'] = False
                                    previous_section_complete = True


                        else:
                            result['is_enabled'] = False
                            previous_section_complete = True


                    else:
                        if user_progress[i][j] >= 20:
                            result['is_enabled'] = False
                            previous_section_complete = True
                        else:
                            # is previous section complete?
                            if previous_section_complete:
                                result['is_enabled'] = True
                                previous_section_complete = False


                else:
                    result['is_enabled'] = False

                results.append(result)



        if self.user.is_superuser:
            print 'superuser is logged in, activate all sections', self.user, self.user.is_superuser
            results = []
            for i in phase_ordered_list:
                for j in section_ordered_list:
                    results.append({
                        'phase': i, 
                        'section': j, 
                        'name': i + '_' +j, 
                        'user_progress': user_progress[i][j], 
                        'is_enabled': True,
                        'phaseSection_start_date': phaseSection_start_date
                        }
                        )

        return results

    def generateInstruction(self, phase, section):
        """
        returns the current instruction / greetings <dict> according to the type required to be rendered in different phases and sections
        """

        # grab all the data belonging to current user
        phase_id = Phase.objects.filter(phase = phase).values_list('id')[0][0]
        section_id = Section.objects.filter(section = section).values_list('id')[0][0]

        queryset = ExerciseResult.objects.filter(owner = self.user, phase = phase_id, section = section_id)

        phase_num = phase[5:]

        if section == 'pretest':
            results = {
                'greetingVideo': VIDEOS['p{}_assessment_greetingAndInstruction'.format(phase_num)],
                'doYouUnderstandVideo': VIDEOS['p{}_assessment_doYouUnderstand'.format(phase_num)]
            }

        if section == 'training':
            results = {
                'greetingVideo': VIDEOS['p{}_training_greetingAndInstruction'.format(phase_num)],
                'doYouUnderstandVideo': VIDEOS['p{}_training_doYouUnderstand'.format(phase_num)]
            }

        if (    section == 'posttest1' or
                section == 'posttest2' or
                section == 'posttest3' 
                ):
            results = {
                'greetingVideo': VIDEOS['p{}_assessment_greetingAndInstruction'.format(phase_num)],
                'doYouUnderstandVideo': VIDEOS['p{}_assessment_doYouUnderstand'.format(phase_num)]
            }

        return results

    def userProgress(self, phase, section):
        queryset = ExerciseResult.objects.filter(owner = self.user, phase = phase, section = section).values_list('gestureTested')
        return len(queryset)
    
    def endCurrentSection(self, phase, section):
        count = self.userProgress(phase, section)

        if count == 0:
            return False
        if count % 20 == 0:
            return True

        return False





    def generateQuestion(self, phase, section):
        """
        returns the current question <dict> according to the type required to be rendered in different phases and sections
        """

        # grab all the data belonging to current user

        # phase_id = Phase.objects.filter(phase = phase).values_list('id')[0][0]
        # section_id = Section.objects.filter(section = section).values_list('id')[0][0]
        # queryset = ExerciseResult.objects.filter(owner = self.user, phase = phase_id, section = section_id) 

        if section == 'training':
            queryset = ExerciseResult.objects.filter(owner = self.user, phase = phase, section = section).order_by('created').values_list('gestureTested')
            progress_percent = len(queryset) / float(len(QUESTIONS) * 4)

            # we only want the remaineder of the 20 questions of the section
            cut = len(queryset) % 20
            if cut == 0:
                queryset = []
            else:
                queryset = list(queryset)[-cut:]
        else:
            # if the section is training, then we only take the last mod 20 of the results
            queryset = ExerciseResult.objects.filter(owner = self.user, phase = phase, section = section).values_list('gestureTested')
            progress_percent = len(queryset) / float(len(QUESTIONS))

        queryset = set(map(lambda x: x[0],queryset))

        # find all the remaining questions needed for the section
        unanswered = set(QUESTIONS) - queryset


        print 'set(QUESTIONS)', set(QUESTIONS)
        print 'set(queryset)', set(queryset)
        print len(set(queryset))
        print 'unanswered:', unanswered
        print len(unanswered)

        # progress = len(unanswered) / len(set(QUESTIONS))

        # if (progress_percent >= 1.0 and section != 'training') or (section == 'training' and progress_percent > 0.0 and len(queryset) % 20 == 0):
        #     # posttest or pretest section is finished kick user back to dashboard
        #     #  or
        #     # since training sections have 4 * 20 = 80 questions we have to kick users out every 20th question
        #     return {
        #         'question': None,
        #         'status' : 'user completed all questions in this section',
        #         'phase' : phase,
        #         'section': section,
        #         'Feedback': 'You have completed all questions in this section!'
        #     }

        #     # TBD need to think of a way to let training users go back in



        if len(unanswered) != 0:
        # if True:

            # randomize the order of the unanswered questions

            # pick the first item randomly as the next question:
            unanswered = sample(unanswered, 1)[0]

            if phase == 'phase1' and section == 'pretest':

                # get randomized choices of that unanswered question
                choices = sample(QUESTIONS[unanswered]['choices'],3)

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,


                    'instructionPreGestureVideo': VIDEOS['p1_assessment_instructionPreGesture'],

                    'targetGestureVideo': VIDEOS['p1_assessment_{}Gesture'.format(unanswered)],

                    'instructionPostGestureVideo': VIDEOS['p1_assessment_instructionPostGesture'],

                    'choiceA': choices[0],
                    'choiceAVideo':VIDEOS['p1_assessment_{}Choice'.format(choices[0])],
                    'choiceB': choices[1],
                    'choiceBVideo':VIDEOS['p1_assessment_{}Choice'.format(choices[1])],
                    'choiceC': choices[2],
                    'choiceCVideo': VIDEOS['p1_assessment_{}Choice'.format(choices[2])],


                    'MakeAChoiceVideo': VIDEOS['p1_assessment_makeAChoiceNow'],

                    'FeedbackThanks': VIDEOS['p1_feedback_thankyou'],



                }

                # return questionSet

            if phase == 'phase1' and section == 'training':

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,
                    'targetGestureVideo': VIDEOS['p1_training_{}Training'.format(unanswered)],

                }

                # return questionSet

            if phase == 'phase1' and (section == 'posttest1' or 
                                        section == 'posttest2' or
                                        section == 'posttest3' ) :

                # get randomized choices of that unanswered question
                choices = sample(QUESTIONS[unanswered]['choices'],3)

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,


                    'instructionPreGestureVideo': VIDEOS['p1_assessment_instructionPreGesture'],

                    'targetGestureVideo': VIDEOS['p1_assessment_{}Gesture'.format(unanswered)],

                    'instructionPostGestureVideo': VIDEOS['p1_assessment_instructionPostGesture'],

                    'choiceA': choices[0],
                    'choiceAVideo':VIDEOS['p1_assessment_{}Choice'.format(choices[0])],
                    'choiceB': choices[1],
                    'choiceBVideo':VIDEOS['p1_assessment_{}Choice'.format(choices[1])],
                    'choiceC': choices[2],
                    'choiceCVideo': VIDEOS['p1_assessment_{}Choice'.format(choices[2])],


                    'MakeAChoiceVideo': VIDEOS['p1_assessment_makeAChoiceNow'],

                    'FeedbackCorrect': VIDEOS['p1_feedback_correct'],
                    'FeedbackWrong': VIDEOS['p1_feedback_{}Incorrect'.format(unanswered)],


                }

            if phase == 'phase2' and section == 'pretest':

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,


                    'instructionPreGestureVideo': VIDEOS['p2_assessment_instructionPreGesture'],

                    'targetGestureVideo': VIDEOS['p2_assessment_{}Gesture'.format(unanswered)],

                    'FeedbackThanks': VIDEOS['p2_feedback_thankyou'],


                }

            if phase == 'phase2' and section == 'training':

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,
                    'targetGestureVideo1': VIDEOS['p2_training_{}Training_1'.format(unanswered)],
                    'targetGestureVideo2': VIDEOS['p2_training_{}Training_2'.format(unanswered)],

                }

            if phase == 'phase2' and (section == 'posttest1' or 
                            section == 'posttest2' or
                            section == 'posttest3' ) :

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,


                    'instructionPreGestureVideo': VIDEOS['p2_assessment_instructionPreGesture'],

                    'targetGestureVideo': VIDEOS['p2_assessment_{}Gesture'.format(unanswered)],

                    'FeedbackCorrect': VIDEOS['p2_feedback_correct'],
                    'FeedbackWrong': VIDEOS['p2_feedback_{}Incorrect'.format(unanswered)],


                }

            if phase == 'phase3' and section == 'pretest':

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,

                    'targetGestureVideo': VIDEOS['p3_assessment_{}_{}Gesture'.format(section,unanswered)],

                    'FeedbackThanks': VIDEOS['p3_feedback_thankyou'],

                    # phase 3 pretest special delay sequence
                    'videoCutoff': P3_VIDEO_CUTOFF[unanswered][0],


                }

            if phase == 'phase3' and section == 'training':

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,
                    'targetGestureVideo1': VIDEOS['p3_training_{}Training_1'.format(unanswered)],
                    'targetGestureVideo2': VIDEOS['p3_training_{}Training_2'.format(unanswered)],

                }

            if phase == 'phase3' and (section == 'posttest1' or 
                            section == 'posttest2' or
                            section == 'posttest3' ) :

                questionSet = {
                    # basic values for the section
                    'phase': phase,
                    'section': section,
                    'targetGesture': unanswered,

                    'targetGestureVideo': VIDEOS['p3_assessment_{}_{}Gesture'.format(section,unanswered)],

                    'FeedbackCorrect': VIDEOS['p3_feedback_correct'],
                    'FeedbackWrong': VIDEOS['p3_feedback_{}Incorrect'.format(unanswered)],

                    # phase 3 posttest special delay sequence
                    'videoCutoff': P3_VIDEO_CUTOFF[unanswered][int(section[-1])],


                }


            questionSet['progress_percent'] = progress_percent
            return questionSet








        # if user has completed all questions, then we should move on

















        