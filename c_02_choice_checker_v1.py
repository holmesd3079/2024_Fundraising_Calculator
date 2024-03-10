# Choice checker/Default to yes_no checker if only Question is inputted
def choice_checker(question, chosen_valid=("yes", "no"), error="Pick yes or no", skip_char=1):
    while True:
        response = input(question).lower()

        # Loop through list of valid with the input
        for item in chosen_valid:
            if response == item[:skip_char] or response == item:
                # Return matched valid
                return item

        print(error)


while True:
    if choice_checker("Do you want instructions") == "yes":
        print("{Instructions}")

    print("Continues...")
