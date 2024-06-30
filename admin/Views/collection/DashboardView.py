from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from ..ViewMiddleware import ViewMiddleware

from ...Models.SiteSetting import SiteSetting

class DashboardView(View):
    def get(self, request):
        return render(request, 'admin/dashboard.html')
