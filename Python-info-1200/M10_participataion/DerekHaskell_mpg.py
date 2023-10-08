#!/usr/bin/env python3

import csv  # import csv module for r-w ability

FILE_NAME = "trips.csv"  # sets trips.csv for access


def write_trips(trips):  # define write_trips function
    """writes trips to csv file

    Args:
        trips (csv): stores data
    """
    with open(FILE_NAME, "w", newline="") as output_file:  # opens file in write mode
        writer = csv.writer(output_file)  # writes to csv
        writer.writerows(trips)  # write rows for each trip


def read_trips():  # define read_trips function
    """reads trips from csv

    Returns:
        list: trip info
    """
    trips = []  # make trips a list
    with open(FILE_NAME, "r", newline="") as input_file:  # opens csv file in read mode
        reader = csv.reader(input_file)  # reads from csv
        for row in reader:  # iderates through rows in reader
            trips.append(row)  # appens info to trips list
    return trips  # returns trips list


def list_trips(trips):  # defines list_trips function
    """displays trips on console

    Args:
        trips (csv): stores trips in list
    """
    print("Distance\tGallons\t\tMPG")  # lists fields for list
    for i in range(0, len(trips)):  # iderates through trips starting at 0
        trip = trips[i]  # sets trip equal to a single trip as it iderates
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")  # displays single trips


def get_miles_driven():  # define get_miles_driven function
    """gets user input for miles driven

    Returns:
        float: user input
    """
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:  # starting while loop
        # displays if entry is less than or equal to zero
        print("Entry must be greater than zero. Please try again.\n")
    return miles_driven  # return miles driven


def get_gallons_used():  # define get_gallons_used function
    """gets user input for gallons used

    Returns:
        float: gallons used
    """
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:  # start while loop get user input as float
        # display error message
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used  # return gallons used


def main():  # defining main function
    """main function
    """
    # display a welcome message
    print("Derek Haskell's Miles Per Gallon program")
    print()
    trips = []  # making trips a list

    more = "y"  # more to string var y
    while more.lower() == "y":  # start while loop
        miles_driven = get_miles_driven()  # calls get_miles_driven function
        gallons_used = get_gallons_used()  # calls get_gallons_used function

        mpg = round((miles_driven / gallons_used), 2)  # calculate mpg
        print(f"Miles Per Gallon:\t{mpg}")  # display mpg
        print()

        # setting fields in list for single trip
        single_trip = [miles_driven, gallons_used, mpg]
        trips.append(single_trip)  # append single trip to trips
        write_trips(trips)  # calls write trips function with trips
        trips = read_trips()  # calls read trips function
        # calls list trips function with trips as a parameter
        list_trips(trips)

        # see if user wants to continue
        more = input("More entries? (y or n): ")

    print("Bye!")  # goodbye message


if __name__ == "__main__":  # if main is there run main function as main
    main()  # calls main function
