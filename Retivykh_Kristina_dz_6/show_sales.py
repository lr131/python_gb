import sys

import utils_bakery


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 3:
        utils_bakery.show_sale(int(args[1]), int(args[2]))
    elif len(args) == 2:
        utils_bakery.show_sale(int(args[1]))
    else:
        utils_bakery.show_sale()