from django.shortcuts import render
from django.conf import settings
import os


def find_markdown(now_dir):
    for dirpath, dirnames, filenames in os.walk(now_dir.__str__()):
        for filename in filenames:
            if filename.lower() == 'readme.md':
                return filename
    
    for dirpath, dirnames, filenames in os.walk(now_dir.__str__()):
        for filename in filenames:
            if filename[-3:] == '.md':
                return filename

    print('Markdown 파일이 없습니다. default name을 반환합니다.')
    return 'README.md'


def index(request, pjt_name):
    BASE_DIR = settings.BASE_DIR
    students = os.listdir(BASE_DIR / pjt_name)
    students.sort()
    students_with_port = [(student, f'80{str(idx).zfill(2)}') for idx, student in enumerate(students)]
    context = {
        'students_with_port': students_with_port,
    }
    return render(request, 'index.html', context)


def readme(request, pjt_name, student_name):
    BASE_DIR = settings.BASE_DIR
    try:
        MARKDOWN = find_markdown(BASE_DIR / pjt_name / student_name)
        with open(BASE_DIR / pjt_name / student_name / MARKDOWN, encoding='utf8') as f:
            readme = f.read()
    except:
        readme = f'# {student_name}님의 프로젝트에 README.md가 없습니다'
    
    return render(request, 'readme.html', {'readme':readme,})
