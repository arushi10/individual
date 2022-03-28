"""
Introduction to Console Programming
Writing a function to print a menu
"""
from subprocess import call


# Menu options as a dictionary
menu_options = {
    1: 'week 0',
    2: 'week 1',
    3: 'week 2',
    4: 'exit',
}

menu2_options = {
    1: 'factorial',
    2: 'math',
    3: 'palindrome',
    4: 'exit',
}

# Print menu options from dictionary key/value pair
def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()
    
# menu option 1
def option1():
    print('You chose \' 1 -  week 0\'')
    call(["python", "week0/week0_menu.py"])

# menu option 2
def option2():
    print('You chose \' 2 - week 1\'')
    call(["python", "week1/week1_menu.py"])

# menu option 3
def option3():
    print('You chose \'3 - week 2\'')
    call(["python", "week2/week2_menu.py"])

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                option1()
            elif option == 2:
                option2()
            elif option == 3:
                option3()
            # Exit menu
            elif option == 4:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu()