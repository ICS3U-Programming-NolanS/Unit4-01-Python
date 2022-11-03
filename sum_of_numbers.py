#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: November 2nd, 2022
# This program tells the user to enter a positive number
# and then calculate and display the sum of all numbers,
# from 0 to that given number, through using a loop.


def main():
    # set the sum and the loop counter
    loop_counter = 0
    sum = 0

    # get the user number as a string
    user_number_as_string = input("Enter a positive integer: ")
    print("")

    # try catch to check for erroneous data
    try:

        # turns input into an integer
        user_number = int(user_number_as_string)

        # if statement to check if input is a positive integer
        if user_number < 0:
            print("\n" + user_number + " is not a positive integer.")
        elif user_number == 0:
            print(" 0 is not a positive integer.")
        else:
            # calculate the sum of all numbers from 0 to user number
            while loop_counter <= user_number:
                sum = sum + loop_counter
                print("\nTracking {0} times through a loop.".format(loop_counter))
                loop_counter = loop_counter + 1
            print(
                "\nThe sum of the numbers from 0 to {} is: {}.".format(user_number, sum)
            )

    # exception if user input is not an integer
    except Exception:
        print("This is not a positive integer...please enter a valid number.")

    # ending message
    finally:
        print("\nThank you for enjoying this wonderful video game!")


if __name__ == "__main__":
    main()
