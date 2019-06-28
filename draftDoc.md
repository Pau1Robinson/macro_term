# MacroTerm

## Statement of purpose

MacroTerm is a python terminal program that will enable the user to create and use of keyboard macros and shortcuts, saving and loading of those macros from a file and activate a listening mode where MacroTerm will go to the background a list for the key presses to activated those macros and then output the key presses as specified by the macro to interact with the window that the user currently has open.  macroterm will allow the user to automate the input of groups of key presses, the repeated pressing of one key and the opening of program, files and folders. This will allow a user to improve their workflow, reduce wear and tear on their keyboard, automate input to programs or games where repeated keyboard input is need and improve their health by reducing the users chance of suffering from repetitive strain injuries. 

This program is targeted at a wide target audience ranging from developers and higher level computer users who will be able to user the create shortcut to navigate to open file, folders and start programs faster. They will also be able to use the create macro feature to create macro to enter inputs such as terminal commands faster which will enable them to speed up there work flow and navigation of their computer. Professionals who create official documents and need to repeatedly input information for letter heads, legal or copyright reasons will be able to use the create macro feature to input that information.

Users at risk of repetitive strain injury due to preforming repeated actions or to reduce amount of use of the keyboard for users who due to injury or disability are unable to type on a keyboard for long periods of time will be able to use the create macro function to create macro to enter repeated input thus reducing the amount of use of the keyboard and avoiding repeating the same muscle movements to prevent repetitive strain injury.

## Features

. MacroTerm will have a options menu to present the user with several options to create a macro, create Macros with repeat key presses, create shortcuts to open applications, save to file , import from file and a listen mode where Macroterm will become a background process and listen for and run the macro's and keyboard shortcuts.

The create a macro option will ask the user for input to define the two key presses that will activate the macro for example alt+ l. Then it will ask for user input to define several key presses that will be outputted when the macro is activated by the user when MacroTerm is in listening mode these user inputs will be saved to a dictionary. The create macros with repeat key presses option will enable the user to create a macro where the output of the macro is a single key press that is repeated until the user presses that key combination to activate the macro again. The option to create shortcuts will instead of asking the user for keyboard presses to output will instead ask the user for a file path to a exe that be started or a file or folder that will be opened.

The save option will ask for user input that will be used as the name for a .json file where the dictionary that stores the macro will be saved. Import from file will ask the user to specify a .json file that will be imported and added to the dictionary storing the macro that are created.  

The listen mode option will cause the program to become a background process that will listen for the key press that activate the Macros that are stored in the dictionary and then output the presses for that macro or follow the shortcut specified as well as listen for a key press combination to close the program.

## Implantation

- The options menu will be implemented in a function that prints the options menu when it is called
- keyboard_input is a function that will get input from the user then check if the input is a valid key press then return that as output.
- The create macro option will be implemented in a function that runs key_input to get user input that will be used to define the key presses that activate the macro. then It will again request user input from keyboard_input. then the function will save the inputs to a dictionary where the macros the user had created are held in memory. 

## ////

MacroTerm will also include error handling to ensure that user inputs for the macros are valid key presses that can be inputted and outputted from the keyboard. Make sure that user input for new filenames are valid filenames and input for file paths actually exist.

## features

- create keyboard macros to take an input of a key combination and output a series of keypresses 

- save those keyboard macros to a file

- import/load keyboard macros from a file

- go into to listening mode where the program waits in the background for you to press your macro and then runs that macro

- keyboard macros to output repeated key presses

- custom keyboard shortcuts to start programs or open file paths

  

  