# admin/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from admin.models import SiteSetting
from django.contrib.auth.decorators import login_required


class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

    @login_required
    def SiteSettingCheck():
        # Define excluded URLs where redirection should not occur
        excluded_urls = [
            reverse('admin:login'),
            reverse('admin:logout'),
            reverse('admin:siteSetting'),
            reverse('admin:siteSetting.update'),
        ]

        # Check if the requested URL belongs to the admin app
        if request.path_info.startswith('/admin/'):
            # Check if the requested URL is excluded
            if request.path_info in excluded_urls:
                return self.get_response(request)

            # Check if SiteSetting has the first row
            try:
                site_setting = SiteSetting.objects.first()
            except ObjectDoesNotExist:
                site_setting = None

            if not site_setting:
                return redirect('admin:siteSetting')

        return self.get_response(request)
