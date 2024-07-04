# customdashboard/middleware.py

from django.shortcuts import redirect
from django.urls import reverse,resolve, Resolver404
from django.http import Http404, HttpResponse
from django.conf import settings

class AdminLoginRequiredMiddleware:
    """
    Middleware that ensures the user is authenticated for all admin pages
    except for the login and logout pages.
    """

    excluded_urls = [
        settings.LOGIN_URL
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Checking if the path starts with '/admin/' or not and check if the 
        # route is not in excluded_urls
        if request.path.startswith('/admin/') and request.path not in self.excluded_urls:
            try:
                # Checking if the requested route exists or not
                resolve(request.path)
            except Resolver404:
                # If route not found then return 404 response
                raise Http404

            if not request.user.is_authenticated:
                return redirect(settings.LOGIN_URL)

        response = self.get_response(request)
        return response
