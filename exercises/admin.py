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

def autoregister(*app_list):
  for app_name in app_list:
    app_models = get_app(app_name)
    for model in get_models(app_models):
      try:
        # print list(map(lambda x: x.name ,model._meta.fields))[1:]
        class ModAdmin(ImportExportModelAdmin):
          list_display = list(map(lambda x: x.name ,model._meta.fields))[1:]
        admin.site.register(model, ModAdmin)
      except AlreadyRegistered:
        pass

autoregister('exercises')
