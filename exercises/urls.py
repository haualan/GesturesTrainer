from django.conf.urls import url, include
from exercises import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import login
from django.contrib.auth.decorators import user_passes_test


login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')



urlpatterns = [
    url(r'^login$', login_forbidden(login),{'template_name': 'exercises/login.html' }, name="login"),
    # url(r'^$', 'django.contrib.auth.views.login',{'template_name': 'exercises/login.html'}, name='login'),
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^exercise$', views.ExerciseView.as_view(), name='exercise'),
    url(r'^userResponse$', views.UserResponseView.as_view(), name='userResponse'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name = 'logout'),
]