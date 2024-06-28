from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/admin/login/")
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')
