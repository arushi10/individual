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


The name of the dictionary is called menu_options. The dictionary contains the options for the menu.  
