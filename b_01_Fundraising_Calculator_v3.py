import math
import pandas
from datetime import date


def currency(x, ceil=None):
    if ceil:
        x = math.ceil(x)
    return f"${format(x, '.2f')}"


def not_blank(question, err="This is blank, please enter real characters"):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print(err)


def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


def int_check(question, low_num=None, high_num=None, exit_code=None, n_type=int):
    situation = ""

    if low_num is not None and high_num is not None:
        situation = "both"
        error_msg = f"Please enter a number between {low_num} and {high_num}"
    elif low_num is not None and high_num is None:
        situation = "low only"
        error_msg = f"Please enter a number that is more than (or equal to) {low_num}"
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
                if response < low_num:
                    print(error_msg)
                    continue

            return response

        except ValueError:

            print(error_msg)


def choice_checker(question, chosen_valid=("yes", "no"), error="Pick yes or no", skip_char=1):
    while True:
        response = input(question).lower()

        # Loop through list of valid with the input
        for item in chosen_valid:
            if response == item[:skip_char] or response == item:
                # Return matched valid
                return item

        print(error)


def statement_generator(statement, decoration, dec_mode=1):
    middle = f'{decoration.upper() * 3} | {statement} | {decoration.upper() * 3}'
    top_bottom = decoration.upper() * len(middle)

    print(top_bottom)
    print(middle if dec_mode == 1 else 6 * " " + statement)
    print(top_bottom)

    return f"{top_bottom}\n{middle}\n{top_bottom}"


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
            amount = (amount / 100) * total_costs
        return amount


def get_expenses(var_fixed):
    item_list, quantity_list, price_list = [], [], []
    item_name = ""
    var_dict = None
    item_count = 0
    while item_name.lower() != "xxx":

        item_name = not_blank("Item name: ")
        if item_name.lower() == "xxx":
            if item_count == 0:
                print("You must by the least buy something before quiting")
                item_name = ""
                continue
            break

        if var_fixed == "variable":
            var_dict = {
                "Item": item_list,
                "Quantity": quantity_list,
                "Price": price_list
            }
            quantity = int_check("Quantity: ˣ", 0)
        else:
            var_dict = {
                "Item": item_list,
                "Price": price_list
            }
            quantity = 1

        price = int_check("Price per item: $", 0, n_type=float)

        total_item_cost = currency(quantity * price)
        print(f"{item_name}ˣ{quantity} | Total:", total_item_cost)
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)
        print("\n--")
        item_count += 1
    var_frame = pandas.DataFrame(var_dict)
    var_frame = var_frame.set_index('Item')

    var_frame["Cost"] = (var_frame["Quantity"] * var_frame["Price"] if var_fixed == "variable" else var_frame["Price"])
    sub_total = var_frame["Cost"].sum()

    add_dollars = ["Price", "Cost"]

    for item in add_dollars:
        var_frame[item] = var_frame[item].apply(currency)
    return [var_frame, sub_total]


print("🧮 Instructions 🧮\n"
      "-- Starting off --\n-Put insert Product Name\n- Insert the amount of items you will be producing\n"
      "\nInsert your item/stock amounts and prices"
      "\nIf you have fixed costs (e,g; Rent/Building/Stalls) Having 1 and only paying it once, say yes to fixed costs."
      "\nNow the program will do all the work"
      if choice_checker("Do you want to see the instructions? ") == "yes" else "")

# MAIN ROUTINE ---

# Gather variable costs & product name and set values after user inputs
print(5 * "*", "Variable Costs", 5 * "*")
product_name = not_blank("What is your product name: ")
how_many = int_check("How many items will you be producing?", 1)

var_expenses = get_expenses("variable")
var_exp_frame = var_expenses[0]
var_exp_sub_total = var_expenses[1]
print()

# Gather fixed costs/prices
fix_exp_sub_total = 0
fixed_costs_print = ""
if choice_checker("Do you have Fixed costs? (y / n)?") == "yes":
    print(3 * "\n")
    statement_generator("Fixed Costs", "*", 2)
    fix_expenses = get_expenses("fixed")
    fix_exp_frame = fix_expenses[0]
    fix_exp_sub_total = fix_expenses[1]
    fixed_costs_print = 3 * "-" + " Fixed costs " + 3 * "-" + "\n\n" \
                                                              f"{fix_exp_frame}\n" \
                                                              f"--\nfixed costs: {currency(fix_exp_sub_total)}"

# Gather today's date for file name and information
today = date.today()
write_date = f"{today.day}/{today.month}/{today.year}"
sh_date = f"{today.day}_{today.month}_{today.year}"
filename = f"FC_{sh_date}"

# Calculate money
all_costs = var_exp_sub_total + fix_exp_sub_total
profit_targ = profit_goal(all_costs)

sales_needed = all_costs + profit_targ
round_to = int_check("Round to nearest...", 1)

selling_price = sales_needed / how_many
print(f"Selling price (unrounded): {selling_price}")

recommended_price = round_up(selling_price, round_to)


# What is going to the file & along with print
to_save = (
    f"{statement_generator(product_name, '=')} {sh_date}"
    f"\n\n--- Variable costs ---\n\n{var_exp_frame}\n---\nVar costs: {currency(var_exp_sub_total)}\n\n"
    f"{fixed_costs_print}"
    f"\n\nProfit Target: {currency(profit_targ)}\n"
    f"Total sales {currency(all_costs + profit_targ, 1)}\n"
    f"Minimum price {currency(selling_price)} | Recommended price: {currency(recommended_price)}"
)
# Print all items before saving items to file
print(to_save)

# Create and edit file
text_file = open(f"{filename}.txt", "w+")
text_file.write(to_save)
text_file.close()
