"""
Introduction to Console Programming
Writing a function to print a menu
"""
from subprocess import call
from week1 import fibonacci, infoDB_lists, infoDB_loops

# Menu options as a dictionary
menu_options = {
    1: 'InfoDB Lists',
    2: 'InfoDB Loops',
    3: 'Fibonacci',
    4: 'exit',
}


# Print menu options from dictionary key/value pair
def driver():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()
    
# menu option 1
def option1():
    print('You chose \' 1 -  InfoDB Lists\'')
    call(["python", infoDB_lists.driver])

# menu option 2
def option2():
    print('You chose \' 2 - InfoDB Loops\'')
    call(["python", infoDB_loops.driver])

# menu option 3
def option3():
    print('You chose \'3 - Fibonacci\'')
    call(["python", fibonacci.driver])
  


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
    driver()