{% include navigation.html %}

# Create Task

[Link to Video](https://drive.google.com/file/d/1Q0BaE9bdI0uU5melWicJHrujReS3nP_H/view)


3. a) The purpose of the program is to provide a easy-to-use calculator system that performs math functions of varying difficulty. The calculator is for students who would like to solve math problems potentially involving fairly complex functions but either do not have access to or do not know how to correctly use a graphing calculator. The program takes an integer input from the user, which serves as their menu selection. The program then prompts them to input the necessary values for the math function that they selected. The input is the text that the user inputs in the menu and math fucntions. The output is routing the user to the correct menu selection as well as displaying the correct answer for the math functions.

3. b) 


# menu options as a dictionary
menu_options = {
    1: 'Find Hypotenuse Length',
    2: 'Find the Derivative',
    3: 'Find the Distance',
    4: 'exit',
}


# print menu options from dictionary key/value pair
def print_menu() -> object:
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()


The name of the dictionary is called menu_options. The dictionary contains the options for the menu. The list allows for the organization of menu options and the print_menu() function to run.


3. c)


# call procedures based on user input
def runOptions():
  # setting while loop condition to be true
  n = 0
  # while loop to accept/process user menu choice
  while (n == 0):
    try:
      option = int(input('Enter your choice 1-4: '))
      if option == 1:
        option1()
      elif option == 2:
        option2()
      elif option == 3:
        option3()
      elif option == 4:
        # setting while loop condition to be false
        n = 1
      else:
        # reprompt user if input is not an integer between 1 and 4
        print('Invalid option. Please enter a number between 1 and 4.')
    except ValueError:
      # reprompt user if input is not an integer
      print('Invalid input. Please enter an integer input.')
      
      
# print menu options from dictionary key/value pair
def print_menu() -> object:
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()    
 

The procedure displays the menu options in a loop. The procedure routes the user to the correct math function based on their selection. It reprompts users if they enter an invalid menu option using a try-except.


Initially, n is set to 0. The while loop parameter is n=0, so the while loop does not terminate. The if-else statements call the correct Python file. The procedure also includes the try-except.


3. d)


The procedure returns different different outputs based on the user's menu selection. The first call tests hypotenuse, which returns the value of the hypotenuse. The second call tests the derivative, which returns the derivative.
