#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This program helps grandma decide if uer is allowed to date her grandchild


def main():
    # This program helps grandma decide if uer is allowed to date her grandchild
    user_age = input("Please enter your age : ")

    try:
        # input
        user_age = int(user_age)
        # process and output
        if user_age > 25 and user_age < 40:
            print("You have been accepted to date my grandchild.")
        elif user_age > 40:
            print("Sorry, you are too old!")
        else:
            print("Sorry, you are too young!")
    except Exception:
        print("Not a valid age.")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
