import sys
import os
from utils import get_students

BASE_URL = 'https://lab.ssafy.com'
DIR_NAME = sys.argv[1]


def check_directory(now_dir):
    for dirpath, dirnames, filenames in os.walk(now_dir):
        for filename in filenames:
            if filename == 'manage.py':
                if dirpath is not now_dir:
                    # 상위 경로 이름 수정(프로젝트 디렉토리 이름 겹칠 수 있어서), 파일 옮김, 기존 상위 경로 삭제
                    os.system(f'mv {dirpath}/ {dirpath}_temp/')
                    os.system(f'mv {dirpath}_temp/* {now_dir}/')
                    os.system(f'rm -rf {dirpath}_sample/')
                return True

failure = []

SUPER_USERNAME = 'happy'
SUPER_PASSWORD = '1234'

for name, gitlab_name in get_students():
    print(f'========== {name} ==========')
    result = os.system(f'git clone {BASE_URL}/{gitlab_name}/{DIR_NAME}.git ./{DIR_NAME}/{name}')
    if result == 0:
        # manage.py의 경로를 확인합니다.
        check_directory(f'./{DIR_NAME}/{name}/')
        
        # migration 과정이 필요한 경우
        os.system(f'python ./{DIR_NAME}/{name}/manage.py makemigrations')
        os.system(f'python ./{DIR_NAME}/{name}/manage.py migrate') 
        # super유저 설정
        os.system(f'python ./{DIR_NAME}/{name}/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(\'{SUPER_USERNAME}\', None, \'{SUPER_PASSWORD}\')"')
    else:
        failure.append(name)
    print()

print((f'========== clone 완료 ✅ =========='))
if len(failure) != 0:
    print((f'========== 총 {len(failure)}명 실패 🚨 =========='))
    with open('results.txt', 'w', encoding='utf-8', newline='') as f:
        f.write(f'{DIR_NAME} clone 실패 학생 목록\n')
        for name in failure:
            f.write(f'{name}\n')