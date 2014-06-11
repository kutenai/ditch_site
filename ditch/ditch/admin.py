
from django.contrib import admin as a
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User,Group
from ditchdb.models import DitchLog,DitchCal

class DitchAdminSite(a.AdminSite):
    @never_cache
    def index(self, request, extra_context=None):
        context = {'title': 'ditch.gardenbuzz.com Administration'}
        for model, model_admin in self._registry.items():
            setattr(model._meta, 'verbose_name_plural', unicode(model._meta.verbose_name_plural))
        response = super(DitchAdminSite, self).index(request, extra_context=context)
        return response

site = DitchAdminSite()
site.register(User)
site.register(Group)
site.register(DitchLog)
site.register(DitchCal)
