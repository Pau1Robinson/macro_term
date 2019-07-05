'''
tests for macro_term to test output of create_macro() and save_macro() function
'''
import json
from os import remove as delete_file
from os import path
from macro_term import create_macro
from macro_term import save_macro

def test_create_macro():
    '''
    feeds create_macro a valid set of inputs and tests if it outputs the dictionary correctly
    '''
    test_char_input = 'm'
    test_string_input = 'my macro'
    test_dict = {}
    create_macro(test_char_input, test_string_input, test_dict)
    assert test_dict == {'m':'my macro'}

def test_create_macro_invalid():
    '''
    feeds create_macro a set of failed inputs and tests if it outputs the dictionary correctly
    '''
    test_char_input = 'fail'
    test_string_input = 'fail'
    test_dict = {}
    create_macro(test_char_input, test_string_input, test_dict)
    assert test_dict == {}

def test_save_macro():
    '''
    feeds save_macro a valid filename and dictionary/n
    tests if it writes to a file correctly
    '''
    test_dict = {'m':'macro', 'n':'macro2'}
    test_filename = 'macros'
    save_macro(test_dict, test_filename)
    with open(f'{test_filename}.json') as file:
        data = file.read().strip()
    data_dict = json.loads(data)
    assert data_dict == test_dict
    delete_file(f'{test_filename}.json')

def test_save_macro_invalid():
    '''
    feeds save_macro an invalid filename and dictionary/n
    tests to see if it will write to an invalid file
    '''
    test_dict = {'m':'macro', 'n':'macro2'}
    test_filename = '<fail>'
    test_bool = True
    save_macro(test_dict, test_filename)
    if path.exists(f'{test_filename}.json'):
        test_bool = False
    assert test_bool is True
