import itertools
import json
import csv


def get_info(users_file, hobbies_file):
    data = {}
    with open(users_file, 'r', encoding='utf-8') as users:
        with open(hobbies_file, "r", encoding="utf-8") as hobbies:
            for user, hobby in itertools.zip_longest(users, hobbies):
                if not user:
                    return 1
                data[" ".join(user.strip().split(","))] = tuple(
                    hobby.strip().split(",")
                ) if hobby else None
        return data


def get_info_adv(users_file, hobbies_file):
    with open(users_file, 'r', encoding='utf-8') as users:
        with open(hobbies_file, "r", encoding="utf-8") as hobbies:
            for user, hobby in itertools.zip_longest(users, hobbies):
                if not user:
                    return 1
                yield ({
                    "family": user.strip().split(",")[0],
                    "name": user.strip().split(",")[1],
                    "patr": user.strip().split(",")[2],
                    "hobby": tuple(hobby.strip().split(",")) if hobby else None
                })


def save_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def save_file_adv(data, filename, separator=";"):
    """Записывает данные в файл построчно"""
    with open(filename, 'a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=separator)
        writer.writerow(data)


def load_row_data(filename, separator=";"):
    """Загружает данные из файла csv построчно."""
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=separator)
        for row in reader:
            yield row
