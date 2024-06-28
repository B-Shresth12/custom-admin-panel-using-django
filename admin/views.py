from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   

from .controllers.AuthController import *
from .controllers import DashboardController


