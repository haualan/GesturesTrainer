# from django.contrib import admin

# # Register your models here.
# from .models import Snippet, ExerciseResult

# admin.site.register(Snippet)

# admin.site.register(ExerciseResult)


""" Django-admin autoregister -- automatic model registration

## sample admin.py ##

from yourproject.autoregister import autoregister

# register all models defined on each app
autoregister('app1', 'app2', 'app3', ...)

"""

from django.db.models import get_models, get_app
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from exercises.models import ExerciseResult

# we want to make sure username gets printed on export so we need a custom resource
class ExerciseResultResource(resources.ModelResource):

  class Meta:
      model = ExerciseResult
      fields = ('owner__username', 'id', 'created', 'owner', 'phase', 'section', 'gestureTested' ,'response',)


def autoregister(*app_list):
  for app_name in app_list:
    app_models = get_app(app_name)
    for model in get_models(app_models):
      try:
        # print list(map(lambda x: x.name ,model._meta.fields))[1:]
        class ModAdmin(ImportExportModelAdmin):
          if model.__name__ == 'ExerciseResult':
            resource_class = ExerciseResultResource
          list_display = list(map(lambda x: x.name ,model._meta.fields))[1:]
        admin.site.register(model, ModAdmin)
      except AlreadyRegistered:
        pass

autoregister('exercises')
