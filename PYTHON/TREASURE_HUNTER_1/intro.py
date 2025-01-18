import os
from termcolor import colored
import time
import sys
import random

os.system("color")
map = [["@" for i in range(0, 51)] for j in range(0, 10)]


def init_map():
    x, y = 25, 25
    name = "TREASURE HUNTER"
    author = "TRUONG VAN DAI"
    l, r = 7, 7
    while x >= 0:
        print("\n" * 5)
        for i in map:
            print(" " * 30, end="")
            for j in i:
                sys.stdout.write(
                    colored(
                        j,
                        random.choice(
                            [
                                "red",
                                "green",
                                "yellow",
                                "blue",
                                "magenta",
                                "cyan",
                                "white",
                            ]
                        ),
                    )
                )
                print(end=" ")
            print(end="\n")
        time.sleep(0.05)
        os.system("cls")
        for k in range(0, 10):
            map[k][x] = " "
            map[k][y] = " "
        if l > -1:
            map[4][x] = name[l]
            map[4][y] = name[r]
            l -= 1
            r += 1
        x -= 1
        y += 1
    for i in map:
        print(" " * 25, end="")
        for j in i:
            sys.stdout.write(
                colored(
                    j,
                    random.choice(
                        ["red", "green", "yellow", "blue",
                            "magenta", "cyan", "white"]
                    ),
                )
            )
            print(end=" ")
        print(end="\n")
    print(" " * 52, "Ver 1.0.0")
    print(" " * 50, colored(author, "green"))
    time.sleep(1)
    os.system("cls")


def loading():
    pass


init_map()
