def statement_generator(statement, decoration):
    middle = f'{decoration.upper() * 3} | {statement} | {decoration.upper() * 3}'
    top_bottom = decoration.upper() * len(middle)

    print(top_bottom)
    print(middle)
    print(top_bottom)


statement_generator("This is a rather decorated text", "*")
print("Director: Daniel holmes\nCamera effects: Nobody\nSound director: Nobody")
