def not_blank(question, err="This is blank, please enter real characters"):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print(err)


not_blank("What is your IP address")
