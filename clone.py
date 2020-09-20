import sys
import os
from utils import get_students

BASE_URL = 'https://lab.ssafy.com'
DIR_NAME = sys.argv[1]

success = []
failure = []

for name, gitlab_name in get_students():
    print(f'========== {name} ==========')
    result = os.system(f'git clone {BASE_URL}/{gitlab_name}/{DIR_NAME}.git ./{DIR_NAME}/{name}')
    if result == 0:
        success.append(name)
        os.system(f'cd ./{DIR_NAME}/{name} && python manage.py migrate && cd ../..')
    else:
        failure.append(name)
        os.system(f'rm -rf ./{DIR_NAME}/{name}')
    print()

print((f'========== 총 {len(success)}명 완료 ✅ =========='))
if len(failure) != 0:
    print((f'========== 총 {len(failure)}명 실패 🚨 =========='))
    for name in failure:
        print(f'{name} 학생 저장소 확인 바랍니다.')