from django.shortcuts import render
from django.conf import settings
import os
# Create your views here.
def index(request, pjt_name):
    BASE_DIR = settings.BASE_DIR
    students = os.listdir(BASE_DIR / pjt_name)
    students.sort()
    students_with_port = [(student, f'80{str(idx).zfill(2)}') for idx, student in enumerate(students)]
    context = {
        'students_with_port': students_with_port,
    }
    return render(request, 'index.html', context)

