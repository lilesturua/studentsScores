from django.shortcuts import render, redirect, get_object_or_404
from students_info.models import Student
from students_info.forms import StudentForm


def create(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect("student-detail", form.instance.pk)


    return render(request, "student/create.html", {"form":form})


def list_all(request):
    students = Student.objects.all()

    return render(request, 'student/list.html', {'students':students})


def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(request, 'student/detail.html', {'student':student})


def update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form=StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

            return redirect("student-detail", student.pk)

    return render(request, 'student/update.html', {"form":form})


def delete(request, pk):
    if request.method == "POST":
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        
        return redirect("student-list", student.pk)