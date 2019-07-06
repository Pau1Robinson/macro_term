# macro_term

macro_term is a program for creating and using of macros and keyboard shortcuts. macro_term lets you create, save, import and even use macros while your using another application.

## Installation

## Running macro_term

when starting macro_term you are able to specify a  .json file containing macros to be imported when macro_term starts. To do this use the add --path file_path when running macro_term from the command line for example.

> macro_term --path C:\my_folder\my_macros.json

## Creating a macro

After launching macro_term you will be show the main menu

> [1] Create a macro
> [2] Create a repeating macro
> [3] Create a keyboard shortcut
> [4] Import macros from a file
> [5] Save your macros to a file
> [6] Listen for your macros and shortcuts
> [7] Exit macro_term

Press 1 and then enter to use the Create a Macro option. macro_term will ask you what key you want to use to activate your macro.

> your macro will be activated by holding right alt and a key of your choice please type the key you would like to use

Press the key you would like to use to activate your macro and hit enter.  your macro will be activated by pressing right alt and this key at the same time. Next you be asked for the key presses your macro will output.

> enter the keystrokes you would like your macro to output

Type the keystrokes you want your macro to output when you activate it and press enter. If any of your inputs are not valid key presses macro_term will show you an error.

> those are not valid keystrokes

Your macro may only contain non CAPS key characters and not keys such as backspace,shift, tab .etc

To use your macro you must press 6 so that macro_term will listen for your macros

> [1] Create a macro
> [2] Create a repeating macro
> [3] Create a keyboard shortcut
> [4] Import macros from a file
> [5] Save your macros to a file
> [6] Listen for your macros and shortcuts
> [7] Exit macro_term

This will start listening mode.

> macro_term is now listening for your macros

To use a macro you have created press the key you set to activate it and right alt at the same time. As long as macro_term is in listening mode it will listen for your macros even while in the background or while your using another application.

> macro alt_r + m:'my_macro' has been activated

- known issue: using a macro may activate menu shortcuts in the program your using instead of tying out your macro as text due to alt being pressed as your macro outputs to the keyboard . This is reduced with the current implementation of macro_terms listening mode but its recommended you only press the keys to activate your macro for second and don't hold down the keys.

## Saving and importing your macros

To save the macros you have created press 5

> [1] Create a macro
> [2] Create a repeating macro
> [3] Create a keyboard shortcut
> [4] Import macros from a file
> [5] Save your macros to a file
> [6] Listen for your macros and shortcuts
> [7] Exit macro_term

macro_term will then ask you for a file name for your save file.

> What would you like your file to be named?

Here you need to type in your file name it must not be longer than 255 characters or contain the characters < > : \" / \' | ? * or the ASIIC NUL character.

Then press enter and macro_term will save your macros to a .json file.

> your macros have been saved to my_macros.json

To import your macros from a .json file press 4

>[1] Create a macro
>[2] Create a repeating macro
>[3] Create a keyboard shortcut
>[4] Import macros from a file
>[5] Save your macros to a file
>[6] Listen for your macros and shortcuts
>[7] Exit macro_term

macro_term will ask you for the file path of the file you want to import.

> Enter the path of the file you want to input

for example

> C:\my_folder\my_macros.json

After typing in the file path press enter and macro_term will import the macros from the .json file

> C:\my_folder\my_macros.json has been imported

You will now be able to use listening mode to use the macros you have imported.
