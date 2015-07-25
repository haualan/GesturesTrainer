from django.conf.urls import url, include
from exercises import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    url(r'^$', 'django.contrib.auth.views.login',{'template_name': 'exercises/login.html'}, name='login'),
    url(r'^dashboard$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^exercise$', views.ExerciseView.as_view(), name='exercise'),
    url(r'^userResponse$', views.UserResponseView.as_view(), name='userResponse'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name = 'logout'),
]