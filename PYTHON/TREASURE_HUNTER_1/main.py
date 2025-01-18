#! usr/bin/python-3.11.4

# Demo program in cmd
# import required module

# import menu
# import loading
# import intro
# import check
import keyboard
import time
from termcolor import colored
import os
import sys
import random
import colorama


width = 1367
height = 728

colorama.init(autoreset=True)
os.system("color")
size_x, size_y = 400, 300

map = []
mem = [15, 10]
temp_move : list[str] = [""]
record_move_last = ["0"]
# #x --> size_x,y --> size_y
# [y-ly[0]:y+ry[0]]
# [x-lx[0]:x + rx[0]]
# d-u -- y,r-l -- x

parent_dir = os.path.dirname(os.path.abspath(__file__)) 
print(parent_dir)
def import_map():
    parent_dir = os.path.dirname(os.path.abspath(__file__)) 
    txt_path = os.path.join(parent_dir,'map.txt')
    file = open(txt_path, mode="r")
    x = file.readline()
    while x != "":
        x = x.strip("\n")
        map.append(list(x.split(",")))
        x = file.readline()


def init_map(x, y):
    a, b, c, d = resize_map(x, y)
    line : str = ""
    # str1 = " " * 22 + "_" * 100
    # sys.stdout.write(str1 + "\n")
    for i in map[a:b]:
        # print(" " * 20, "|", end=" ")
        for j in i[c:d]:
            if j == "I":
                line += colored(j, "yellow")
            elif j == "-1":
                line += colored(".", "light_green")
            elif j == "1":
                line += colored("~", "light_blue")
            elif j == "2":
                line += colored("+", "light_green")
            # elif j == 'v':
            #   sys.stdout.write(colored('v','green'))
            elif j == "0":
                line += " "
            else:
                line += str(j)
            line += " "
            
        time.sleep(0.00001)
        line += "\n"
    sys.stdout.write(line)
    sys.stdout.flush()  
    return c


def resize_map(x, y):  # mini map, user center interface
    if x - mem[0] < 0:
        if y - mem[1] < 0:
            return 0, y + mem[1], 0, x + mem[0]
        if y + mem[1] >= 300:
            return y - mem[1], 300, 0, x + mem[0]
        else:
            return y - mem[1], y + mem[1], 0, x + mem[0]
    elif x + mem[0] >= 400:
        if y - mem[1] < 0:
            return 0, y + mem[1], x - mem[0], 400
        if y + mem[1] >= 300:
            return y - mem[1], 300, x - mem[0], 400
        else:
            return y - mem[1], y + mem[1], x - mem[0], 400
    else:
        if y - mem[1] < 0:
            return 0, y + mem[1], x - mem[0], x + mem[0]
        if y + mem[1] >= 300:
            return y - mem[1], 300, x - mem[0], x + mem[0]
        else:
            return y - mem[1], y + mem[1], x - mem[0], x + mem[0]


# def init_maze(size_x,size_y):
#   for j in range(0,300000):
#       map[random.randint(0,size_y-1)][random.randint(0,size_x-1)] = ' '
#   for j in range(0,100):
#       while map[random.randint(0,size_y-1)][random.randint(0,size_x-1)] not in block:
#           map[random.randint(0,size_y-1)][random.randint(0,size_x-1)] = 'T'
#           break


def move(x, y, max_x, max_y, direct):
    if collision(x, y, max_x, max_y):
        return None
    else:
        temp = map[y][x]
        if direct == "U":
            map[y][x] = "I"
            map[y + 1][x] = record_move_last[0]
        elif direct == "D":
            map[y][x] = "I"
            map[y - 1][x] = record_move_last[0]
        elif direct == "L":
            map[y][x] = "I"
            map[y][x + 1] = record_move_last[0]
        else:
            map[y][x] = "I"
            map[y][x - 1] = record_move_last[0]
        record_move_last[0] = temp


def collision(x, y, max_x, max_y):
    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return True
    if map[y][x] in ["1", "2"]:
        return True
    return False


def check_aim(x, y):
    if x == len(map[0]) - 1 and y == len(map) - 1:
        os.system("cls")
        print("WIN GAME")
        return True
    return False


def player():
    pass


# def refresh_map():
#   if map[0][1] in block and map[1][0] in block:
#       return True
#   return False


def init_game(max_x, max_y):
    x, y = 0, 0
    press = False
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "up":
            if not collision(x, y - 1, max_x, max_y):
                y -= 1
                temp_move[0] = "u"
                move(x, y, max_x, max_y, "U")
                press = True
        if event.event_type == keyboard.KEY_DOWN and event.name == "down":
            if not collision(x, y + 1, max_x, max_y):
                y += 1
                temp_move[0] = "d"
                move(x, y, max_x, max_y, "D")
                press = True
        if event.event_type == keyboard.KEY_DOWN and event.name == "left":
            if not collision(x - 1, y, max_x, max_y):
                x -= 1
                temp_move[0] = "l"
                move(x, y, max_x, max_y, "L")
                press = True
        if event.event_type == keyboard.KEY_DOWN and event.name == "right":
            if not collision(x + 1, y, max_x, max_y):
                x += 1
                temp_move[0] = "r"
                move(x, y, max_x, max_y, "R")
                press = True
        if event.name == "q":
            os.system("cls")
            print(
                r"""

                      ______ _   _ _____     _____          __  __ ______
                     |  ____| \ | |  __ \   / ____|   /\   |  \/  |  ____|
                     | |__  |  \| | |  | | | |  __   /  \  | \  / | |__
                     |  __| | . ` | |  | | | | |_ | / /\ \ | |\/| |  __|
                     | |____| |\  | |__| | | |__| |/ ____ \| |  | | |____
                     |______|_| \_|_____/   \_____/_/    \_\_|  |_|______|


"""
            )
            time.sleep(2)
            os.system("cls")
            # import loading
            # import menu

            break

        # Main program
        if press:  # fix while loop ,if user press on keyboard,map will change
            time.sleep(0.002)
            os.system("cls")
            init_map(x, y)
            check_aim(x, y)
            print("\n" * (15 - y))
            print(x, y, max_x, max_y, temp_move, record_move_last)
            press = False


import_map()
map[0][0] = "I"
map[len(map) - 1][len(map[0]) - 1] = "Flag"

init_map(0, 0)
init_game(size_x, size_y)
print(os.getcwd())
