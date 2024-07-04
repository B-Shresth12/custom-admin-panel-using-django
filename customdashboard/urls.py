from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def redirectToHome(self):
    return HttpResponse('Welcome Page')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', redirectToHome, name="welcome"),
    path('admin/', include('admin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
