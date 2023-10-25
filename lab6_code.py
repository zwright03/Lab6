# Author: Zachary Wright
def menu():  # Menu function
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')


def encoder(password_in):  # takes a numerical password in, returns all digits in the password +3.
    stored_pass = ''
    for char in password_in:
        char = int(char) + 3
        stored_pass += str(char)[-1]  # if 7, 8, or 9 then the output is 2 digits, only the last one is needed
    return stored_pass


def decoder(password_in):
    stored_pass = ''
    for char in password_in:
        char = int(char) - 3
        stored_pass += str(char)[-1]  # if 7, 8, or 9 then the output is 2 digits, only the last one is needed
    return stored_pass


def main():
    final_password = None
    password_input = None
    continue_program = True

    while continue_program:
        menu()  # Prints the menu
        user_choice = int(input('Please enter an option: '))  # Prompt the user to choose a menu option
        
        if user_choice == 1:  # intakes the password to encode and stores it
            password_input = input('Please enter your password to encode: ')
            final_password = encoder(password_input)
            print('Your password has been encoded and stored!\n')

        if user_choice == 2:  # displays the original and new password
            print(f'The encoded password is {final_password}, and the original password is {password_input}')

        if user_choice == 3:  # stops the program
            continue_program = False

        if user_choice not in range(1, 4):  # invalid input check
            print('Invalid choice, please choose an integer 1-3.')


if __name__ == '__main__':
    main()
