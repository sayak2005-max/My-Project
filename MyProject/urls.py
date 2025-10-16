from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Django Project 🚀</h1>")

urlpatterns = [
    path('', home),  # 👈 this handles the empty path
    path('admin/', admin.site.urls),
]
