import pygame
import keyboard
import time
from termcolor import colored
import os, sys
import random
import colorama 
from story import Story 
from setting import Setting
from sound import SFX, MUSIC

# Kích thước màn hình
width = 1367
height = 728

# Khởi tạo màu cho CMD
colorama.init(autoreset=True)
os.system("color")

# Khởi tạo Pygame

# Loading configs.txt
maps = []
mem = [20, 15]  # Kích thước camera
temp_move = [""]
record_move_last = ["0"]
step = [0]

# Đường dẫn tới tệp
parent_dir = os.path.dirname(os.path.abspath(__file__))

def import_map():
    txt_path = os.path.join(parent_dir, 'map.txt')
    try:
        with open(txt_path, mode="r") as file:
            for line in file:
                maps.append(list(line.strip().split(",")))
    except FileNotFoundError:
        print(f"File {colored('map.txt', 'red')} not found.")
        exit()

def move_cursor_and_clear():
    print("\033[H\033[J", end="")

def init_map(x, y):
    a, b, c, d = resize_map(x, y)
    line = ""
    for i in maps[a:b]:
        line += " " * 20
        for j in i[c:d]:
            if j == "I":
                line += colored(j, "yellow")
            elif j == "-1":
                line += colored(".", "light_green")
            elif j == "1":
                line += colored("~", "light_blue")
            elif j == "2":
                line += colored("+", "light_grey")
            elif j == "0" or j == "v":
                line += " "
            else:
                line += str(j)
            line += " "
        line += "\n"
    sys.stdout.write(line)
    sys.stdout.flush()  
    return c

def resize_map(x: int, y: int):
    # Camera algorithm
    top = max(0, y - mem[1])
    bottom = min(300, y + mem[1])
    left = max(0, x - mem[0]) 
    right = min(400, x + mem[0])
    return top, bottom, left, right

def move(x, y, max_x, max_y, direct):
    if collision(x, y, max_x, max_y):
        return None
    else:
        temp = maps[y][x]
        if direct == "U":
            maps[y][x] = "I"
            maps[y + 1][x] = record_move_last[0]
        elif direct == "D":
            maps[y][x] = "I"
            maps[y - 1][x] = record_move_last[0]
        elif direct == "L":
            maps[y][x] = "I"
            maps[y][x + 1] = record_move_last[0]
        else:  # direct == "R"
            maps[y][x] = "I"
            maps[y][x - 1] = record_move_last[0]
        record_move_last[0] = temp
        step[0] += 1

def collision(x, y, max_x, max_y):
    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return True
    if maps[y][x] in ["1", "2"]:
        return True
    return False

def check_aim(x, y):
    if x == len(maps[0]) - 1 and y == len(maps) - 1:
        move_cursor_and_clear()
        print("WIN GAME")
        return True
    return False

def init_game(max_x, max_y):
    x, y = 0, 0
    press = False
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            press = True
            if event.name == "up" and not collision(x, y - 1, max_x, max_y):
                y -= 1
                move(x, y, max_x, max_y, "U")
                
            elif event.name == "down" and not collision(x, y + 1, max_x, max_y):
                y += 1
                move(x, y, max_x, max_y, "D")

            elif event.name == "left" and not collision(x - 1, y, max_x, max_y):
                x -= 1
                move(x, y, max_x, max_y, "L")

            elif event.name == "right" and not collision(x + 1, y, max_x, max_y):
                x += 1
                move(x, y, max_x, max_y, "R")
            
            elif event.name == "q":
                move_cursor_and_clear()
                print("Exiting game...")
                time.sleep(1)
                break

        if press:
            # Giảm độ trễ giữa các lần vẽ lại
            time.sleep(0.05)
            SFX().player_walking()
            move_cursor_and_clear()  # Vẽ lại màn hình mỗi khi người chơi di chuyển
            init_map(x, y)  # Cập nhật bản đồ với vị trí mới
            check_aim(x, y)
            print("\n" * (15 - y))
            print(f'{" "*15}[Health : {50}]{" "*5}[Atk : {2.0}]{" "*5}[Def : {2.0}]')
            print(x, y, max_x, max_y, temp_move, record_move_last)
            if step[0] > random.randint(50, 70):
                for _ in range(random.randint(1, 4)):
                    Story(random.randint(0, 80)).run()
                step[0] = 0
            press = False

if __name__ == "__main__":
    MUSIC().player()
    import_map()
    maps[0][0] = "I"
    maps[len(maps) - 1][len(maps[0]) - 1] = "Flag"
    init_map(0, 0)
    init_game(400, 300)
