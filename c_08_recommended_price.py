import math


def int_check(question, low_num=None, high_num=None, exit_code=None, n_type=int):
    situation = ""

    if low_num is not None and high_num is not None:
        situation = "both"
        error_msg = f"Please enter a number between {low_num} and {high_num}"
    elif low_num is not None and high_num is None:
        situation = "low only"
        error_msg = f"Please enter a number that is more than {low_num}"
    else:
        error_msg = "Please enter a number"

    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            response = n_type(response)

            if situation == "both":

                if response < low_num or response > high_num:
                    print(error_msg)

                    continue

            elif situation == "low only":
                if response <= low_num:
                    print(error_msg)
                    continue

            return response

        except ValueError:

            print(error_msg)


def currency(x, ceil=None):
    if ceil:
        x = math.ceil(x)
    return f"${format(x, '.2f')}"


def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


how_many = int_check("How many items?", 0)
total = int_check("Total costs?", 0, n_type=float)
prof_goal = int_check("Profit Goal?", 0, n_type=float)
rnd_to = int_check("Round to nearest...?", 0)

sales_needed = total + prof_goal

print(f"Total: {currency(total)}\n"
      f"Profit Goal: {prof_goal}")

selling_price = sales_needed/how_many
print(f"Selling price (un-rounded): {currency(selling_price)}")

recommended_price = round_up(selling_price, rnd_to)
print(f"Recommended price {currency(recommended_price)}")
