import sys
import os
from utils import get_students

BASE_URL = 'https://lab.ssafy.com'
DIR_NAME = sys.argv[1]


def check_directory(now_dir):
    for dirpath, dirnames, filenames in os.walk(now_dir):
        for filename in filenames:
            if filename == 'manage.py':
                print('manage.py를 찾았습니다 :', dirpath, dirnames)
                if dirpath is not now_dir:
                    print('상위 경로의 이름을 수정합니다.')
                    os.system(f'mv {dirpath}/ {dirpath}_sample/')
                    print('파일을 옮깁니다.')
                    os.system(f'mv {dirpath}_sample/* {now_dir}/')
                    print('기존 상위 경로를 삭제합니다.')
                    os.system(f'rm -rf {dirpath}_sample/')
                return True

success = []
failure = []

for name, gitlab_name in get_students():
    print(f'========== {name} ==========')
    result = os.system(f'git clone {BASE_URL}/{gitlab_name}/{DIR_NAME}.git ./{DIR_NAME}/{name}')
    if result == 0:
        success.append(name)
        # manage.py의 경로를 확인합니다.
        check_directory(f'./{DIR_NAME}/{name}/')
        
        # migration 과정이 필요한 경우
        os.system(f'python ./{DIR_NAME}/{name}/manage.py makemigrations')
        os.system(f'python ./{DIR_NAME}/{name}/manage.py migrate')
    else:
        failure.append(name)
    print()

print((f'========== 총 {len(success)}명 완료 ✅ =========='))
if len(failure) != 0:
    print((f'========== 총 {len(failure)}명 실패 🚨 =========='))
    for name in failure:
        print(f'{name} 학생 저장소 확인 바랍니다.')