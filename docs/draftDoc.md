# MacroTerm

## Statement of purpose

macro_term is a python terminal program that will enable the user to create and use keyboard macros and shortcuts. allow them to save and load those macros to and from file and activate a listening mode where macro_term will listen for the key presses to activated those macros and then output the key presses as specified by the macro to interact with the window that the user currently has open. macro_term using these features the user will be able to automate the input of groups of key presses, the repeated pressing of one key and the opening of program, files and folders. This will allow a user to improve their workflow, reduce wear and tear on their keyboard, automate input to programs or games where repeated keyboard input is need and improve their health by reducing the likelihood of them suffering from repetitive strain injuries.

This program is targeted at a wide target audience ranging from developers, gamers and higher level computer users who will be able to user the create shortcut to navigate to open file, folders and start programs faster. They will also be able to use the create macro feature to create macro to enter inputs such as terminal commands faster which will enable them to speed up there work flow and navigation of their computer. Professionals who create official documents and need to repeatedly input information for letter heads, legal or copyright reasons will be able to use the create macro feature to input that information.

Users at risk of repetitive strain injury due to preforming repeated actions or to reduce amount of use of the keyboard for users who due to injury or disability are unable to type on a keyboard for long periods of time will be able to use the create macro function to create macro to enter repeated input thus reducing the amount of use of the keyboard and avoiding repeating the same muscle movements to prevent repetitive strain injury.

## Features

macro_term will have a options menu to present the user with several options to create a macro, create Macros with repeat key presses, create shortcuts to open applications, save to file, import from file and a listen mode where macro_term will become a background process and listen for and run the macro's and keyboard shortcuts.

The create a macro option will ask the user for input to define the two key presses that will activate the macro for example alt+ l. Then it will ask for user input to define several key presses that will be outputted when the macro is activated by the user when MacroTerm is in listening mode these user inputs will be saved to a dictionary. The create macros with repeat key presses option will enable the user to create a macro where the output of the macro is a single key press that is repeated until the user presses that key combination to activate the macro again. The option to create shortcuts will instead of asking the user for keyboard presses to output will instead ask the user for a file path to a exe that be started or a file or folder that will be opened.

The save option will ask for user input that will be used as the name for a .json file where the dictionary that stores the macro will be saved. Import from file will ask the user to specify a .json file that will be imported and added to the dictionary storing the macro that are created.

The listen mode option will cause the program to become a background process that will listen for the key press that activate the Macros that are stored in the dictionary and then output the presses for that macro or follow the shortcut specified as well as listen for a esc key press to close the program.

## User Interaction

When using macro_term the user will first encounter the main menu, here the user will be shown a list of options that the user can choose between by inputting the number next to the option into the terminal or by inputting the full name of the option into the terminal. input will be handled by using conditional statements to check that the input is valid and in the event it is not inform the user that their input was invalid and the correct inputs they can use.

for the create macro option the user will be asked to input the  combination of two key presses to activate the macro they want to create. They are then asked to input the key presses that their macro will output. The input from the user will be handled to ensure that their inputs are possible key presses and the user will be informed if their input is not valid key presses.

for the Save and Import options the user will be asked to input a file name that will be imported or where the current macros that the user has created will be saved to. Error handling will be used to ensure that the input from the user is a valid file name and in the case of importing the file that the file exists. otherwise the user will be informed of the limits of filenames or that the file they tried to import doesn't exist.

for the create repeating macro option in the same way as the create macro option the user will be asked for input to determine what the key presses are for their macro except that they will be informed that they need to input the key presses to start the macro a second time to stop the macro repeating. as in the create macro option the users input will be error handled to ensure they input valid key presses.

for the create shortcut option the user will be asked for input in the same way as the earlier options except the second option will ask for a file or folder path that the shortcut will open. The users input will be error handled to ensure that their input is a valid and existing file path.

The listening mode option will inform the user that macro_term is now listening for their key presses and that the macro they have created are now able to be activated. The user will also be informed of the key presses that they can use to deactivate listening mode.

## Implantation

- The options menu will be implemented in a function that prints the options menu when it is called
- keyboard_input is a function that will get input from the user then check if the input is a valid key press then return that as output.
- The create macro option will be implemented in a function that runs key_input to get user input that will be used to define the key presses that activate the macro. then It will again request user input from keyboard_input. then the function will save the inputs to a dictionary where the macros the user had created are held in memory.

## ////

MacroTerm will also include error handling to ensure that user inputs for the macros are valid key presses that can be inputted and outputted from the keyboard. Make sure that user input for new filenames are valid filenames and input for file paths actually exist.

## features

- create keyboard macros to take an input of a key combination and output a series of key presses

- save those keyboard macros to a file

- import/load keyboard macros from a file

- go into to listening mode where the program waits in the background for you to press your macro and then runs that macro

- keyboard macros to output repeated key presses

- custom keyboard shortcuts to start programs or open file paths
