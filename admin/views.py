from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   

from .Controllers.collection.AuthController import *
from .Controllers.collection.DashboardController import *
from .Controllers.collection.SiteSettingController import *


