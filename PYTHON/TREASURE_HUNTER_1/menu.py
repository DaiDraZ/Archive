import keyboard
import os
from termcolor import colored


# Thiết lập màu cho CMD
os.system('color')

def move_cursor_and_clear():
    print("\033[H\033[J", end="")  # Di chuyển con trỏ về đầu và xóa màn hình.


class MainMenu():
    def __init__(self) -> None:
        self.menus = ['New game', 'Continue', 'Option', 'Credit']

        self.logo = [r'''
          _____   ____    _____      _      ____    _   _   ____    _____     _   _   _   _   _   _   _____   _____   ____  
         |_   _| |  _ \  | ____|    / \    / ___|  | | | | |  _ \  | ____|   | | | | | | | | | \ | | |_   _| | ____| |  _ \ 
           | |   | |_) | |  _|     / _ \   \___ \  | | | | | |_) | |  _|     | |_| | | | | | |  \| |   | |   |  _|   | |_) |
           | |   |  _ <  | |___   / ___ \   ___) | | |_| | |  _ <  | |___    |  _  | | |_| | | |\  |   | |   | |___  |  _ < 
           |_|   |_| \_\ |_____| /_/   \_\ |____/   \___/  |_| \_\ |_____|   |_| |_|  \___/  |_| \_|   |_|   |_____| |_| \_\.'''
        ]
        
        pass
    def display_menu(self,selected_index :int):
        move_cursor_and_clear()
        print(colored(self.logo[0], 'light_blue'))
        print('\n' * 10)
        for i, menu in enumerate(self.menus):
            if i == selected_index:
                print(' ' * 69, '[', colored(menu, 'light_red'), ']')
            else:
                print(' ' * 70, f' {menu}')
            print("\n")




    def show(self):
        selected_index = 0
        self.display_menu(selected_index)

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'up' and selected_index > 0:
                    selected_index -= 1
                elif event.name == 'down' and selected_index < len(menus) - 1:
                    selected_index += 1
                elif event.name == 'enter':
                    if selected_index == 0:
                        move_cursor_and_clear()
                    elif selected_index == 1:
                        pass
                    elif selected_index == 2:
                        pass  
                    elif selected_index == 3:
                        pass

                self.display_menu(selected_index)  #Update menu

