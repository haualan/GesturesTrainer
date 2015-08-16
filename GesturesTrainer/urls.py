from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('exercises.urls', namespace = "exercises")),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    ]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# social oauth
urlpatterns.append(url('', include('social.apps.django_app.urls', namespace='social')))

urlpatterns = i18n_patterns(*urlpatterns)
