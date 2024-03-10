import pandas


def currency(x):
    return f"${format(x, '.2f')}"


def not_blank(question, err="This is blank, please enter real characters"):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print(err)


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


item_list, quantity_list, price_list = [], [], []
var_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

print("🧮 Instructions 🧮" if choice_checker("Do you want to see the instructions? ") == "yes" else "")

item_name = ""

product_name = not_blank("What is your product name: ")

while item_name.lower() != "xxx":

    item_name = not_blank("Item name: ")
    if item_name.lower() == "xxx":
        break

    quantity = int_check("Quantity: $", 0)
    price = int_check("Price per item: $", 0, n_type=float)

    total_item_cost = currency(quantity * price)
    print("The price in total is", total_item_cost)
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

var_frame = pandas.DataFrame(var_dict)
var_frame = var_frame.set_index('Item')

var_frame["Cost"] = var_frame["Quantity"] * var_frame["Price"]
var_sub = var_frame["Cost"].sum()

add_dollars = ["Price", "Cost"]

for item in add_dollars:
    var_frame[item] = var_frame[item].apply(currency)

print(var_frame)
print(f"Var costs: {currency(var_sub)}")
