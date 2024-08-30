#need_error_handling
#produce_random_number_between1-1000
#user_guess_higher_or_lower

import random

ran_number= (random.randrange(1, 1000, 1))
print("A random number from range is : ", ran_number)


def gameplay():
    try:
        user_guess = int(input("Guess number between 1 and 1000: "))
        if user_guess/2 == 1:
            print("")
    except:
        print("bad input only ints")
        user_guess = int(input("Guess number between 1 and 1000: "))


    while True:
        if user_guess == ran_number:
            print("correct")
            break

        else:
            print("incorrect")

        if user_guess > ran_number:
            print("lower")

        if user_guess < ran_number:
            print("higher")

        if user_guess != ran_number:
            user_guess = int(input("Guess Again: "))

gameplay()