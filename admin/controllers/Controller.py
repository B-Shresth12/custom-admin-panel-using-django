from typing import Any
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

class Controller(View):

    """
    This is a universal controller for 
    controller that need the validation and verification 
    wheather they are superuser or not.
    This controller acts as a middleware for all the controllers for admin app
    """
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        return login_required(view, login_url='/admin/login')
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) :
        if not request.user.is_superuser:
            return HttpResponse("Forbidden", statis=403)
        
        return super().dispatch(request, *args, **kwargs)