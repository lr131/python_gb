import re


def email_parse(email_address):
    regexp = re.compile(r'\b([\w]+)@(\w+\.[a-zA-Z]+)\b')
    email_match = regexp.match(email_address)
    if email_match:
        print("000")
        return {"user_name": email_match[1],
                "mail_domain": email_match[2]}
    raise ValueError(f'wrong email: {email_address}')


def task_one():
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))


def type_logger(func):
    def wrapper(*args):
        res = func(*args)
        args_str = ", ".join(tuple(map(lambda x: f'{x}: {type(x)}', args)))
        print(f'{func.__name__}({args_str})\n'
              f'Result {func.__name__} type: {type(res)}')
        return res

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_cubes(*args):
    return tuple(map(lambda x: x ** 3, args))


def task_three():
    a = calc_cube(5)
    print('result task_three: ', a)
    a = calc_cubes(5, 3, 2, 1)
    print('result task_three: ', a)


def val_checker(validate):
    def _val_checker(func):
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
    # task_three()
    task_four()
