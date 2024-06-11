# Create list for plates
plates = []

# Global variables
main_menu = "Main Menu"
option_1 = "1. Exit"
option_2 = "2. Add a plate"
option_3 = "3. Print plate(s)"
option_4 = "4. Remove plate(s)"
exit_display = "1. Exit to Main Menu"
plate_list = "2. List of the plates."
vertical_display = "3. Vertically stacked"

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
    while plate_number <= 0: # checks that input is positive
        print("Must be a positive integer.")
        plate_number = read_user_input("Enter desired plate size: ")
    while plates and plate_number > plates[-1]: # checks that input is appropriate size
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
    display_choice = ""
    while display_choice != 1:
        print_plate_menu() # Displays printing plate menu
        display_choice = read_user_input("How do you want to display your plates? [1-3]: ")
        match display_choice:
            case 1:
                return
            case 2:
                print(plates)
            case 3:
                for i in reversed(plates):
                    plate_number = "= " * i
                    print(f"{plate_number:^26}")
            case _:
                print("Invalid option.")
    
    print("") 


# Remove plate function
def remove_plate():
    if plates == []:
        print("There are currently no plates to remove.")
        return
    chosen_option_ui("Removing plate(s)")
    print(f"There are currently {len(plates)} plate(s).")
    remove_num = read_user_input("How many plates would you like to remove from the stack?: ")
    while remove_num <=0 or remove_num > len(plates):
        if remove_num <= 0:
            print(f"Number must be positive.")
        else:
            print(f"Can't remove more than {len(plates)} plates.")
        remove_num = read_user_input("How many plates would you like to remove from the stack?: ")
    while remove_num != 0:
        plates.pop()
        remove_num -= 1
    print("Successfully removed plate(s).")

# Read input function
def read_user_input(prompt):
    value = input(prompt).strip()
    int_value = ""
    validated = False
    while not validated:
        if not value:
            print("Error: invalid response.")
            value = input(prompt).strip()
        try:
            int_value = int(value)
            validated = True
        except ValueError:
            print("You must type a valid whole number")
            value = input(prompt).strip()


    int_value = int(value)
    return int_value


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

# displays printing plate menu
def print_plate_menu():
    print("=" * 26)
    print(f"||{exit_display:<22}||")
    print(f"||{plate_list:<22}||")
    print(f"||{vertical_display:<22}||")
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


            