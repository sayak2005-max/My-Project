from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.StudentList, name="student-list"),
    path("list/", views.StudentList, name="student-list"),
    path("add/", views.StudentCreate, name="student-add"),
    path("create/<int:id>/", views.StudentCreate, name="student-create"),
     path("update/<int:id>/", views.StudentUpdate, name="student-update"),
    path("delete/<int:id>/", views.StudentDelete, name="student-delete"),
]