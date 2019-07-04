'''
macro_term written by Paul Robinson for Assessment 1: Plan and Implement a Terminal Application
'''
from os import path
import json
import argparse
from pynput import keyboard
from pynput.keyboard import Controller

parser = argparse.ArgumentParser(description='.json file to import macros from')
#TODO finish implenting argparse

def options_menu():
    '''
    prints the options menu
    '''
    print('[1] Create a macro')
    print('[2] Create a repeating macro')
    print('[3] Create a keyboard shortcut')
    print('[4] Import macros from a file')
    print('[5] Save your macros to a file')
    print('[6] Listen for your macros and shortcuts')
    print('[7] Exit MacroTerm')

def get_valid_keypress_input(input_question, invalid_input_response):
    '''
    asks the user for input using the input-question argument\n
    and returns that input if it is valid or informs the user their input\n
    is invalid using invalid_input_response\n
    input_question: string outputted to the user when the input is requested\n
    invalid_input_response: the string sent to the user when their input is invalid\n
    '''
    user_input = input(input_question)
    valid_keyboard_press = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w',
                            'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f',
                            'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
                            ',', '.', '/', '*', '`']
    for key in valid_keyboard_press:
        if user_input == key:
            #print(f'your valid input is {user_input}')
            return user_input
    print(invalid_input_response)
    return 'fail'

def get_valid_keypress_string(string_input_question, invalid_string_response):
    '''
    Asks the user for a string of keypresses using string_input_question/n
    and check if those keypresses are valid/n
    string_input_question: String outputted to the user when the input is requested/n
    invalid_string_response: The string sent to the user when the string they inputted is invalid\n
    '''
    #NTS add support for capitalization? change to using pynput instead of input?
    user_input = input(string_input_question)
    valid_keyboard_press = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w',
                            'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f',
                            'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
                            ',', '.', '/', '*', '`']
    user_input_list = [char for char in user_input]
    is_valid = False
    for char in user_input_list:
        for key in valid_keyboard_press:
            if char == key:
                is_valid = True
    if is_valid is False:
        print(invalid_string_response)
        return 'fail'
    return user_input

def get_valid_filename(filename_input_question, invalid_filename_response):
    '''
    Asks the user to input a filename using filename_input_question
    and check if they inputted a valid filename either returning the filename if its valid/n
    or printing invalid_filename_response if its not/n
    filename_input_question: The string printed to the user when asking for the filename/n
    invalid_filename_response: The string printed to the user when their filename is valid
    '''
    user_input = input(filename_input_question)
    invalid_filename_chars = ['<', '>', ':', '\"', '/', '\\', '|', '?', '*', '\0']
    is_valid = True
    if len(user_input) < 256:
        for char in user_input:
            for chars in invalid_filename_chars:
                if char == chars:
                    is_valid = False
        if is_valid is True:
            return user_input
    print(invalid_filename_response)
    return 'fail'

def get_valid_file_path(path_input, invalid_path_response):
    '''
    Requests input from the user for a file path then checks if the path exists\n
    and returns it if does or outputs invalid_path_response if it doesn't\n
    path_input: The string to be outputted to the user when asking for the file path\n
    invalid_path_response: The string to be outputted to the user if the file path is invalid
    '''
#NTS add support for filename without path?
    if path.exists(path_input):
        return path_input
    print(invalid_path_response)
    return 'fail'

def save_macro(save_dict, filename):
    '''
    Saves save_dict to a .json file using filename as the name of the file
    save_dict: the dictionary to be saved to the file
    filename: the name to be used for the file
    '''
    if filename != 'fail':
        dict_string = json.dumps(save_dict)
        filename = filename.strip()
        if (filename.split('.')[-1] != 'json') or (filename == 'json'):
            filename += '.json'
        with open(filename, 'w') as file:
            file.write(dict_string)
            print(f'your macros have been saved to {filename}')

def import_macro(file_path, import_dict):
    '''
    Imports a json file using file_path into the macro dictionary\n
    file_path: The path of the file to be imported\n
    import_dict: The dictionary the data from file will be imported into
    '''
    if file_path != 'fail':
        file_path = str(file_path)
        with open(file_path) as file:
            data = file.read().strip()
        data_dict = json.loads(data)
        import_dict.update(data_dict)
        return import_dict
    return import_dict

def create_macro(keypress_input, keypress_string, create_dict):
    '''
    Takes input from keypress_input and keypress_string and writes it into create_dict/n
    to store the macro/n
    keypress_input: The first keypress that will be used to activate the macro/n
    Keypress_string: The keypresses that will be outputted by the macro/n
    create_dict: The dictionary where keypress_input and keypress_string are added to
    '''
    if keypress_input != 'fail':
        if keypress_string != 'fail':
            keypress_input = str(keypress_input)
            keypress_string = str(keypress_string)
            create_dict[keypress_input] = keypress_string
            print(create_dict)#NTS remove after debuging
            return create_dict
        return create_dict
    return create_dict

def listening_mode(listen_dict):
    '''
    Activates listening mode where MarcoTerm will be listen for the marcos/n
    listen_dict: dictionary where the macros are stored
    '''
    currently_pressed = set()
    currently_pressed_macro = set()
    def on_press(key):
        '''
        uses currently_pressed to keep track of the keys being presses,/n
        then check if those keys are a macro shortcut/n
        and passes them to currently_pressed_macro if they are
        '''
        print(f'{key} pressed')#NTS remove after debuging
        currently_pressed.add(key)
        if keyboard.Key.alt_r in currently_pressed:
            print('alt is pressed')#NTS remove after debuging
            for macro in listen_dict:
                #if keyboard.KeyCode.from_char(macro) in currently_pressed:
                str_key = str(key)
                print(str_key)#NTS remove after debuging
                if macro == str_key[1]:
                    print(f'macro {key} triggered')#NTS remove after debuging
                    currently_pressed_macro.add(f'macro is pressed')
                    currently_pressed_macro.add(macro)
    def on_release(key):
        '''
        uses currently_pressed_macro to check if a macro shortcut is pressed\n
        and on the release of that shortcut activates the macro using output_macro
        '''
        try:
            currently_pressed.remove(key)
        except KeyError:
            print('key release excpetion')#NTS remove after debuging
        if 'macro is pressed' in currently_pressed_macro:
            currently_pressed_macro.remove('macro is pressed')
            released_marco = str(currently_pressed_macro.pop())
            print(released_marco)#NTS remove after debuging
            print(f'macro released is {released_marco}')#NTS remove after debuging
            output_macro(released_marco, listen_dict)
            currently_pressed_macro.clear()
        print(f'{key} release')#NTS remove after debuging
        if key == keyboard.Key.esc:
            print('esc pressed')#NTS remove after debuging
            listener.stop()
    def output_macro(activated_macro, output_dict):
        '''
        checks output_dict for the key activated_macro\n
        then outputs the value of activated_macro using pynput keyboard controller
        '''
        print('output trigged')#NTS remove after debuging
        print(output_dict)#NTS remove after debuging
        print(f'the macro activated is {activated_macro}')#NTS remove after debuging
        if activated_macro in output_dict:
            macro_value = output_dict[activated_macro]
            print(f'output from macro_value = {macro_value}')#NTS remove after debuging
            for char in macro_value:
                print(f'output {char}')#NTS remove after debuging
                keyboard = Controller()
                keyboard.press(char)
                keyboard.release(char)
        else:
            print('not found')
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def main():
    '''
    Handles the main logic for navigating the menus and calling functions
    '''
    macro_dict = {}
    options_menu()
    create_string = 'your macro will be activated by holding alt and a key of your choice'
    create_string2 = 'please type the key you would like to use\n'
    main_input = input()
    while main_input != '7':
        if main_input == '1':
            macro_dict = create_macro(
                get_valid_keypress_input(create_string + create_string2, 'that is not a valid key'),
                get_valid_keypress_string(
                    'enter the keystrokes you would like your macro to output\n',
                    'those are not valid keystokes'), macro_dict)
            print(macro_dict)
            main_input = input()
        elif main_input == '4':
            path_input = input('Enter the path of the file you want to input\n')
            macro_dict = import_macro(get_valid_file_path(path_input,
                'That is not a valid file path'), macro_dict)
            main_input = input()
        elif main_input == '5':
            save_macro(macro_dict, get_valid_filename('What would you like your file to be named?\n'
                                                        , 'That is not a valid filename'))
            main_input = input()
        elif main_input == '6':
            listening_mode(macro_dict)
            main_input = input()
        else:
            print('your input is invalid')
            main_input = input()
    exit()

main()
