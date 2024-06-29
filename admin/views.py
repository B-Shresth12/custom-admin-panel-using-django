from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   

from .Views.collection.AuthView import *
from .Views.collection.DashboardView import *
from .Views.collection.SiteSettingView import *


