import re


def email_parse(email_address):
    regexp = re.compile(r'\b([\w]+)@(\w+\.[a-zA-Z]+)\b')
    email_match = regexp.match(email_address)
    if email_match:
        print("000")
        return {"user_name": email_match[1],
                "mail_domain" :email_match[2]}
    raise ValueError(f'wrong email: {email_address}')


def task_one():
    print(email_parse('someone@geekbrains.ru'))
    #print(email_parse('someone@geekbrainsru'))


def type_logger(func):
    def wrapper(args):
        res = func(args)
        return f'{args}: {type(args)}'
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


def task_three():
    a = calc_cube(5)
    print(a)


if __name__ == '__main__':
    task_one()
    task_three()
