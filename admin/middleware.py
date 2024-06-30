# admin/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from admin.models import SiteSetting
from django.views import View
from django.http import HttpResponse, HttpResponseForbidden


class AdminMiddleware(View):
    excluded_urls = [
        reverse('admin:login'),
        reverse('admin:logout'),
        reverse('admin:siteSetting'),
        reverse('admin:siteSetting.update'),
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path_info.startswith('/admin/'):

            if request.path_info in self.excluded_urls:
                return self.get_response(request)
            
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    redirect_route = self.SiteSettingCheck(request)
            else:
                return redirect('admin:login')
            
            if redirect_route is not None:
                return redirect(redirect_route)
            
        return self.get_response(request)

    def SiteSettingCheck(self, request):
        # Check if SiteSetting has the first row
        try:
            site_setting = SiteSetting.objects.first()
        except ObjectDoesNotExist:
            site_setting = None

        if not site_setting:
            return redirect('admin:siteSetting')

        return None
