import sys
import os
from utils import get_students

BASE_URL = 'https://lab.ssafy.com'
DIR_NAME = sys.argv[1]

for name, gitlab_name in get_students():
    print(f'========== {name} ==========')
    # os.system(f'mkdir -p ./{DIR_NAME}/{name}')
    os.system(
        f'git clone {BASE_URL}/{gitlab_name}/{DIR_NAME}.git ./{DIR_NAME}/{name}')
    print()
