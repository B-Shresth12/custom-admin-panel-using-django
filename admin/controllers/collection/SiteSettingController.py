from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from ..Controller import Controller
from admin.Forms.SiteSettingForm import SitesettingBasicForm, SiteSettingSEOForm
from admin.Models.SiteSetting import SiteSetting

# Importing ObjectDoesNotExist exception
from django.core.exceptions import ObjectDoesNotExist


class SiteSettingController(Controller):
    def get(self, request):
        setting = SiteSetting.objects.get(pk=1)

        return render(request, 'admin/site-settings/index.html', {'setting': setting})

    def post(self, request, *args, **kwargs):
        if "update" in self.kwargs.get('action',  ''):
            return self.update(request, *args, **kwargs)
        elif "updateSEO" in self.kwargs.get('action', ''):
            return self.updateSEO(request, *args, **kwargs)
        else:
            return redirect('admin:dashboard')

    def update(self, request, *args, **kwargs):
        try:
            site_setting = SiteSetting.objects.get(pk=1)
        except ObjectDoesNotExist:
            site_setting = None

        basicForm = SitesettingBasicForm(
            request.POST, request.FILES, instance=site_setting)

        if basicForm.is_valid():
            basicForm.save()
            return redirect('admin:siteSetting')

        return HttpResponse('updating basic information')

    def updateSEO(self, request, *args, **kwargs):
        return HttpResponse('updating SEO information')
