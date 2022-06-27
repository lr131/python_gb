from itertools import islice


FILENAME = "bakery.csv"


def add_sale(sum):
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(sum+"\n")


def show_sale(startline=1, stopline=None):
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = islice(file, startline - 1, stopline, None)
        for line in lines:
            print(line)

