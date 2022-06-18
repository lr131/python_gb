from pprint import pprint
from random import choice, sample


# 1. Написать функцию num_translate(), переводящую числительные
# от 0 до 10 c английского на русский язык.
def num_translate(numeral_en):
    numeral_en_ru = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    return numeral_en_ru.get(numeral_en)


def iscapitalize(word):
    """Проверяет, написано ли слово с заглавной буквы"""
    return word[0].isupper() and word[1:].islower()


# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной
def num_translate_adv(numeral_en):
    if iscapitalize(numeral_en):
        return num_translate(numeral_en.lower()).capitalize() \
            if num_translate(numeral_en.lower()) else None
    else:
        return num_translate(numeral_en)


# Написать функцию thesaurus(), принимающую в качестве аргументов
# имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
def thesaurus(*args):
    result = {}
    for name in args:
        result.setdefault(name[0], []).append(name)
    return result


def thesaurus_sort_by_key(thesaur):
    return dict(sorted(thesaur.items(), key=lambda item: item[0]))


def thesaurus_adv(*args):
    result = {}
    for data in args:
        inner_dict = result.setdefault(data.split(' ')[1][0], {})
        inner_dict.setdefault(data.split(' ')[0][0], []).append(data)
    return result


def get_jokes(count, repeat=True):
    """Возвращает n шуток, сформированных из трех случайных слов, взятых из
    трех списков (по одному из каждого.

    :param count: количество шуток
    :param repeat: разрешает повтор слов в шутках. По умолчанию True
    :return: список шуток"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if repeat:
        return [" ".join([choice(nouns), choice(adverbs), choice(adjectives)])
                for i in range(count)]
    noun, adverb, adjective = list(map(lambda x: sample(x, count),
                                       (nouns, adverbs, adjectives)))
    return [f"{noun[i]} {adverb[i]} {adjective[i]}" for i in range(count)]


if __name__ == '__main__':
    print("Задача с переводом числительных num_translate():")
    print("one: ", num_translate('one'))
    print("five: ", num_translate('five'))
    print("12: ", num_translate("12"))
    print("\nЗадача с переводом числительных num_translate_adv():")
    print("One: ", num_translate_adv("One"))
    print("two: ", num_translate_adv("two"))
    print("hghjgfkdkjd: ", num_translate_adv("hghjgfkdkjd"))
    print("\nЗадача с тезаурусом thesaurus():")
    pprint(thesaurus("Иван", "Мария", "Петр", "Илья"))
    print("Как поступить, если потребуется сортировка по ключам: ")
    data = thesaurus("Иван", "Мария", "Петр", "Илья")
    print(thesaurus_sort_by_key(data))
    print("\nЗадача с тезаурусом thesaurus_adv():")
    pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                         "Илья Иванов", "Анна Савельева"))
    print("Как поступить в случае adv, если потребуется сортировка по ключам:")
    pprint(thesaurus_sort_by_key(thesaurus_adv("Иван Сергеев", "Инна Серова",
                                              "Петр Алексеев","Илья Иванов",
                                              "Анна Савельева")))
    print("\nЗадача с шутками, повторения разрешены:")
    print(get_jokes(4))
    print("\nЗадача с шутками, повторения отключены:")
    print(get_jokes(4, repeat=False))
    print("\nЗадача с шутками, вызов с именованными аргументами:")
    print(get_jokes(repeat=False, count=2))


