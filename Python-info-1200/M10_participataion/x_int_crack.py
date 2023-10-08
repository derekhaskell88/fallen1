
import math


def main():
    # get_y()
    # get_range()
    get_intercept()


def get_range():
    for i in range(0, 100000):
        x = round(i/10000-10, 4)
        # x1 = round(i/10000, 4)
        print(x)


def get_y():

    a = float(input("a"))
    b = float(input("b"))
    c = float(input("c"))
    d = float(input("d"))
    x = float(input("x"))
    y = round((a*(x**3))+(b*(x**2))+(c*x)+d, 1)
    print(y)


def get_intercept():

    a = float(input("a"))
    b = float(input("b"))
    c = float(input("c"))
    d = float(input("d"))
    x = 0
    for i in range(0, 100000):
        x = round(i/10000, 4)
        x1 = round(i/10000*-1, 4)
        y = round((a*(x**3))+(b*(x**2))+(c*x)+d, 3)
        y1 = round((a*(x1**3))+(b*(x1**2))+(c*x1)+d, 2)

        if y == 0:
            print("x=", x)
        elif y1 == 0:
            print("x1", x1)


if __name__ == "__main__":
    main()
