import re

from functools import wraps


def email_parse(email_address):
    regexp = re.compile(r'\b([\w.-]+)@(?:[A-Za-z0-9]+[\w-]*\.[A-Za-z]{2,6})\b')
    email_match = regexp.match(email_address)
    print(email_match)
    if email_match:
        return {"user_name": email_match[1],
                "mail_domain": email_match[2]}
    raise ValueError(f'wrong email: {email_address}')


def task_one():
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        args_print_list = tuple(map(lambda x: f'{x}: {type(x)}', args))
        kwargs_print_list = (f'{k}: {v} / type({v}) - {type(v)}' for k, v in
                             kwargs.items())

        import platform
        import re
        regexp = re.compile(r"\d+.\d+")
        python_version_str = platform.python_version()
        python_ver = float(regexp.match(python_version_str)[0])

        if python_ver >= 3.6:
            # такая распаковка доступна только в Python 3.6+
            res_wrapper = [*args_print_list, *kwargs_print_list]
        else:
            res_wrapper = list(args_print_list) + list(kwargs_print_list)

        res_wrapper_str = ", ".join(res_wrapper) if len(res_wrapper) else ""
        print(f'{func.__name__}({res_wrapper_str})\n'
              f'Result {func.__name__} type: {type(res)}')
        return res

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_cubes(*args):
    return tuple(map(lambda x: x ** 3, args))


@type_logger
def push_something(**kwargs):
    return "&".join(tuple(map((lambda key: f'{key}={kwargs[key]}'), kwargs)))


def task_three():
    a = calc_cube(5)
    print('\nЭто уже task_three: ', a, "function name = ", calc_cube.__name__)
    a = calc_cubes(5, 3, 2, 1)
    print('\nЭто уже task_three:: ', a, "function name = ", calc_cube.__name__)
    b = push_something(Abba="Happy_New_Year",
                       Nigthwish="Wishmaster",
                       Kamelot="Karma",
                       Lacrimosa="Seele_in_not",
                       Scorpions="Humanity",
                       Louna=("Весна", "Мама", "Путь_к_себе"),
                       Oomph="Labyrinth")
    print('\nЭто уже task_three:: ', b, "function name = ",
          push_something.__name__)


def val_checker(validate):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            valid = tuple(map(validate, args))
            if False in valid:
                raise ValueError(f'wrong value: {args[valid.index(False)]}')
            result = func(*args)
            return result

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube_4(x):
    return x ** 3


@val_checker(lambda x: x > 0)
def calc_cubes_4(*args):
    return tuple(map(lambda x: x ** 3, args))


def task_four():
    print(calc_cube_4(5))
    print(calc_cube_4(-5))
    print(calc_cubes_4(5, 1, 2))
    print(calc_cubes_4(5, 2, 8, -7, 4))


if __name__ == '__main__':
    # task_one()
    task_three()
    # task_four()
