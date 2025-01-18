import keyboard
import os
from termcolor import colored
os.system('color')
menus = ['New game', 'Continue', 'Option', 'Credit']


def comd(x):
    print(colored(r'''
		  _____   ____    _____      _      ____    _   _   ____    _____     _   _   _   _   _   _   _____   _____   ____  
		 |_   _| |  _ \  | ____|    / \    / ___|  | | | | |  _ \  | ____|   | | | | | | | | | \ | | |_   _| | ____| |  _ \ 
		   | |   | |_) | |  _|     / _ \   \___ \  | | | | | |_) | |  _|     | |_| | | | | | |  \| |   | |   |  _|   | |_) |
		   | |   |  _ <  | |___   / ___ \   ___) | | |_| | |  _ <  | |___    |  _  | | |_| | | |\  |   | |   | |___  |  _ < 
		   |_|   |_| \_\ |_____| /_/   \_\ |____/   \___/  |_| \_\ |_____|   |_| |_|  \___/  |_| \_|   |_|   |_____| |_| \_\.''', 'light_blue'))

    print('\n'*10)
    for i in range(0, 4):
        if i == x:
            print(' '*70, '[', colored(menus[i], 'light_red'), ']')
        else:
            print(' '*70, f' {menus[i]}')


press = False
comd(0)
x = 0
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'up' and x > 0:
        x -= 1
        press = True
    if event.event_type == keyboard.KEY_DOWN and event.name == 'down' and x < 3:
        x += 1
        press = True
    if event.event_type == keyboard.KEY_DOWN and event.name == 'enter' and 0 <= x < 4:
        if x == 0:
            os.system('cls')
            import main
        if x == 1:
            import main
        if x == 2:
            import setting
        if x == 3:
            import intro
    if press:
        os.system('cls')
        comd(x)
        press = False
