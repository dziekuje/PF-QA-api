# https://docs.python.org/3/library/argparse.html

import argparse

parser = argparse.ArgumentParser()


parser.add_argument('--method', '-m',
                    action='store',
                    help='Method to make request',
                    default='GET')

parser.add_argument('--url', '-u',
                    action='store',
                    help='Url to make request to',
                    required=True)

# Если параметр передан то True, иначе False
parser.add_argument('--true', '-t',
                    action='store_true',
                    help='True or false param',
                    required=False)

# Добавляение значений в список по параметру
# python3 2_argparse_method.py --url=interia.pl -s
parser.add_argument('--save', '-s',
                    action='append_const',
                    const='const_to_save',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

# Добавляение значений в список по параметру
# python3 2_argparse_method.py --url=interia.pl -s -s2
parser.add_argument('--save2', '-s2',
                    action='append_const',
                    const='const_to_save2',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

# Парсим всё что положили
args = parser.parse_args()

# Это словарь из которого аргументы можно доставать
print(args)
