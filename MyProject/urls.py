from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', include("MyApp.urls")),  # 👈 this handles the empty path
    path('admin/', admin.site.urls),
]
