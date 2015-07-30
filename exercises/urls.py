from django.conf.urls import url, include
from exercises import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login',{'template_name': 'exercises/login.html'}, name='login'),
    url(r'^dashboard$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^exercise$', views.ExerciseView.as_view(), name='exercise'),
    url(r'^userResponse$', views.UserResponseView.as_view(), name='userResponse'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name = 'logout'),
]