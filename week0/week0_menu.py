"""
Introduction to Console Programming
Writing a function to print a menu
"""
from subprocess import call
from week0 import keypad, ship, swap, tree

# Menu options in print statement
# def print_menu1():
#     print('1 -- option1' )
#     print('2 -- option2' )
#     print('3 -- option3' )
#     print('4 -- Exit' )
#     runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'swap',
    2: 'keypad',
    3: 'patterns',
    4: 'exit',
}

menu2_options = {
    1: 'tree',
    2: 'animation',
    3: 'exit',
}

# Print menu options from dictionary key/value pair
def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

def print_menu2():
    for key in menu2_options.keys():
        print(key, '--', menu2_options[key] )
    run2Options()
    
# menu option 1
def option1():
    print('You chose \' 1 -  swap\'')
    swap.driver()

# menu option 2
def option2():
    print('You chose \' 2 - keypad\'')
    keypad.driver()

# menu option 3
def option3():
    print('You chose \'3 - patterns\'')
    print_menu2()

def option4():
    print('You chose \' 1 - Tree\'')
    tree.driver()

def option5():
    print('You chose \' 2 - Animation\'')
    ship.driver()
    ship.driver()
  


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

def run2Options():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option2 = int(input('Enter your choice 1-3: '))
            if option2 == 1:
                option4()
            elif option2 == 2:
                option5()
            # Exit menu
            elif option2 == 3:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 3.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    print_menu()