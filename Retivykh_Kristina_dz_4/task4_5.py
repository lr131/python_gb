from utils import currency_rates_adv

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        result = currency_rates_adv(sys.argv[1])
        print(f'{result.get("value")}, '
              f'{result.get("date").strftime("%Y-%m-%d")}')
