# Development Log

## Development log 1/7/19

finally implemented the listen mode using pynput for macroterm after over coming several blockers. first being unable to use bash in WSL to run code that uses pynput as needs a proper os to work. to fix this I setup vscode so I can switch between using windows python from cmd and bash from WSL. It turns out using cmd means debugging in vscode now work unlike with WSL but unforunalty pynput wont work in the debugger either so I have debugged using print() at each step and try except to test exceptions. The second blocker was how to track the press and release of keys to check if those are shortcuts for a macro as on_press() and on_release() are functions defined in pynput I can't change their arguments to pass through more variables to them. after being unable to use a global bool to track if alt was being pressed I used a set to track the keys that were currently being pressed. 



