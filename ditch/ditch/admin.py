
from django.contrib import admin as a
from django.views.decorators.cache import never_cache


class DitchAdminSite(a.AdminSite):
    @never_cache
    def index(self, request, extra_context=None):
        context = {'title': 'Schematics.com Administration'}
        for model, model_admin in self._registry.items():
            setattr(model._meta, 'verbose_name_plural', unicode(model._meta.verbose_name_plural))
        response = super(DitchAdminSite, self).index(request, extra_context=context)
        return response

site = DitchAdminSite()
