import math


def choice_checker(question, chosen_valid=("yes", "no"), error="Pick yes or no", skip_char=1):
    while True:
        response = input(question).lower()

        # Loop through list of valid with the input
        for item in chosen_valid:
            if response == item[:skip_char] or response == item:
                # Return matched valid
                return item

        print(error)


def currency(x, ceil=None):
    if ceil:
        x = math.ceil(x)
    return f"${format(x, '.2f')}"


def profit_goal(total_costs):
    err = "Please enter a valid profit goal\n"

    while True:
        response = input("What is your profit goal (e.g; $500 or 50%): ")
        if not response:
            continue
        # Simplify, sort and breakup and set values based off response
        if response[0] == "$":
            profit_type = "$"
            amount = response[1:]

        elif response[-1] == "%":
            profit_type = "%"
            amount = response[:-1]
        else:
            profit_type = "unknown"
            amount = response

        try:
            amount = float(amount)
            if amount <= 0:
                print(err)
                continue
        except ValueError:
            print(err)
            continue
        # Code shortened heavily because it was giant. ("yes" if 2 == 2 else "no") would be "yes"
        if profit_type == "unknown" and amount >= 100:
            profit_type = ("$" if choice_checker(f"Did you mean {currency(amount)} ") == "yes" else "%")
        elif profit_type == "unknown" and amount <= 100:
            profit_type = ("%" if choice_checker(f"Did you mean {amount}% ") == "yes" else "$")

        if profit_type == "%":
            amount = (amount/100) * total_costs
        return amount


all_cost = 200

for item in range(0, 6):
    profit_targ = profit_goal(all_cost)
    print(f"Profit Target: {currency(profit_targ)}\n"
          f"Total sales {currency(all_cost + profit_targ, 1)}")
