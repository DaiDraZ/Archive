
import pygame
import random


pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()


class load_file():
    def __init__(self) -> None:
        self.list_setting: dict = self.load_config("configs.txt")

    def load_config(self, config_file: str):
        config = {}
        with open(config_file, "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                config[key] = int(float(value) * 10) if key in ["Music", "Sfx", "Font"] else int(value)
        return config

# config_data = load_file().load_config("configs.txt")


class SFX():
    def __init__(self) -> None:
        self.text_sould = pygame.mixer.Sound(f"walk.mp3")
        self.set_typing_sound_volumes = self.text_sould.set_volume

        self.sfx_typing = pygame.mixer.Sound(f"typing{random.randint(0,3)}.mp3")
        self.set_sfx_typing_volums = self.sfx_typing.set_volume

        # Set volume event first time
        self.config_data = load_file().load_config("configs.txt")
        self.set_volumes(self.config_data["Sfx"])

    def set_volumes(self, volumes: float):
        self.set_typing_sound_volumes(volumes)
        self.set_sfx_typing_volums(volumes)

    def player_walking(self):
        self.text_sould.play()

    def player_typing(self):
        self.sfx_typing.play()


class MUSIC():
    def __init__(self) -> None:
        # pygame.mixer.music.load("Accel World - Way Home.mp3")
        self.game_music = pygame.mixer.music 
        self.game_music.load("retro_game.mp3")
        self.volumes = pygame.mixer.music.set_volume

        # Set volume event first time
        self.config_data = load_file().load_config("configs.txt")
        self.set_volumes(self.config_data["Music"])

    def set_volumes(self, volumes: float):
        self.volumes(volumes)

    def change_music(self, name: str):
        self.game_music.load(name)
        self.player()

    def player(self):
        if not self.game_music.get_busy():
            self.game_music.play(-1)


# class update_volume():
#     def __init__(self) -> None:
#         if __name__ == "__main__":
#             config_data = load_file().load_config("configs.txt")
#             MUSIC().set_volumes(config_data["Music"])
#             SFX().set_volumes(config_data["Sfx"])
