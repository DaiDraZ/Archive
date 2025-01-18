import os
from termcolor import colored
import colorama
import time
import sys
import random

os.system("color")
colorama.init(autoreset=True)




def move_cursor_and_clear():
    print("\033[H\033[J", end="")

class Intro():
    def __init__(self) -> None:
        self.maps : list = [["@" for i in range(0, 51)] for j in range(0, 10)]
        self.colors : list = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    
    def init_map(self):
        x, y = 25, 25
        name = "TREASURE HUNTER"
        author = "Devevelop By TRUONG VAN DAI"
        l, r = 7, 7
        while x >= 0:
            print("\n" * 20)
            for i in self.maps:
                print(" " * 20, end="")
                for j in i:
                    sys.stdout.write(colored(j, random.choice(self.colors),))
                    print(end=" ")
                print(end="\n")

            time.sleep(0.05)
            move_cursor_and_clear()
            # os.system("cls")
            for k in range(0, 10):
                self.maps[k][x] = " "
                self.maps[k][y] = " "
            if l > -1:
                self.maps[4][x] = name[l]
                self.maps[4][y] = name[r]
                l -= 1
                r += 1
            x -= 1
            y += 1
        for i in self.maps:
            print(" " * 25, end="")
            for j in i:
                sys.stdout.write(colored(j, random.choice(self.colors),))
                print(end=" ")
            print(end="\n")
        print(" " * 70, "Ver 1.0.0")
        print(" " * 50, end="")
        for i in author:
            print(colored(i, "green"), end="", flush=True)
            time.sleep(0.15)
        time.sleep(1.5)
        # os.system("cls")
        move_cursor_and_clear()
    def start(self):
        self.init_map()

    def clean(self):
        move_cursor_and_clear()




Intro().start()