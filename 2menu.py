options = ["Option 1", "Option 2", "Option 3", "Quit"]


while True:
    print("\nMenu:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    # Get user input and handle it
    try:
        choice = int(input("Enter your choice: "))
        if choice == len(options):
            break
        elif 1 <= choice <= len(options)-1:
            print(f"You chose {options[choice-1]}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")
        