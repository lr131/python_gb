
# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield:
def task_one():
    print("\nПример 1:")
    for i in num_generator(15, 1):
        print(i)
    print("\nПример 2:")
    for i in num_generator(123, 13):
        print(i)


def num_generator(max_num, start_num=3):
    """Генератор нечетных чисел ждя задачи №1"""
    current = start_num - 1
    while current < max_num:
        current += 1
        if current % 2:
            yield current


# Есть два списка. Необходимо реализовать генератор.
def task_three():
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses2 = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б'
    ]
    print("\nПример 1:")
    for i in tuple_generator(tutors, klasses):
        print(i)
        print(type(i))
    print("\nПример 2:")
    for i in tuple_generator(tutors, klasses2):
        print(i)
        print(type(i))

    # Доказать, что вы создали именно генератор.
    generator = tuple_generator(['Дмитрий', 'Борис', 'Елена'],
                                ['9Б', '9В'])
    print("\nДоказать, что вы создали именно генератор:")
    print(type(generator))
    # Проверить его работу вплоть до истощения.
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))


def tuple_generator(tutors, klasses):
    """Генератор для задачи №3, возвращающий кортежи вида (<tutor>, <klass>)"""
    for tutor in tutors:
        try:
            yield tutor, klasses[tutors.index(tutor)]
        except IndexError:
            yield tutor, None


# 4. Представлен список чисел. Dывести те его элементы,
# значения которых больше предыдущего:
def task_four():
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    # resul = [12, 44, 4, 10, 78, 123]
    return [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]


# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования
# в исходном списке:
def task_five():
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    # result = [23, 1, 3, 10, 4, 11]
    return [src[i] for i in range(len(src)) if src.count(src[i]) == 1]
    # return tuple(src[i] for i in range(len(src)) if src.count(src[i]) == 1)


if __name__ == '__main__':
    print("\nЗадача № 1:")
    task_one()
    print("****\nЗадача № 3:")
    task_three()
    print("****\nЗадача № 5:")
    print(task_five())
    print("****\nЗадача № 4:")
    print(task_four())
