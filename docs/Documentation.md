# macro_term

## Statement of purpose

macro_term is a python terminal program that will enable the user to create and use keyboard macros and shortcuts. allow them to save and load those macros to and from file and activate a listening mode where macro_term will listen for the key presses to activated those macros and then output the key presses as specified by the macro to interact with the window that the user currently has open. macro_term using these features the user will be able to automate the input of groups of key presses, the repeated pressing of one key and the opening of program, files and folders. This will allow a user to improve their workflow, reduce wear and tear on their keyboard, automate input to programs or games where repeated keyboard input is need and improve their health by reducing the likelihood of them suffering from repetitive strain injuries.

This program is targeted at a wide target audience ranging from developers, gamers and higher level computer users who will be able to user the create shortcut to navigate to open file, folders and start programs faster. They will also be able to use the create macro feature to create macro to enter inputs such as terminal commands faster which will enable them to speed up there work flow and navigation of their computer. Professionals who create official documents and need to repeatedly input information for letter heads, legal or copyright reasons will be able to use the create macro feature to input that information.

Users at risk of repetitive strain injury due to preforming repeated actions or to reduce amount of use of the keyboard for users who due to injury or disability are unable to type on a keyboard for long periods of time will be able to use the create macro function to create macro to enter repeated input thus reducing the amount of use of the keyboard and avoiding repeating the same muscle movements to prevent repetitive strain injury.

## Features

macro_term will have a options menu to present the user with several options to create a macro, create Macros with repeat key presses, create shortcuts to open applications, save to file, import from file and a listen mode where macro_term will become a background process and listen for and run the macro's and keyboard shortcuts.

The create a macro option will ask the user for input to define the two key presses that will activate the macro for example alt+ l. Then it will ask for user input to define several key presses that will be outputted when the macro is activated by the user when macro_term is in listening mode these user inputs will be saved to a dictionary. The create macros with repeat key presses option will enable the user to create a macro where the output of the macro is a single key press that is repeated until the user presses that key combination to activate the macro again. The option to create shortcuts will instead of asking the user for keyboard presses to output will instead ask the user for a file path to a exe that be started or a file or folder that will be opened.

The save option will ask for user input that will be used as the name for a .json file where the dictionary that stores the macro will be saved. Import from file will ask the user to specify a .json file that will be imported and added to the dictionary storing the macro that are created.

The listen mode option will cause the program to become a background process that will listen for the key press that activate the Macros that are stored in the dictionary and then output the presses for that macro or follow the shortcut specified as well as listen for a esc key press to close the program.

## User Interaction

When using macro_term the user will first encounter the main menu, here the user will be shown a list of options that the user can choose between by inputting the number next to the option into the terminal or by inputting the full name of the option into the terminal. input will be handled by using conditional statements to check that the input is valid and in the event it is not inform the user that their input was invalid and the correct inputs they can use.

for the create macro option the user will be asked to input the  combination of two key presses to activate the macro they want to create. They are then asked to input the key presses that their macro will output. The input from the user will be handled to ensure that their inputs are possible key presses and the user will be informed if their input is not valid key presses.

for the Save and Import options the user will be asked to input a file name that will be imported or where the current macros that the user has created will be saved to. Error handling will be used to ensure that the input from the user is a valid file name and in the case of importing the file that the file exists. otherwise the user will be informed of the limits of filenames or that the file they tried to import doesn't exist.

for the create repeating macro option in the same way as the create macro option the user will be asked for input to determine what the key presses are for their macro except that they will be informed that they need to input the key presses to start the macro a second time to stop the macro repeating. as in the create macro option the users input will be error handled to ensure they input valid key presses.

for the create shortcut option the user will be asked for input in the same way as the earlier options except the second option will ask for a file or folder path that the shortcut will open. The users input will be error handled to ensure that their input is a valid and existing file path.

The listening mode option will inform the user that macro_term is now listening for their key presses and that the macro they have created are now able to be activated. The user will also be informed of the key presses that they can use to deactivate listening mode.

## Implementation

- options_menu is a function that will print the options menu when called

  - priority: medium duration: 5min

- The main function is where the loop and statements for calling functions using input as prompted by the main menu and args parser for importing  macros from .json files on start.

  - args parser will be used to enable the use to input --path as a argument when macro_term is run from the command line. This path will then be passed on to import_macro to import the file.

  - priority: high duration: 3hour

- create_macro is a function that will use get_valid_keypress_input and get_valid_keypress_string to get input from the user, check those inputs are valid keystrokes and then add them to the macro dictionary to store them.

  - get_valid_keypress_input is a function that gets input from the user and check against a list of valid key presses to ensure the input is valid a then return that input
  - get_valid_keypress_string is a function that gets the user to input a string and checks each character against a list of valid key presses to ensure the string only contains valid key presses and them returns the string.

  - priority: high duration: 2hour

- listening mode is a function that will listen for the key presses that activate the macros the user has created and are stored in macro_dict. listening mode will have three sub functions being

  - on_press for detecting the users key presses and storing them in a set call currently_pressed and detecting if a macro has been activated and send that to a set macro_currently_pressed
  - on_release for detecting keys being released and removing them from currently_pressed and detecting that macros have been released and then activate output_macro to output the macro.
  - output_macro for getting the output of a macro from macro_dict and then outputting it to the keyboard.
  - priority: high duration: 6hour

- import_macro is a function that will use get_valid_file_path to get the user to input a valid file path and then import_macro will import the macros from the .json file to macro_dict that path points to.

  - get_valid_file_path will ask the user for a file path, then get_valid_file_path will check that the file path exists and return the file path.

  - priority: medium duration: 2hour

- save_macro is a function that will use get_valid_filename to get a filename from the user and then save_macro will save the macros currently in macro_dict to a .json with the filename the user specified.
  - get_valid_filename is a function that asks the user to input a filename then checks the length and against a list of invalid characters. if the filename is valid get_valid_filename will then return the filename.

  - priority: medium duration: 2hour

## features

- create keyboard macros to take an input of a key combination and output a series of key presses
- save those keyboard macros to a file
- import/load keyboard macros from a file
- go into to listening mode where the program waits in the background for you to press your macro and then runs that macro
- keyboard macros to output repeated key presses
- custom keyboard shortcuts to start programs or open file paths
