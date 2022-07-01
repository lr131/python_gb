import os
from pprint import pprint

import starter
from starter import STRUCTURE_ONE, STRUCTURE_TWO, FILE_CONFIG_ONE,\
    FILE_CONFIG_TWO, init_yaml
from templater import templater
from statistic import get_stat


def task_one():
    init_yaml(STRUCTURE_ONE, FILE_CONFIG_ONE)
    starter.task_one()


def task_two():
    init_yaml(STRUCTURE_TWO, FILE_CONFIG_TWO)
    starter.task_two()


def task_three():
    templater()


def task_four():
    pprint(get_stat(os.curdir))


if __name__ == '__main__':
    task_one()
    task_two()
    task_three()
    task_four()
