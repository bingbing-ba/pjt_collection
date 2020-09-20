from multiprocessing import Process
import os
import sys
from pathlib import Path


# 학생들 pjt에 X-Frame-Option관련 장고 default middleware 해제
def deactivate_XFrameOption(target_pjt, pjt_dir):
    students = os.listdir(pjt_dir)
    students.sort()
    students_with_port = [(student, idx) for idx, student in enumerate(students)]
    
    for student in students:
        settings_file_url = pjt_dir / student / target_pjt / 'settings.py'
        
        new_lines = []
        try:
            with open(settings_file_url) as f:
                lines = f.readlines()
                for line in lines:
                    if 'django.middleware.clickjacking.XFrameOptionsMiddleware' in line:
                        continue
                    new_lines.append(line)
            with open(settings_file_url, 'w') as f:
                f.writelines(new_lines)
        except:
            print(student, '프로젝트 구조에 문제가 있을 수 있음')
    
    return students, students_with_port


def start_server(students_with_port, target_pjt, pjt_dir):
    student, idx = students_with_port
    student_pjt_dir = pjt_dir / student
    os.chdir(student_pjt_dir)
    port_num = str(idx).zfill(2)
    os.environ['DJANGO_SETTINGS_MODULE'] = f'{target_pjt}.settings'
    os.system(f'python manage.py runserver 80{port_num}')


def start_main_server(port):
    os.system(f'python manage.py runserver {port}')


def start_multiprocessing(target_pjt, port):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    pjt_dir = (Path(BASE_DIR) / target_pjt).absolute()

    students, students_with_port = deactivate_XFrameOption(target_pjt, pjt_dir)

    # multiprocessing
    for idx in range(len(students)):
        proc = Process(target=start_server, args=(students_with_port[idx], target_pjt, pjt_dir))
        proc.start()
    
    # start the main server
    proc = Process(target=start_main_server, args=(port,))
    proc.start()


