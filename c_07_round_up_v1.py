import math


def currency(x, ceil=None):
    if ceil:
        x = math.ceil(x)
    return f"${format(x, '.2f')}"


def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


to_round = [2.75, 2.25, 2]

for item in to_round:
    rounded = round_up(item, 1)
    print(f"{currency(item)} --> {rounded}")