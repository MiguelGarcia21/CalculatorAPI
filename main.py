# coder: kev 4.april.2025
"""

Create
-- def is_valid_number(s: str) -> bool

Create
-- Menu to select operation
-- Prompt user for two numbers
-- Call corresponding operation module
-- Print result

"""


def chosen_option(z: str, x: str, y: str):
    user_input_option = int(z)
    user_input_one = x
    user_input_two = y
    # the final solution variable is set here
    solution = 0
    # create a dict where each number activates a function
    options_nums = {
        '1': addition,
        '2': subtraction,
        '3': division,
        '4': multiply,
        '5': modules,
        '6': power
    }
    # Function mapping.. checks each z compared to dict values if inside continue
    if z in options_nums:
        solution = options_nums[z](user_input_one, user_input_two)# calls the z while giving the two values/parameters
    else:
        print("error chosen option")
    return solution # return to menu func

# This function is used for checking the option user selected
def is_valid_option(s: str):
    user_num = 0
    if s.isnumeric():
        user_num = int(s)
        if user_num <= 6:# makes sure number is not greater than 6 as max option is 6
            return True
        elif user_num > 6:
            return False
    else:
        print("something went wrong")

# This function is for checking the numbers inputted by user for calculation
def is_valid_number(s: str):
    user_num = 0 # store user number variable once verified is a number
    if s.isnumeric():
        user_num = int(s)
        return True # returns vaild is True
    else:
        return False


def addition(x: str, y: str):  # completed addition to test to see if others work
    num_one = int(x)
    num_two = int(y)
    print(num_one + num_two)


def subtraction(x: str, y: str):
    pass


def division(x: str, y: str):
    pass


def multiply(x: str, y: str):
    pass


def modules(x: str, y: str):
    pass


def power(x: str, y: str):
    pass


# Menu and inital welcomes
def cli_menu():
    running = True  # for later while loop
    valid = False  # check vaildation return value

    # Welcome area
    print(" -+- Welcome to the Calculator -+- ")
    print("Below are all the option this Calculator has:")
    print("1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Modules\n6. Power\n")
    # -----
    while running:
        valid_user_number = False
        user_input = input(str("Choose a option, ex: 1\n: "))
        valid_option = is_valid_option(user_input)  # using function to check if valid option was chosen
        if valid_option:
            print("Give Calculation to me two number:")
            user_num_one = input(str("num1: "))
            user_num_two = input(str("num2: "))
            valid_user_number = bool(is_valid_number(user_num_one) and is_valid_number(user_num_two))
            if valid_user_number:
                chosen_option(user_input, user_num_one, user_num_two)
            else:
                print("try a number please")


        else:
            print("Valid Option Please, choose one of the 6 (six) options\n")


if __name__ == "__main__":
    # Program starts here
    cli_menu()
