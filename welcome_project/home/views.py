from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('home')  # Replace 'home' with your main page name

def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Student registered successfully!"
            return redirect('register')  # Redirect to clear form after saving
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'register.html', {
        'form': form,
        'students': students
    })
