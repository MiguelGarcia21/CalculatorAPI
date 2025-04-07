def chosen_option(z: str, x: str, y: str):
    user_input_option = z
    user_input_one = float(x)
    user_input_two = float(y)
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
    if user_input_option in options_nums:
        return options_nums[user_input_option](user_input_one, user_input_two)# calls the z while giving the two values/parameters
    else:
        print("error chosen option...........")

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
    return s.isnumeric()


def addition(x: float, y: float):  # completed addition to test to see if others work
    return x+y


def subtraction(x: float, y: float):
    return x-y


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
                print(chosen_option(user_input, user_num_one, user_num_two))
            else:
                print("try a number please")


        else:
            print("Valid Option Please, choose one of the 6 (six) options\n")


if __name__ == "__main__":
    # Program starts here
    cli_menu()
