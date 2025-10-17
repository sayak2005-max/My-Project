from django.shortcuts import render, redirect 
from .models import Student
from .forms import StudentForm
# Create your views here.


def home(request):
    students = Student.objects.all()
    return render(request, "home.html", {"students": students})
def StudentCreate(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student-list")
    else:
        form = StudentForm()
    return render(request, "student_form.html", {"form": form})

def StudentUpdate(request, id):
    student =  Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student-list")
        
    else:
        form = StudentForm(instance=student)
    return render(request, "student_form.html", {"form": form})

def StudentDelete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("student-list")
def student_list(request):
    students = Student.objects.all()
    return render(request, "studentlist.html", {"students": students})
