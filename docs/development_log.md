# Development Log

## Development log 1/7/19

finally implemented the listen mode using pynput for macro_term after over coming several blockers. first being unable to use bash in WSL to run code that uses pynput as needs a proper os to work. to fix this I setup vscode so I can switch between using windows python from cmd and bash from WSL. It turns out using cmd means debugging in vscode now work unlike with WSL but unfortunately pynput wont work in the debugger either so I have debugged using print() at each step and try except to test exceptions. The second blocker was how to track the press and release of keys to check if those are shortcuts for a macro as on_press() and on_release() are functions defined in pynput I can't change their arguments to pass through more variables to them. after being unable to use a global bool to track if alt was being pressed I used a set to track the keys that were currently being pressed used a set to track the keys that where currently pressed so that macro_term can check when the macros in the macro dictionary are being activated and pass that to the output function.

## Development log 5/7/19

successfully implemented args parser to use the import function to enable the user to specify a file path that will be imported in a argument  when starting macro_term in the console. The main blocker I encountered while trying to implement args parser was first being able to call import_macro with the argument macro_dict when I first tried to implement arg parser at the start of my code. after changing it so that args parser was inside the main function I could use import_macro and macro_dict no problem.  I then had to use '--path' so that macro_term could be started without args incase the user didn't have a .json file they wanted to import macro from yet.



