def print_center(string):
    position = 40 - len(string) // 2
    print(' ' * position, string)


def separator():
    print('-'*80)

def format_coin(value, coin="R$"):
    formatted_string = coin + ' ' + value
    return formatted_string
