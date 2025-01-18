import random
import os
import sys
from termcolor import colored
import time
from colorama import init
import keyboard
import pygame


# Auto reload color in CMD
init(autoreset=True)
# Require cmd get color
os.system("color")
# Khởi tạo Pygame
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()


def move_cursor_and_clear():
    print("\033[H\033[J", end="")  # Di chuyển con trỏ về đầu và xóa màn hình.


# class SFX():

#     def __init__(self) -> None:
#         self.text_sould = pygame.mixer.Sound(f"typing0.mp3")
#         self.volumes = self.text_sould.set_volume

#     def set_volumes(self, volumes: float):
#         self.volumes(volumes)

#     def player(self):
#         self.text_sould.play()


# class MUSIC():
#     def __init__(self) -> None:
#         pygame.mixer.music.load("Accel World - Way Home.mp3")
#         self.volumes = pygame.mixer.music.set_volume

#     def set_volumes(self, volumes: float):
#         self.volumes(volumes)

#     def player(self):
#         # Phát nhạc nếu chưa phát
#         if not pygame.mixer.music.get_busy():
#             pygame.mixer.music.play(-1)


class Setting():
    """Setting game"""

    def __init__(self) -> None:
        # self.list_setting: dict = {
        #     "Music": 10,
        #     "Sfx": 10,
        #     "Graphic": ["Full screen", "1280x720", "800x600", 0],
        #     "Fps": [60, 45, 30, 0],
        #     "Font": 10,
        #     "Task": 1  # 1 - save, 0 - quit
        # }
        self.list_setting: dict = self.load_config("configs.txt")
        self.graphic = ["Full screen", "1280x720", "800x600"]
        self.fps = [60, 45, 30]
        self.option: int = 0
        self.keys: list = list(self.list_setting.keys())
        # self.music = MUSIC()
        # self.sfx = SFX()

    def load_config(self, config_file: str):
        config = {}
        with open(config_file, "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                config[key] = int(value)
        return config

    def save_config(self, config_file: str):
        """Ghi lại dictionary cài đặt vào file config.txt."""
        try:
            with open(config_file, "w") as file:
                for key, value in self.list_setting.items():
                    file.write(f"{key}: {value}\n")
        except Exception as e:
            print(f"Không thể lưu cài đặt: {e}")

        pass
        move_cursor_and_clear() 

    def update_setting(self, change):
        if self.keys[self.option] == "Graphic":
            self.list_setting["Graphic"] += change
            self.list_setting["Graphic"] = max(0, min(2, self.list_setting["Graphic"]))

        elif self.keys[self.option] == "Fps":
            self.list_setting["Fps"] += change
            self.list_setting["Fps"] = max(0, min(2, self.list_setting["Fps"]))

        elif self.keys[self.option] == "Task":
            self.list_setting["Task"] += change
            self.list_setting["Task"] = max(0, min(1, self.list_setting["Task"]))

        elif self.keys[self.option] == "Font":
            self.list_setting[self.keys[self.option]] += change
            self.list_setting[self.keys[self.option]] = max(0, min(10, self.list_setting[self.keys[self.option]]))
            pass    

        else:
            self.list_setting[self.keys[self.option]] += change
            self.list_setting[self.keys[self.option]] = max(0, min(10, self.list_setting[self.keys[self.option]]))
            # if self.keys[self.option] == "Music":
            #     self.music.set_volumes(self.list_setting[self.keys[self.option]] / 10.0)
            # else:
            #     self.sfx.set_volumes(self.list_setting[self.keys[self.option]] / 10.0)

    def display_menu(self):
        move_cursor_and_clear()
        print(f"{" "*30}Menu - press Left and Right to change")
        print("\n" * 5)
        for i in range(len(self.keys)):
            print(end="")
            colored_key = colored(self.keys[i], "red" if i == self.option else "white")
            if self.option == i:
                if self.keys[i] == "Graphic":
                    # graphic_option: int = self.list_setting["Graphic"][-1]
                    print(f"{" "*15}[{colored_key}]{" "*(14 - len(self.keys[i]))}: [{self.graphic[self.list_setting["Graphic"]]}]")

                elif self.keys[i] == "Fps":
                    # fps_option: int = self.list_setting["Fps"][-1]
                    print(f"{" "*15}[{colored_key}]{" "*(14 - len(self.keys[i]))}: [{self.fps[self.list_setting["Fps"]]}]")

                elif self.keys[i] == "Task":
                    print(f"{" "*60}{colored("Quit",on_color="on_red")}{" "*5}Save" if self.list_setting["Task"] == 0 else f"{" "*60}Quit{" "*5}{colored("Save",on_color="on_green")}")
                    if keyboard.read_key() == "enter" and self.list_setting["Task"] == 1:
                        self.save_config("configs.txt")
                        MainMenu().main_menu()


                else:
                    print(f"{" "*15}[{colored_key} - {int(self.list_setting[self.keys[i]]*100/10)}%]{" "*(6 - len(self.keys[i]))} : {colored(' * ' * self.list_setting[self.keys[i]], 'white', 'on_white')}")

            else:
                if self.keys[i] == "Graphic":
                    # graphic_option: int = self.list_setting["Graphic"][-1]
                    print(f"{" "*16}{colored_key}{" "*(15 - len(self.keys[i]))}: [{self.graphic[self.list_setting["Graphic"]]}]")

                elif self.keys[i] == "Fps":
                    # fps_option: int = self.list_setting["Fps"][-1]
                    print(f"{" "*16}{colored_key}{" "*(15 - len(self.keys[i]))}: [{self.fps[self.list_setting["Fps"]]}]")

                elif self.keys[i] == "Task":
                    print(f"{" "*60}Quit{" "*5}Save")
                    pass
                # elif self.keys[i] == "Save":
                #     print(f"{" "*60}{colored_key}")
                # elif self.keys[i] == "Back":
                #     print(f"{" "*60}  {colored_key}")
                else:
                    print(f"{" "*16}{colored_key} - {int(self.list_setting[self.keys[i]]*100/10)}%{" "*(8 - len(self.keys[i]))}: {colored(' * ' * self.list_setting[self.keys[i]], 'white', 'on_white')}")
            print("\n" * 2)

    def start(self) -> None:
        """Start setting menu """
        self.display_menu()
        # self.music.player()
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'up' and self.option > 0:
                    self.option -= 1
                elif event.name == 'down' and self.option < len(self.list_setting) - 1:
                    self.option += 1
                elif event.name == 'left':
                    self.update_setting(-1)
                elif event.name == 'right':
                    self.update_setting(1)
                # self.sfx.player()
                self.display_menu()


