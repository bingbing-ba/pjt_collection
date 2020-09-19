from multiprocessing import Pool
import os
import sys
from pathlib import Path
target_pjt = sys.argv[1]
pjt_dir = (Path('.') / target_pjt).absolute()
students = os.listdir(pjt_dir)
students.sort()
students_with_port = [(student, idx) for idx, student in enumerate(students)]

# 학생들 pjt에 X-Frame-Option관련 장고 default middleware 해제
for student in students:
    settings_file_url = pjt_dir / student / target_pjt / 'settings.py'
    
    new_lines = []
    with open(settings_file_url) as f:
        lines = f.readlines()
        for line in lines:
            if "    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n" in line:
                continue
            new_lines.append(line)
    with open(settings_file_url, 'w') as f:
        f.writelines(new_lines)


def start_server(student_with_port):
    student, idx = student_with_port
    student_pjt_dir = pjt_dir / student
    os.chdir(student_pjt_dir)
    port_num = str(idx).zfill(2)
    os.system(f'python manage.py runserver 80{port_num}')

# multiprocessing
pool = Pool(len(students))
pool.map(start_server, students_with_port)