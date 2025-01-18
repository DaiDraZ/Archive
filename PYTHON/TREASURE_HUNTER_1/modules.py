import random
import os
import sys
import shutil
import ctypes
from termcolor import colored
import time
import colorama 
from colorama import Fore, Style
import keyboard
import pygame
from sound import MUSIC, SFX

# Auto reload color in CMD
colorama.init(autoreset=True)
os.system("color")


# Khởi tạo Pygame
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()


def clear_console():
    """Clear console"""
    print("\033[H\033[J", end="")  # Di chuyển con trỏ về đầu và xóa màn hình.


def type_effect(text, delay=0.1):
    """
    Text run 

    Args:
    - text (str)
    - delay (float) (s)
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 


def fade_in_text(text, delay=0.05, steps=10):
    """
    Hiệu ứng chữ từ trong suốt (mờ) đến rõ ràng cho nhiều dòng văn bản.\n

    Args:\n
    - text (str)\n
    - delay (float) (s).\n
    - steps (int)
    """

    lines = text.splitlines()
    num_lines = len(lines)

    # opacity
    opacity_levels = [
        f"\033[38;2;{int(255 * (i / steps))};{int(255 * (i / steps))};{int(255 * (i / steps))}m"
        for i in range(steps + 1)
    ]

    # fade-in effect
    for i in range(steps + 1):
        for line in lines:
            print(opacity_levels[i] + line + "\033[0m")
        time.sleep(delay)
        # Đưa con trỏ lên lại để in đè các dòng (nếu không phải bước cuối)
        if i < steps:
            print(f"\033[{num_lines}F", end='')  # Quay lại số dòng tương ứng
    time.sleep(1.5)


class Menu():
    """Menu game"""

    def __init__(self) -> None:
        self.menus = ['New game', 'Continue', 'Option', 'Credit']
        self.colors: list[str] = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        self.attributes = ["bold", "dark", "underline", "blink", "reverse", "concealed"]
        self.logo = [r'''
          _____   ____    _____      _      ____    _   _   ____    _____     _   _   _   _   _   _   _____   _____   ____  
         |_   _| |  _ \  | ____|    / \    / ___|  | | | | |  _ \  | ____|   | | | | | | | | | \ | | |_   _| | ____| |  _ \ 
           | |   | |_) | |  _|     / _ \   \___ \  | | | | | |_) | |  _|     | |_| | | | | | |  \| |   | |   |  _|   | |_) |
           | |   |  _ <  | |___   / ___ \   ___) | | |_| | |  _ <  | |___    |  _  | | |_| | | |\  |   | |   | |___  |  _ < 
           |_|   |_| \_\ |_____| /_/   \_\ |____/   \___/  |_| \_\ |_____|   |_| |_|  \___/  |_| \_|   |_|   |_____| |_| \_\.'''
                     ]

    def display_menu(self, selected_index: int):
        clear_console()
        print(colored(self.logo[0], 'yellow', attrs=["bold"]), '\n' * 10)
        # for i in range(len(self.logo[0])):
        #     color = random.choice(self.colors)
        #     print(colored(self.logo[0][i], "yellow", attrs=["blink","bold"]),end="")
        # print("\n"*10)

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
                SFX().player_typing()
                if event.name == 'up':
                    selected_index -= 1
                    if selected_index < 0:
                        selected_index = len(self.menus) - 1
                elif event.name == 'down':
                    selected_index += 1
                    if selected_index > len(self.menus) - 1:
                        selected_index = 0
                elif event.name == 'enter':
                    if selected_index == 0:
                        clear_console()
                    elif selected_index == 1:
                        pass
                    elif selected_index == 2:
                        Setting().start()  
                    elif selected_index == 3:
                        intro.display()

                self.display_menu(selected_index)  # Update menu


class Setting():
    """Setting game"""

    def __init__(self) -> None:
        self.list_setting: dict = self.load_config("configs.txt")
        self.song_list = ["A Bird Story - Mud Dash.mp3", "A Witch's Tale.mp3", "Accel World - Way Home.mp3", "retro_game.mp3"]
        self.graphic = ["Full screen", "1280x720", "800x600"]
        self.fps = [60, 45, 30]
        self.option: int = 0
        self.keys: list = list(self.list_setting.keys())
        # self.music_player = MUSIC()  
        # self.sfx_player = SFX()

    def load_config(self, config_file: str):
        """Loading file config"""
        config = {}
        with open(config_file, "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                config[key] = int(float(value) * 10) if key in ["Music", "Sfx", "Font"] else int(value)
        return config

    def save_config(self, config_file: str):
        """Record dictionary setting to file config.txt """
        try:
            with open(config_file, "w") as file:
                for key, value in self.list_setting.items():
                    if key in ["Music", "Sfx", "Font"]:
                        file.write(f"{key}: {value/10}\n")
                    else:
                        file.write(f"{key}: {value}\n")
        except Exception as e:
            print(f"Không thể lưu cài đặt: {e}")
        clear_console() 

    def update_setting(self, change: int):
        if self.keys[self.option] == "Graphic":
            self.list_setting["Graphic"] += change
            if self.list_setting["Graphic"] < 0:
                self.list_setting["Graphic"] = len(self.graphic) - 1
            elif self.list_setting["Graphic"] > len(self.graphic) - 1:
                self.list_setting["Graphic"] = 0

            # self.list_setting["Graphic"] = max(0, min(2, self.list_setting["Graphic"]))
            if self.list_setting["Graphic"] == 0:
                # self.set_fullscreen()
                os.system(f"mode con: cols={int(screen_width/font_size[0]) - 3} lines={int(screen_height/font_size[1]) - 4}")
            elif self.list_setting["Graphic"] == 1:
                # self.set_window_size(int(1080/font_size[0]) - 3, int(720/font_size[1]) - 4)
                os.system(f"mode con: cols={int(1080/font_size[0]) - 3} lines={int(720/font_size[1]) - 4}")
            elif self.list_setting["Graphic"] == 2:
                # self.set_window_size(int(800/font_size[0]) - 3, int(600/font_size[1]) - 4)
                os.system(f"mode con: cols={int(800/font_size[0]) - 3} lines={int(600/font_size[1]) - 4}")

        elif self.keys[self.option] == "Fps":
            self.list_setting["Fps"] += change
            if self.list_setting["Fps"] < 0:
                self.list_setting["Fps"] = len(self.fps) - 1
            elif self.list_setting["Fps"] > len(self.fps) - 1:
                self.list_setting["Fps"] = 0
            # self.list_setting["Fps"] = max(0, min(2, self.list_setting["Fps"]))

        elif self.keys[self.option] == "Task":
            self.list_setting["Task"] += change
            self.list_setting["Task"] = max(0, min(1, self.list_setting["Task"]))

        elif self.keys[self.option] == "Font":
            self.list_setting[self.keys[self.option]] += change
            self.list_setting[self.keys[self.option]] = max(0, min(10, self.list_setting[self.keys[self.option]]))

        elif self.keys[self.option] == "Song":
            self.list_setting[self.keys[self.option]] += change
            self.list_setting[self.keys[self.option]] = max(0, min(len(self.song_list) - 1, self.list_setting[self.keys[self.option]]))
            GAME_MUSIC.change_music(self.song_list[self.list_setting["Song"]])
            pass

        else:
            self.list_setting[self.keys[self.option]] += change
            self.list_setting[self.keys[self.option]] = max(0, min(10, self.list_setting[self.keys[self.option]]))
            # Update volume after change
            if self.keys[self.option] == "Music":
                GAME_MUSIC.set_volumes(self.list_setting[self.keys[self.option]] / 10)
            if self.keys[self.option] == "Sfx":
                GAME_SFX.set_volumes(self.list_setting[self.keys[self.option]] / 10)

    def display_menu(self):
        clear_console()
        print(f"{" "*30}Setting - press Left and Right to change", "\n" * 5)
        for i in range(len(self.keys)):
            print(end="")
            colored_key = colored(self.keys[i], "red" if i == self.option else "white")
            if self.option == i:
                if self.keys[i] == "Song":
                    # graphic_option: int = self.list_setting["Graphic"][-1]
                    print(f"{" "*15}[{colored_key}]{" "*(14 - len(self.keys[i]))}: {self.song_list[self.list_setting["Song"]]}")

                elif self.keys[i] == "Graphic":
                    # graphic_option: int = self.list_setting["Graphic"][-1]
                    print(f"{" "*15}[{colored_key}]{" "*(14 - len(self.keys[i]))}: [{self.graphic[self.list_setting["Graphic"]]}]")

                elif self.keys[i] == "Fps":
                    # fps_option: int = self.list_setting["Fps"][-1]
                    print(f"{" "*15}[{colored_key}]{" "*(14 - len(self.keys[i]))}: [{self.fps[self.list_setting["Fps"]]}]")

                elif self.keys[i] == "Task":
                    print(f"{" "*60}{colored("Quit",on_color="on_red")}{" "*5}Save" if self.list_setting["Task"] == 0 else f"{" "*60}Quit{" "*5}{colored("Save",on_color="on_green")}")
                    if keyboard.read_key() == "enter":
                        if self.list_setting["Task"] == 1:
                            self.save_config("configs.txt")
                        Menu().show()
                else:
                    print(f"{" "*15}[{colored_key} - {int(self.list_setting[self.keys[i]]*100/10)}%]{" "*(6 - len(self.keys[i]))} : {colored(' * ' * self.list_setting[self.keys[i]], 'white', 'on_white')}")

            else:
                if self.keys[i] == "Song":
                    print(f"{" "*16}{colored_key}{" "*(15 - len(self.keys[i]))}: {self.song_list[self.list_setting["Song"]]}")

                elif self.keys[i] == "Graphic":
                    print(f"{" "*16}{colored_key}{" "*(15 - len(self.keys[i]))}: [{self.graphic[self.list_setting["Graphic"]]}]")

                elif self.keys[i] == "Fps":
                    print(f"{" "*16}{colored_key}{" "*(15 - len(self.keys[i]))}: [{self.fps[self.list_setting["Fps"]]}]")

                elif self.keys[i] == "Task":
                    print(f"{" "*60}Quit{" "*5}Save")

                else:
                    print(f"{" "*16}{colored_key} - {int(self.list_setting[self.keys[i]]*100/10)}%{" "*(8 - len(self.keys[i]))}: {colored(' * ' * self.list_setting[self.keys[i]], 'white', 'on_white')}")
            print("\n")

    def start(self) -> None:
        """Start setting menu """
        self.display_menu()
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                GAME_SFX.player_walking()
                if event.name == 'up' and self.option > 0:
                    self.option -= 1
                elif event.name == 'down' and self.option < len(self.list_setting) - 1:
                    self.option += 1
                elif event.name == 'left':
                    self.update_setting(-1)
                elif event.name == 'right':
                    self.update_setting(1)
                self.display_menu()


class Intro():
    """Start first time,load logo game"""

    def __init__(self) -> None:
        self.maps: list = [["@" for i in range(0, 51)] for j in range(0, 10)]
        self.colors: list = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

    def init_map(self):
        x, y = 25, 25
        name: str = "TREASURE HUNTER"
        author: str = "Devevelop By TRUONG VAN DAI"
        l, r = 7, 7
        while x >= 0:
            print("\n" * 10)
            for i in self.maps:
                print(" " * 20, end="")
                for j in i:
                    sys.stdout.write(colored(j, random.choice(self.colors),))
                    print(end=" ")
                print(end="\n")

            time.sleep(0.05)
            clear_console()
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
            print(" " * 30, end="")
            for j in i:
                sys.stdout.write(colored(j, random.choice(self.colors)))
                print(end=" ")
            print(end="\n")
        print(" " * 60, "Ver 1.0.0", "\n", " " * 55, end="")
        for i in author:
            print(colored(i, "green"), end="", flush=True)
            GAME_SFX.player_walking()
            time.sleep(0.15)
        time.sleep(0.5)
        os.system("cls")
        # clear_console()

    def start(self):
        self.init_map()

    def clean(self):
        clear_console()


class Loading():
    def __init__(self) -> None:
        self.percent: int = 0
        self.dot: list[str] = [".", "..", "..."]
        self.load: list[str] = [">_<", "o_o", ">_<"]
        self.src = [
            "load_CONFIG_SETTINGS", "get_USER_PERMISSIONS", "load_DATABASE_CONNECTION",
            "check_DISK_SPACE", "load_LOG_FILE", "get_ACTIVE_SESSIONS", "load_USER_PROFILE",
            "check_API_STATUS", "get_APPLICATION_VERSION", "load_SESSION_DATA",
            "check_MEMORY_USAGE", "load_ENVIRONMENT_VARIABLES", "get_USER_INPUT",
            "load_SECURITY_SETTINGS", "check_SERVICE_HEALTH", "load_PLUGIN_LIST", "get_SYSTEM_LOGS",
            "load_NETWORK_CONFIG", "check_FIREWALL_SETTINGS", "get_PROCESS_LIST", "load_ERROR_HANDLING",
            "check_UPDATE_AVAILABLE", "load_CACHE_SETTINGS", "get_SYSTEM_MAINTENANCE",
            "load_MODULE_DEPENDENCIES", "check_USER_ACTIVITY", "get_PERFORMANCE_METRICS",
            "load_ASSET_MANAGEMENT", "check_DATABASE_INTEGRITY", "get_NOTIFICATION_SETTINGS",
            "load_ACCESS_LOGS", "check_SYSTEM_UPDATES", "get_CLOUD_STORAGE_INFO",
            "load_EMAIL_SETTINGS", "check_VPN_CONNECTION", "get_HARDWARE_INFO",
            "load_BACKUP_CONFIG", "check_USER_SESSION_TIMEOUT", "get_API_KEYS",
            "load_CRON_JOBS", "check_SYSTEM_SECURITY", "get_APPLICATION_LOGS",
            "load_DEPLOYMENT_INFO", "check_MEMORY_LIMITS", "get_SERVICE_STATUS",
            "load_BACKEND_SERVICES", "check_LOAD_BALANCER", "get_SSL_CERTIFICATES",
            "load_USER_ACTIVITY_LOG", "check_NETWORK_TRAFFIC", "get_THROUGHPUT_METRICS",
            "load_USER_SESSION_DATA", "check_DISK_USAGE", "get_TROUBLESHOOTING_GUIDE",
            "load_EXPORT_SETTINGS", "check_DATA_COMPLIANCE", "get_SYSTEM_NOTIFICATIONS",
            "load_PERFORMANCE_LOGS", "check_SERVICE_DEPENDENCIES", "get_DASHBOARD_DATA",
            "load_SESSION_ACTIVITY", "check_CACHE_HIT_RATIO", "get_SERVICE_PROVIDER_INFO",
            "load_USER_FEEDBACK", "check_SYSTEM_BACKUPS", "get_PROCESS_MONITORING",
            "load_DEPENDENCY_GRAPH", "check_SYSTEM_RESTART",
            "get_USER_AUTHENTICATION", "load_ASSET_TRACKING", "check_SCHEDULED_TASKS",
            "get_API_USAGE_STATS", "load_FILE_SYSTEM_INFO", "check_APPLICATION_LOGGING",
            "get_NETWORK_TOPOLOGY", "load_USER_SETTINGS", "check_MEMORY_ALLOCATIONS", "get_SYSTEM_CONFIG",
            "load_CRASH_REPORTS", "check_HEALTH_CHECKS", "get_PERFORMANCE_PROFILES",
            "load_DATA_ANALYTICS", "check_USER_PRIVILEGES", "get_APPLICATION_ENDPOINTS",
            "load_SERVICE_LOGS", "check_INTEGRATION_STATUS", "get_DEPLOYMENT_STATUS",
            "load_CACHE_MEMORY", "check_NETWORK_MONITORING",
            "get_SYSTEM_AUDIT_LOGS", "load_CONNECTION_POOL", "check_ERROR_LOGS",
            "get_SYSTEM_RESOURCE_USAGE", "load_MODULE_CONFIG", "check_APPLICATION_PERFORMANCE",
            "get_NETWORK_BANDWIDTH", "load_ACCESS_CONTROL_LIST", "check_SERVICE_LOGGING",
            "get_SYSTEM_MONITORING",
            "load_APPLICATION_SETTINGS",
            "check_DATABASE_CONNECTIONS",
            "get_API_ENDPOINTS",
            "load_TROUBLESHOOTING_LOGS",
            "check_LOAD_BALANCING",
            "get_USER_NOTIFICATION_SETTINGS",
            "load_SERVICE_MONITORING",
            "check_SYSTEM_SETTINGS",
            "get_APPLICATION_DEPENDENCIES",
            "load_SYSTEM_BACKUP_LOGS",
            "check_DATA_BACKUP",
            "get_SYSTEM_UPTIME",
            "load_SESSION_LOGS",
            "check_USER_ACCESS",
            "get_SERVER_HEALTH_CHECK",
            "load_SECURITY_AUDIT_LOGS",
            "check_APPLICATION_STATUS",
            "get_SCRIPT_EXECUTION_LOGS",
            "load_NETWORK_ACTIVITY_LOGS",
            "check_RESOURCE_ALLOCATION"]
        self.x: int = 0
        self.y: int = 0

    def start(self):
        while self.percent <= 100:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n" * 5, " " * 65, colored("Welcome to the VN_studio " + self.load[self.x], "white", "on_blue"), "\n" * 15)
            print(" " * 70, colored("Loading" + self.dot[self.x], "white"))

            self.x = (self.x + 1) % len(self.load)
            self.y = (self.y + 1) % len(self.src)

            self.percent += random.randint(0, 8)
            if self.percent >= 100:
                clear_console()
                print("\n" * 5, " " * 65, colored("Welcome to the VN_studio >.<", "white", "on_blue"), "\n" * 15)
                print(" " * 55, colored("Loading success !", "white"))
                print(" " * 50, "[", colored("=" * 50, "green", "on_green"), "] 100%")
                time.sleep(2.5)
                os.system("cls" if os.name == "nt" else "clear")
                break

            print(
                " " * 50,
                "[ ",
                colored("=" * (self.percent // 2), "green", "on_green"),
                " " * ((100 - self.percent) // 2),
                "] ",
                self.percent,
                "%\n", " " * 80, f"{self.src[self.y]}")
            time.sleep(0.5)

        os.system("cls" if os.name == "nt" else "clear")
        print("\n" * 5, " " * 65, colored("Welcome to the VN_studio >.<", "white", "on_blue"), "\n" * 15)
        print(" " * 55, colored("Loading success !", "white"))
        print(" " * 50, "[", colored("=" * 50, "green", "on_green"), "] 100%")
        time.sleep(2.5)
        clear_console()


class Introduce:
    def __init__(self, title, crew, display_height=5, scroll_speed=0.2):
        self.title = title
        self.crew = crew
        self.display_height = display_height
        self.scroll_speed = scroll_speed
        self.lines = self._prepare_lines()

    def _prepare_lines(self):
        full_text = self.title + "\n" + "\n".join(self.crew) + "\n"
        lines = full_text.splitlines()
        lines += [""] * self.display_height  
        return lines

    def display(self):
        """
        Display the scrolling text with color and smooth effects.
        Link : "https://en.wikipedia.org/wiki/ANSI_escape_code"

        """
        max_line_length = max(len(line) for line in self.lines)
        while True:
            for offset in range(len(self.lines) + self.display_height):
                clear_console()
                print("\n" * 5)
                # Render lines with padding
                for i in range(self.display_height):
                    print("\n" * 3)  # Add top padding for better spacing
                    line_index = offset + i - self.display_height
                    if 0 <= line_index < len(self.lines):
                        # Add a fading color effect
                        color_effect = Fore.LIGHTBLUE_EX if i % 2 == 0 else Fore.LIGHTCYAN_EX
                        print(" " * 40 + color_effect + self.lines[line_index].ljust(max_line_length))
                    else:
                        print(" " * 40)

                # Adjust scroll speed
                time.sleep(self.scroll_speed)
            break
        clear_console()
        fade_in_text(logo)
        fade_in_text(thankyou)
        time.sleep(5)

        Menu().show()


# Define content
title = f"{Fore.CYAN}{Style.BRIGHT}INTRODUCING THE CREATIVE GAME DEV\n"
crew = [
    f"{Fore.GREEN}Director: {Fore.YELLOW}DAI DRA",
    f"{Fore.GREEN}Screenwriter: {Fore.YELLOW}HOANG LE",
    f"{Fore.GREEN}Producer: {Fore.YELLOW}DAI DRA",
    f"{Fore.GREEN}Cinematographer: {Fore.YELLOW}TAM TY",
    f"{Fore.GREEN}Sound Designer: {Fore.YELLOW}TUNG SNoWELL",
    f"{Fore.GREEN}Editor: {Fore.YELLOW}MINH TELLer",
    f"{Fore.GREEN}Code Writer: {Fore.YELLOW}DAI DRA",
    f"{Fore.GREEN}Tester: {Fore.YELLOW}DAI DRA,HOANG LE,TAM TY,TUNG SNoWELL,MINH TELLer",
    f"{Fore.MAGENTA}{Style.BRIGHT}\033[4mEND"
]

logo: str = rf"""{Fore.YELLOW}
                  ______                                               __  __               __             
                 /_  __/_____ ___   ____ _ _____ __  __ _____ ___     / / / /__  __ ____   / /_ ___   _____
                  / /  / ___// _ \ / __ `// ___// / / // ___// _ \   / /_/ // / / // __ \ / __// _ \ / ___/
                 / /  / /   /  __// /_/ /(__  )/ /_/ // /   /  __/  / __  // /_/ // / / // /_ /  __// /    
                /_/  /_/    \___/ \__,_//____/ \__,_//_/    \___/  /_/ /_/ \__,_//_/ /_/ \__/ \___//_/     
"""                                                                                        

thankyou: str = rf"""{Fore.GREEN}
 _____  _                    _                           
|_   _|| |                  | |                          
  | |  | |__    __ _  _ __  | | __  _   _   ___   _   _  
  | |  | '_ \  / _` || '_ \ | |/ / | | | | / _ \ | | | | 
  | |  | | | || (_| || | | ||   <  | |_| || (_) || |_| | 
  \_/  |_| |_| \__,_||_| |_||_|\_\  \__, | \___/  \__,_| 
                                     __/ |               
                                    |___/                
                              __                      _                _               
                             / _|                    | |              (_)              
                            | |_  ___   _ __   _ __  | |  __ _  _   _  _  _ __    __ _ 
                            |  _|/ _ \ | '__| | '_ \ | | / _` || | | || || '_ \  / _` |
                            | | | (_) || |    | |_) || || (_| || |_| || || | | || (_| |
                            |_|  \___/ |_|    | .__/ |_| \__,_| \__, ||_||_| |_| \__, |
                                              | |                __/ |            __/ |
                                              |_|               |___/            |___/ 
 _____   ___  ___  ___ _____ 
|  __ \ / _ \ |  \/  ||  ___|
| |  \// /_\ \| .  . || |__  
| | __ |  _  || |\/| ||  __| 
| |_\ \| | | || |  | || |___ 
 \____/\_| |_/\_|  |_/\____/ 
                             
"""

# lay font size cmd
# --------------------------------{{{


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short),  # Tọa độ X
                ("Y", ctypes.c_short)]  # Tọa độ Y

# Định nghĩa cấu trúc CONSOLE_FONT_INFOEX


class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_ulong),
        ("nFont", ctypes.c_ulong),
        ("dwFontSize", COORD),  
        ("FontFamily", ctypes.c_uint),
        ("FontWeight", ctypes.c_uint),
        ("FaceName", ctypes.c_wchar * 32),
    ]


def get_console_font_size():
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
    font_info = CONSOLE_FONT_INFOEX()
    font_info.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    success = kernel32.GetCurrentConsoleFontEx(handle, ctypes.c_bool(False), ctypes.byref(font_info))
    if success:
        return (font_info.dwFontSize.X, font_info.dwFontSize.Y)  # Width, Height
    else:
        return None


def set_window_size(width: int, height: int):
    """
    Set the CMD window size on Windows using the Windows API.

    Args:
        width (int): Width of the CMD window in columns.
        height (int): Height of the CMD window in rows.
    """
    # Structure to store console screen buffer information
    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class SMALL_RECT(ctypes.Structure):
        _fields_ = [("Left", ctypes.c_short), 
                    ("Top", ctypes.c_short), 
                    ("Right", ctypes.c_short), 
                    ("Bottom", ctypes.c_short)]

    class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
        _fields_ = [("dwSize", COORD),
                    ("dwCursorPosition", COORD),
                    ("wAttributes", ctypes.c_ushort),
                    ("srWindow", SMALL_RECT),
                    ("dwMaximumWindowSize", COORD)]

    # Load Windows API functions
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    hConsole = kernel32.GetStdHandle(-11)  # -11 = STD_OUTPUT_HANDLE

    # Get current console buffer info
    csbi = CONSOLE_SCREEN_BUFFER_INFO()
    kernel32.GetConsoleScreenBufferInfo(hConsole, ctypes.byref(csbi))

    # Adjust buffer size
    new_buffer_size = COORD(width, height)
    kernel32.SetConsoleScreenBufferSize(hConsole, new_buffer_size)

    # Adjust window size
    new_window = SMALL_RECT(0, 0, width - 1, height - 1)
    kernel32.SetConsoleWindowInfo(hConsole, ctypes.c_bool(True), ctypes.byref(new_window))


def set_fullscreen():
    """
    Set CMD window to fullscreen mode on Windows.
    """
    # Check if running on Windows
    if os.name == 'nt':
        # Get a handle to the console window
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        hwnd = kernel32.GetConsoleWindow()

        if hwnd:
            user32.ShowWindow(hwnd, 3)  # 3 = SW_MAXIMIZE (fullscreen)
        else:
            print("Unable to detect console window handle.")


font_size = get_console_font_size()
user32 = ctypes.windll.user32
screen_width: int = user32.GetSystemMetrics(0)  # Chiều rộng màn hình
screen_height: int = user32.GetSystemMetrics(1)  # Chiều cao màn hình

# -------------------------------------}}}

if __name__ == "__main__":
    intro = Introduce(title, crew, display_height=5, scroll_speed=0.65)
    GAME_MUSIC = MUSIC()
    GAME_SFX = SFX()
    GAME_MUSIC.player()
    Intro().start()
    Loading().start()
    Menu().show()
    Setting().start()
