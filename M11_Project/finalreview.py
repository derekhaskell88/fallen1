
import csv
FILENAME = "review.csv"


def main():

    welcome_message()
    valid_int()
    csv_file()


def welcome_message():
    print("welcome to valid int and list apps")


def valid_int():
    while True:
        try:
            number = int(input("Enter number between 1 and 10---"))
        except Exception as e:
            print(e)
        if number < 1 or number > 10:
            print("please try again")
            continue
        else:
            print("you entered a valid number! ", number)
            break


def csv_file():
    killers = [["pinhead"], ["michael", "freddy"],
               ["billy"], ["nurse"], ["trapper"]]

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerows(killers)


if __name__ == "__main__":
    main()
