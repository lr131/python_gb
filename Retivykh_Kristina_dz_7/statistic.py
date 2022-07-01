import os
from pprint import pprint

# PATH = "/home/lr131/projects/python_gb/Retivykh_Kristina_dz_4/"
PATH = os.curdir
start_size = 10


def get_size(filename):
    """Возвращает размер файла"""
    return os.stat(filename).st_size


def get_end_num(num):
    start_num = start_size
    while num > start_num:
        start_num = start_num * 10
    return start_num


def get_stat(path):
    tree = os.walk(path)
    result = {}
    for i in tree:
        for file in i[2]:
            size = get_size(os.path.join(i[0], file))
            print(file, size, "Байт", size / 1024, "КБ")
            if size <= start_size:
                result.setdefault(start_size, 0)
                result[start_size] += 1
            else:
                end_size = get_end_num(size)
                result.setdefault(end_size, 0)
                result[end_size] += 1
    return result


if __name__ == '__main__':
    pprint(get_stat(PATH))
