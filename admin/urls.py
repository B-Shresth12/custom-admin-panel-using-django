from django.urls import path
from . import views

app_name = "admin"

urlpatterns = [
    # Admin Login and logout routes
    path('login/', views.AdminLoginView.as_view(), name="login"),
    path('logout/', views.AdminLogoutView.as_view(), name="logout"),

    # Admin Dashboard Route
    path('', views.DashboardView.as_view(), name="dashboard"),

    path('site-management/', views.SiteSettingView.as_view(), name="siteSetting"),
    path('site-management/update', views.SiteSettingView.as_view(),
         {'action': 'update'}, name="siteSetting.update"),
    path('site-management/update-seo', views.SiteSettingView.as_view(),
         {'action': 'updateSEO'}, name="siteSetting.updateSEO"),
]
