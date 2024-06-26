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


my_number = int_check("n", 0, None, "xxx", float)
print(my_number)


