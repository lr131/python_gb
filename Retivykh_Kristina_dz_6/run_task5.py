import re

import utils_users

REGEXP_FILENAME = r"[^\\/^*?<>|\r\n]+$"


def get_filename():
    return input(f"Введите название файла без пути к нему:\n")


def confirm_filename(filename):
    while True:
        data = input(
            f"Файл с данными о пользователях называется {filename}?  (Y/N)\n")
        if data.upper() == "Y":
            return filename
        else:
            filename = get_filename()
            confirm_filename(filename)


def get_path(message):
    full_path = input(f"{message}\n")
    match_filename = re.search(REGEXP_FILENAME, full_path)
    filename = match_filename.group()
    if not filename:
        filename = get_filename()
    filename = confirm_filename(filename)
    if filename != match_filename.group():
        pass
    return full_path


if __name__ == '__main__':
    # /home/lr131/projects/python_gb/Retivykh_Kristina_dz_6/users/users.csv
    users_path = get_path("Укажите путь к файлу с данными о пользователях:")
    # /home/lr131/projects/python_gb/Retivykh_Kristina_dz_6/hobby/hobby.csv
    hobby_path = get_path("Укажите путь к файлу с данными о хобби:")
    # /home/lr131/projects/python_gb/Retivykh_Kristina_dz_6/test/result.csv
    result_path = get_path("Укажите, куда сохранить результат:")
    data = utils_users.get_info_adv(users_path, hobby_path)
    utils_users.save_file_adv(["family",
                               "name",
                               "patr",
                               "hobby"], result_path, ";")
    for datum in data:
        utils_users.save_file_adv(datum.values(), result_path, ";")
    print(f"Файл {result_path} успешно сохранен")

