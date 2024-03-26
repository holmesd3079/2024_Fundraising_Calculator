import math


def currency(x, ceil=None):
    if ceil:
        x = math.ceil(x)
    return f"${format(x, '.2f')}"


print(currency(1))
