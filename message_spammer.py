import os
import time
import importlib

version = '0.1.0'

def clearscreen():
    os.system('cls')

def print_header():
    print('Message Spammer by Green11_KD')
    print('Ver. ', version)
    print('')

print('Welcome to Message Spammer!')
print('Made by Green11_KD')
print('Version: ', version)

time.sleep(0.5)

print('\nWhat will be your message?')
spam_message = input ('> ')

time.sleep(0.5)

print('\nHow many messsages would you like to send?')
try:
    spam_amount = int(input('> '))
except ValueError:
    print("Invalid number. Please restart and enter a valid integer.")
    input("Press Enter to exit...")
    exit()

time.sleep(0.5)

print('\nWould you like to continue?')
print('Message: ' + spam_message)
print('Spamming: ', spam_amount, ' messages')
input ('Press Enter to continue or Ctrl + C to exit')

clearscreen()
# input (' ')
# time.sleep(1)

print_header()

print('Getting Message Spammer ready...')

try:
    import pyautogui
except ImportError as e:
    print('\nError! Could not setup Message Spammer')
    print("Not all package is installed. Please run the installer again to fix this issue")
    input ('Press enter to exit...')
    quit()
try:
    import keyboard
except ImportError as e:
    print('\nError! Could not setup Message Spammer')
    print("Not all package is installed. Please run the installer again to fix this issue")
    input ('Press enter to exit...')
    quit()
import threading
try:
    import pyperclip
except ImportError as e:
    print('\nError! Could not setup Message Spammer')
    print("Not all package is installed. Please run the installer again to fix this issue")
    input ('Press enter to exit...')
    quit()
spam_status = 'n'
spam_count = 0
spam_timer = 0
before_copy = pyperclip.paste()
pyperclip.copy(spam_message)

def spam():
    global spam_amount
    global spam_count
    global spam_status
    global spam_timer
    print('Spamming...')
    time.sleep(0.1)
    start = time.time()
    while spam_status != 'f':
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        spam_count += 1
        if spam_count == int(spam_amount) or spam_status == 'f':
            break
    end = time.time()
    spam_timer = end - start
    print('\nDone Spamming')
    spam_status = 'd'

def forcestop():
    global spam_status
    while spam_status != 'd':
        time.sleep(0.09)
        if keyboard.is_pressed('f6'):
            spam_status = 'f'
            print('\nStopped Spamming')

clearscreen()

print_header()

print('Message Spammer is ready!')

print('\nMessage: ', spam_message)
print('Spamming: ', spam_amount, ' messages')

print('\nPress F6 to start, and press F6 again to stop.')

keyboard.wait('f6')
time.sleep(0.1)
threading.Thread(target=forcestop).start()
spam()
pyperclip.copy(before_copy)
print('Message Spammed: ', spam_message)
print('Spammed ', spam_count, ' times in ', round(spam_timer, 2), ' seconds')
input ('Press Enter to exit...')