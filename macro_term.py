'''
macro_term written by Paul Robinson for Assessment 1: Plan and Implement a Terminal Application
Licence: GPLv3
'''
from os import path
import json
import argparse
if __name__ == "__main__":#This allows test_macro_term.py to work
    from pynput import keyboard
    from pynput.keyboard import Controller

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
    print('[7] Exit macro_term')

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
            return user_input
    print(invalid_input_response)
    return 'FAIL'

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
                            ',', '.', '/', '*', '`', ' ']
    user_input_list = [char for char in user_input]
    is_valid = False
    for char in user_input_list:
        for key in valid_keyboard_press:
            if char == key:
                is_valid = True
    if is_valid is False:
        print(invalid_string_response)
        return 'FAIL'
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
    if path.exists(path_input):#NTS add support for filename without path?
        return path_input
    print(invalid_path_response)
    return '<fail>'

def save_macro(save_dict, filename):
    '''
    Saves save_dict to a .json file using filename as the name of the file
    save_dict: the dictionary to be saved to the file
    filename: the name to be used for the file
    '''
    if filename != '<fail>':
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
    if file_path != '<fail>':
        file_path = str(file_path)
        with open(file_path) as file:
            data = file.read().strip()
        data_dict = json.loads(data)
        import_dict.update(data_dict)
        print(f'{file_path} has been imported')
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
    if keypress_input != 'FAIL':
        if keypress_string != 'FAIL':
            keypress_input = str(keypress_input)
            keypress_string = str(keypress_string)
            create_dict[keypress_input] = keypress_string
            return create_dict
        return create_dict
    return create_dict

def listening_mode(listen_dict):
    '''
    Activates listening mode where marco_term will be listen for the marcos/n
    has three functions to handle the key press, key release and the output of the macro/n
    listen_dict: dictionary where the macros are stored
    '''
    print('macro_term is now listening for your macros')
    currently_pressed = set()
    currently_pressed.add(keyboard.Key.enter)
    currently_pressed_macro = set()

    def on_press(key):
        '''
        Uses currently_pressed to keep track of the keys being presses,/n
        then check if those keys are a macro shortcut/n
        and passes them to currently_pressed_macro if they are
        '''
        currently_pressed.add(key)
        if keyboard.Key.alt_r in currently_pressed:
            for macro in listen_dict:
                str_key = str(key)
                if macro == str_key[1]:
                    currently_pressed_macro.add(f'macro is pressed')
                    currently_pressed_macro.add(macro)

    def on_release(key):
        '''
        Activities on the release of a key, uses currently_pressed_macro to check/n
        if a macro has been activated. Then calls output_macro with the macro as an argument/n
        Also checks if the esc key has been released and returns to menu if it has.
        '''
        try:
            currently_pressed.remove(key)
        except KeyError:
            print('on_release: unable to remove element key from set currently_pressed')
        if 'macro is pressed' in currently_pressed_macro:
            currently_pressed_macro.remove('macro is pressed')
            released_marco = str(currently_pressed_macro.pop())
            output_macro(released_marco, listen_dict)
            currently_pressed_macro.clear()
        if key == keyboard.Key.esc:
            currently_pressed.clear()
            currently_pressed_macro.clear()
            listener.stop()

    def output_macro(activated_macro, output_dict):
        '''
        Checks output_dict for the key activated_macro\n
        then outputs the value of activated_macro to the keyboard/n
        using pynput macro_output controller
        '''
        if activated_macro in output_dict:
            macro_value = output_dict[activated_macro]
            macro_output = Controller()
            macro_output.type(macro_value)
            print(f'macro alt_r + {activated_macro}:\'{macro_value}\' has been activated')
        else:
            print('not found')

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def main():
    '''
    Handles the main logic for parse args, navigating the menus and calling functions
    '''
    macro_dict = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='path of .json file to be imported on start')
    args = parser.parse_args()
    if args.path:
        path_str = str(args.path)
        import_macro(get_valid_file_path(path_str, 'That is not a valid file path'), macro_dict)

    options_menu()
    create_string = 'your macro will be activated by holding right alt and a key of your choice '
    create_string2 = 'please type the key you would like to use\n'
    invalid_filename = 'That is not a valid filename, filenames must not have more than 255 '
    invalid_filename2 = 'characters or contain the characters < > : \" / \' | ? * NUL'
    main_input = input()

    while main_input != '7':
        if main_input == '1':
            macro_dict = create_macro(
                get_valid_keypress_input(create_string + create_string2, 'that is not a valid key'),
                get_valid_keypress_string(
                    'enter the keystrokes you would like your macro to output\n',
                    'those are not valid keystrokes'), macro_dict)
            print(macro_dict)
            options_menu()
            main_input = input()
        elif main_input == '4':
            path_input = input('Enter the path of the file you want to input\n')
            macro_dict = import_macro(get_valid_file_path(
                path_input, 'file path not found'), macro_dict)
            options_menu()
            main_input = input()
        elif main_input == '5':
            save_macro(macro_dict, get_valid_filename(
                'What would you like your file to be named?\n'
                , invalid_filename + invalid_filename2))
            options_menu()
            main_input = input()
        elif main_input == '6':
            listening_mode(macro_dict)
            options_menu()
            main_input = input()
        else:
            print('your input is invalid')
            options_menu()
            main_input = input()
    exit()

if __name__ == "__main__":
    main()
