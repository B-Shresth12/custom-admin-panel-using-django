from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from ..ViewMiddleware import ViewMiddleware
from admin.Forms.SiteSettingForm import SitesettingBasicForm, SiteSettingSEOForm
from admin.Models.SiteSetting import SiteSetting

# importing json and required encoders
import json
from django.core.serializers.json import DjangoJSONEncoder

# Importing ObjectDoesNotExist exception
from django.core.exceptions import ObjectDoesNotExist
# Importing Helper 
from Helper.Helper import *


class SiteSettingView(View):
    def get(self, request):
        try:
            setting = SiteSetting.objects.first()
        except ObjectDoesNotExist:
            setting = None
        
        data = getContentData(request=request, rowData=setting, form_class=SitesettingBasicForm)

        # return HttpResponse(data.data.get('site_email'))
        return render(
            request,
            'admin/site-settings/index.html',
            {
                'data': data,
            })

    def post(self, request, *args, **kwargs):
        if "update" in self.kwargs.get('action', ''):
            return self.update(request, *args, **kwargs)
        elif "updateSEO" in self.kwargs.get('action', ''):
            return self.updateSEO(request, *args, **kwargs)
        else:
            return redirect('admin:dashboard')

    def update(self, request, *args, **kwargs):
        try:
            site_setting = SiteSetting.objects.first()
        except ObjectDoesNotExist:
            site_setting = None

        basicForm = SitesettingBasicForm(
            request.POST, request.FILES, instance=site_setting)
        
        if basicForm.is_valid():
            basicForm.save()

            return redirect('admin:siteSetting')

        request.session['form_data'] = {
            "type": "basic",
            "form": request.POST,
            "errors": basicForm.errors,
        }
        return redirect('admin:siteSetting')

    def updateSEO(self, request, *args, **kwargs):
        return HttpResponse('updating SEO information')
