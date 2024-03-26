def statement_generator(statement, decoration, dec_mode=1):

    middle = f'{decoration.upper() * 3} | {statement} | {decoration.upper() * 3}'
    top_bottom = decoration.upper() * len(middle)

    print(top_bottom)
    print(middle if dec_mode == 1 else 6 * " " + statement)
    print(top_bottom)


statement_generator("This is a rather decorated text", "*", 2)
print()
statement_generator("I'm a dead flower", "^", 2)
print()
statement_generator("I'm a pretty little mud ball", "@", 1)
print("Director: Daniel holmes\nCamera effects: The Blind girl\nSound director: Dr. Deaf man")
