from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django app!")

urlpatterns = [
    
    path('', home),
    # Admin panel URL (default Django admin site)
    path('admin/', admin.site.urls),

    # Include all URLs from the "tasks" app under the "api/" prefix
    path('api/', include('tasks.urls')),
]
