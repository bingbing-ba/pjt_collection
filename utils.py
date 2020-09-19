def get_students():
    with open('students.csv', 'r', encoding='utf-8') as f:
        return [tuple(info.strip().split('\t')) for info in f.readlines()]
