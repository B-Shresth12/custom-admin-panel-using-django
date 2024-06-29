from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View

# importing login and logout
from django.contrib.auth import login, logout

# importing user authentication form
from django.contrib.auth.forms import AuthenticationForm

class AdminLoginView(View):
    def get(self, request):
        return render(request, 'admin/login.html')

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('admin:dashboard')
            else:
                return HttpResponse("Forbidden", status=403)

        return render(request, "admin/login.html", {"form": form})


class AdminLogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('welcome')
