import os
from multiprocessing import Process
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError

def append_django_seed(target_pjt):
    students = os.listdir(target_pjt)
    for student in students:
        settings_file_url = target_pjt / student / target_pjt / 'settings.py'
        new_lines = []
        have_to_append = True
        try:
            with open(settings_file_url) as f:
                lines = f.readlines()
                for line in lines:
                    new_lines.append(line)
                    if 'django_seed' in line:
                        have_to_append = False
                    if 'django.contrib.staticfiles' in line:
                        new_lines.append("    'django_seed',\n")
            if have_to_append:
                with open(settings_file_url, 'w') as f:
                    f.writelines(new_lines)
        except:
            print(student, '프로젝트 구조에 문제가 있을 수 있음')


def seed_data(student, target_pjt, app, number):
    student_pjt_dir = target_pjt / student
    os.chdir(student_pjt_dir)
    os.environ['DJANGO_SETTINGS_MODULE'] = f'{target_pjt}.settings'
    os.system(f'python manage.py seed {app} --number={number} >> seed.log 2>&1')


class Command(BaseCommand):
    help = 'seed data to students pjt'


    def add_arguments(self, parser):
        parser.add_argument('pjt', type=str)
        parser.add_argument('--number', type=int, default=10, help='amount of seed data')
        parser.add_argument('--app', type=str, default='community', help='app name to seed data')


    def handle(self, *args, **options):
        pjt = options.get('pjt')
        number = options.get('number')
        app = options.get('app')
        students = os.listdir(pjt)
        target_pjt = Path(pjt)
        append_django_seed(target_pjt)
        for student in students:
            proc = Process(target=seed_data, args=(student, target_pjt, app, number))
            proc.start()
        self.stdout.write(
            self.style.SUCCESS(f'''
            =====================================
            SEEDING {number} DATA 
            TO {target_pjt}/{app}
            =====================================
            ''')
        )