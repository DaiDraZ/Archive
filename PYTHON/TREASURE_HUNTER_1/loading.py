import time
import random
from termcolor import colored, cprint
import os
import sys

os.system("color")


def bar_loading():
    percent = 0
    dot = [".", "..", "..."]
    load = [">_<", "o_o", ">_<"]
    src = [
        "load_DATA_PLAYER\n",
        "get_DATA_SYSTEM_USER\n",
        "load_FILE_MAP.TXT\n",
        "get_WINDOW_SIZE\n",
        "load_BUFFER_CACHE\n",
        "check_WINDOW_DEFENDER_<!>\n",
        "load_REQUIREMENTS_FILE\n",
        "check_NETWORKING_CONNECT\n",
        "get_SYSTEM_USER\n",
    ]
    x, y = 0, 0
    while percent <= 100:
        print("\n" * 5)
        print(
            " " * 65, colored("Welcome to the VN_studio " +
                              load[x], "white", "on_blue")
        )
        sys.stdout.write("\n" * 15)
        print(" " * 70, colored("Loading" + dot[x]))
        x += 1
        y += 1
        if x > 2:
            x = 0
        if y > 8:
            y = 0
        percent += random.randint(1, 15)
        if percent > 100:
            os.system("cls")
            print("\n" * 5)
            print(" " * 65, colored("Welcome to the VN_studio >.<", "white", "on_blue"))
            sys.stdout.write("\n" * 15)
            print(" " * 55, colored("Loading success !", "white"))
            print(" " * 50, "[", colored("=" * 50,
                                         "green", "on_green"), "] 100%")
            time.sleep(2)
            os.system("cls")
            break
        print(
            " " * 50,
            "[",
            colored("=" * (percent // 2), "green", "on_green"),
            " " * ((100 - percent) // 2),
            "] ",
            percent,
            "%",
        )
        print("\n", " " * 50, f"-->{src[y]} ")
        time.sleep(0.5)
        os.system("cls")
    pass


bar_loading()
