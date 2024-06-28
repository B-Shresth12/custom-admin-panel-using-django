from django.urls import path
from . import views

app_name="admin"

urlpatterns = [
    # Admin Login and logout routes
    path('login/', views.AdminLoginView.as_view(), name="login"),
    path('logout/', views.AdminLogoutView.as_view(), name="logout"),

    path('', views.DashboardController.admin_dashboard, name="home"),
]
