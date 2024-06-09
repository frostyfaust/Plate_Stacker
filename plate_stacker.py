# Create list for plates
plates = []

# prints chosen section for UI
def chosen_option_ui(prompt):
    option_string = prompt
    print("=" * 26)
    print(f"*{option_string:^24}*")
    print("=" * 26)

# Add plate function
def add_a_plate():
    chosen_option_ui("Add a plate")
    if plates == []: # checks if list is empty and tells user
        print("There are currently no plates.")
    else:
        print(f"Current plate size is {plates[-1]}.")
    plate_number = read_user_input("Enter desired plate size: ")
    if not plates == []: # checks that input is positive and appropriate size
        while plate_number <= 0 or plate_number > plates[-1]:
            print("must be positive integer & smaller or equal to current plate size.")
            print(f"current plate size: {plates[-1]}")
            plate_number = read_user_input("Enter desired plate size: ")
    plates.append(plate_number)
    print("Plate successfully added.")

# Displaying plates function
def display_all_plates():
    chosen_option_ui("Printing plate(s)")
    if plates == []:
        print("There are no plates to print.")
    for i in reversed(plates):
        plate_number = "= " * i
        print(f"{plate_number:^26}")
    print("") 


# Remove plate function
def remove_plate():
    if plates == []:
        print("There are currently no plates to remove.")
        return
    chosen_option_ui("Removing plate(s)")
    print(f"There are currently {len(plates)} plate(s).")
    remove_num = read_user_input("How many plates would you like to remove from the stack?: ")
    if remove_num <= 0:
        print(f"Number must be positive.")
    elif remove_num > len(plates):
        print(f"Can't remove more than {len(plates)} plates.")
    else:
        while remove_num != 0:
            plates.pop()
            remove_num -= 1
        print("Successfully removed plate(s).")

# Read input function
def read_user_input(prompt):
    value = ""
    while not value or value.isalpha():
        value = input(prompt).strip()
        if not value or value.isalpha():
            print("Error: invalid response.")
    value = int(value) # converts user input into an integer
    return value

main_menu = "Main Menu"
option_1 = "1. Exit"
option_2 = "2. Add a plate"
option_3 = "3. Print plate(s)"
option_4 = "4. Remove plate(s)"

# displays plate stacker main menu for user
def display_menu():
    print("=" * 26)
    print(f"*{main_menu:^24}*")
    print("=" * 26)
    print(f"||{option_1:<22}||")
    print(f"||{option_2:<22}||")
    print(f"||{option_3:<22}||")
    print(f"||{option_4:<22}||")
    print("=" * 26)

def run():
    print("")
    print("Welcome to Epic Plate Stacker!")
    print("")
    option = ""
    while option != 1:
        display_menu()
        option = read_user_input("Please select option [1-4]: ")
        match option:
            case 1:
                print("Goodbye.")
            case 2:
                add_a_plate()
            case 3:
                display_all_plates()
            case 4:
                remove_plate()
            case _:
                print ("Not a valid reponse.")

run()


            