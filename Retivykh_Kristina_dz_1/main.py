# 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
def task_one():
    minute = 60
    hour = minute * 60
    day = hour * 24

    duration = int(input("Введите целое значение duration: "))

    if duration < minute:
        result = f"{duration} сек"
    elif duration < hour:
        minutes = duration // minute
        seconds = duration % minute
        result = f"{minutes} мин {seconds} сек"
    elif duration < day:
        hours = duration // hour
        minutes = duration % hour // minute
        seconds = duration % hour % minute
        result = f"{hours} час {minutes} мин {seconds} сек"
    else:
        days = duration // day
        hours = duration % day // hour
        minutes = duration % hour // minute
        seconds = duration % hour % minute
        result = f"{days} дн {hours} час {minutes} мин {seconds} сек"

    print(result)


def get_sum_of_digit(element):
    element_sum = 0
    rank = 1
    while element // rank != 0:
        rank = rank * 10
        dizit = element % rank // (rank / 10)
        element_sum = element_sum + dizit
    return element_sum


# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):
def task_two():
    result_lst = []
    result_variant_a = 0
    result_variant_b = 0

    for i in range(1, 1001):
        element = i ** 3
        result_lst.append(element)
        element_sum = get_sum_of_digit(element)
        element_sum_b = get_sum_of_digit(element + 17)
        if not element_sum % 7:
            result_variant_a = result_variant_a + element
        if not element_sum_b % 7:
            result_variant_b = result_variant_b + element + 17

    print("Сумма чисел из списка, сумма цифр которых делится нацело на 7: ",
          result_variant_a)
    print("Сумма чисел из списка, сумма цифр которых делится нацело на 7, "
          + "после добавления числа 17  к каждому элементу списка: ",
          result_variant_b)


# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел
# в интервале от 1 до 100:
def task_three():
    word = "процент"
    for i in range(1, 101):
        if (i % 10 == 1) and (i != 11):
            print(i, word)
        elif (i % 10 > 1) and (i % 10 < 5) and (i not in [12, 13, 14]):
            print(i, f"{word}а")
        else:
            print(i, f"{word}ов")


if __name__ == '__main__':
    task_one()
    task_two()
    task_three()
