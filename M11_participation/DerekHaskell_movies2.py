import csv  # import csv module
import sys  # import sys module

FILENAME = "movies1.csv"  # setting file name for csv file


def exit_program():  # define exit program function
    """exits program
    """
    print("Terminating program.")  # exit message
    sys.exit()  # run exit function


def read_movies():  # define read movies function
    """read moview from csv file

    Returns:
        string: movies list
    """
    try:  # tries user input to catch exceptions
        movies = []  # setting movies equal to an empty list
        with open(FILENAME, newline="") as file:  # open file perform action then close
            reader = csv.reader(file)  # reader tool to read the csv file
            for row in reader:  # iterate through the rows
                movies.append(row)  # append the row to movies list
        return movies  # returns movies to list
    except FileNotFoundError as e:  # specific exception error
        # print(f"Could not find {FILENAME} file.")
        # exit_program()
        return movies  # returns movies
    except Exception as e:  # checks for specific exception
        # print the type of error message for e as defined before
        print(type(e), e)
        exit_program()  # calls exit program function


def write_movies(movies):  # define write moview function
    """writes to csv file from list

    Args:
        movies (list): updated list
    """
    try:  # tries operation
        # opens file to perform an action then closes file
        with open(FILENAME, "w", newline="") as file:
            # raise BlockingIOError("Test the OSError exception")
            writer = csv.writer(file)  # writing tool
            # writes rows to movies list from csv file
            writer.writerows(movies)
    except OSError as o:  # checks for specific exception error
        print(type(o), o)  # displays specific error type
    except Exception as e:  # checks for exception
        print(type(e), e)  # prints specific error type
        exit_program()  # exits app


def list_movies(movies):  # define list movies function
    """lists movies if user enters list command

    Args:
        movies (list): movies
    """
    for i, movie in enumerate(movies, start=1):  # iderates through movies list
        print(f"{i}. {movie[0]} ({movie[1]})")  # displays each row of list
    print()


def add_movie(movies):  # add movies
    """adds movies from user input

    Args:
        movies (input): string
    """

    name = input("Name: ")  # get user input
    while True:  # start infinate loop
        try:  # tries input
            year = int(input("Year: "))  # get input
        except ValueError:  # checks for specific error
            print("Invalid year")  # invalid message
            continue  # continues to top of loop if invalid input
        if year <= 0:  # checks for valid input
            print("Invalid year")  # invalid message
            continue  # continue to top of loop
        else:  # if valid
            break  # breaks out of while loop

    movie = [name, year]  # adding list to list
    movies.append(movie)  # appends movie to list
    # calls write movies function with movies as a parameter
    write_movies(movies)
    print(f"{name} was added.\n")  # displays name as a field


def delete_movie(movies):  # define delete movie function
    while True:  # start infinate loop
        try:  # tries to catch error
            number = int(input("Number: "))  # get user input as int
        except ValueError:  # check for specific error
            # invalid error message
            print("Invalid integer. Please try again.")
            continue  # continue to top of loop
        if number < 1 or number > len(movies):  # checks for valid input
            # invalid message
            print("There is no movie with that number. Please try again.")
        else:  # if valid
            break  # break out of while loop
    movie = movies.pop(number - 1)  # delete movie
    # calls write movies function with movies as a parameter
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")  # displays the movie that was deleted


def display_menu():  # define display menu function
    """displays menu
    """
    print("The Movie List program")  # title
    print()
    print("COMMAND MENU")  # command menu title
    # list of available commands and what they do
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()


def main():  # define main function
    """main function
    """
    display_menu()  # call display menu function
    movies = read_movies()  # calls read movies function sets equal to movies list
    while True:  # start infinate loop
        command = input("Command: ")  # get user input
        if command.lower() == "list":  # runs if user types list
            list_movies(movies)  # calls list movies function
        elif command.lower() == "add":  # runs if input is add
            add_movie(movies)  # calls add movie function
        elif command.lower() == "del":  # funs if input del
            delete_movie(movies)  # calls del movie function
        elif command.lower() == "exit":  # if input exit
            break  # breaks out of app closes it down
        else:  # if invalid command
            print("Not a valid command. Please try again.\n")  # invalid message
    print("Bye!")  # goodbye message


if __name__ == "__main__":  # if name is present
    main()  # run main
