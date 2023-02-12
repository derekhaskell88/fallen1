# Derek Haskell validation file for the Future Value App
def get_float(prompt, low, high):  # defining the get float function
    while True:  # setting up infinate loop
        number = float(input(prompt))  # setting number variable
        if number > low and number <= high:  # rules for get float function
            return number  # return the number and coninue if true
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)  # this will run if entry is invalid


def get_int(prompt, low, high):  # defining the get int function
    while True:  # setting up infinate loop
        number = float(input(prompt))  # setting the number variable
        if number > low and number <= high:  # rules for get int function
            return number  # return number and if true continue
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)  # this will run if entry is invalid


def main():  # defining main function
    choice = "y"  # variable for while loop
    while choice.lower() == "y":  # starting while loop
        # valid range for get float function
        valid_number = get_float("Enter number:", 0, 1000)
        print("Valid number = ", valid_number)  # display valid number
        print()
        # valid range for get int function
        valid_integer = get_int("Enter integer: ", 0, 50)
        print("Valid integer = ", valid_integer)  # display valid integer
        print()
        choice = input("Repeat? (y/n): ")  # ask user if they want to continue
    print()
    print("Bye!")  # goodbye message


if __name__ == "__main__":  # code needed at the bottom so the main function will execute
    main()
