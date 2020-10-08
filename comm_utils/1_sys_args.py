import sys

print(sys.argv)
args = sys.argv


def sum_args(num1, num2):
    return int(num1) + int(num2)


print(sum_args(args[1], args[2]))