from os import system
from time import sleep
from pygame import mixer
from string import ascii_letters
from random import choice
from termcolor import colored


def add_music() -> None:
    mixer.init()
    mixer.music.load('sources/2_Unlimited_-_Get_Ready_For_This_Orchestral_Mix.mp3')
    mixer.music.play()


def find_the_word(word: str) -> None:
    full_list = [_ for _ in ascii_letters]
    full_list.extend([',', '!', '?', ' '])
    full_colors_list = ["red", "green", "yellow", "blue", "magenta", "cyan", "light_red",
                        "light_green", "light_yellow", "light_blue", "light_magenta",
                        "light_cyan"]
    c_word = ""
    while len(c_word) != len(word):
        lst = full_list.copy()
        while True:
            i = choice(range(len(lst)))
            print(c_word, end="")
            print(colored(lst[i], choice(full_colors_list)))
            sleep(0.035)
            system("cls")
            if lst[i] == word[len(c_word)]:
                c_word += lst[i]
                break
            else:
                lst.pop(i)


def add_border(word: str) -> None:
    first = True
    main_index = 0
    full_colors_list = ["light_red", "red", "light_yellow", "light_green", "light_cyan", "light_blue", "light_magenta"]
    while mixer.music.get_busy():
        main_index = main_index - 1 if main_index > 0 else 6
        index = main_index
        for i in range(5):
            print(colored("_", full_colors_list[index]), end="")
            index = index + 1 if index < 6 else 0
        for i in range(len(word)):
            print(colored("_", full_colors_list[index]), end="")
            index = index + 1 if index < 6 else 0
        for i in range(9):
            print(colored("_", full_colors_list[index]), end="")
            index = index + 1 if index < 6 else 0
        if first: sleep(0.5)
        print()
        print(colored("|", full_colors_list[(index + 30 + len(word)) % 7]), " " * (10 + len(word)),
              colored("|", full_colors_list[index]), end="")
        index = index + 1 if index < 6 else 0
        if first: sleep(0.5)
        print()
        print(colored("|", full_colors_list[(index + 28 + len(word)) % 7]), " " * (10 + len(word)),
              colored("|", full_colors_list[index]), end="")
        index = index + 1 if index < 6 else 0
        if first: sleep(0.5)
        print()
        print(colored("|", full_colors_list[(index + 26 + len(word)) % 7]), " " * 4, word, " " * 4,
              colored("|", full_colors_list[index]), end="")
        index = index + 1 if index < 6 else 0
        if first: sleep(0.5)
        print()
        print(colored("|", full_colors_list[(index + 24 + len(word)) % 7]), " " * (10 + len(word)),
              colored("|", full_colors_list[index]), end="")
        index = index + 1 if index < 6 else 0
        if first: sleep(0.5)
        print()
        print(colored("|", full_colors_list[(index + 22 + len(word)) % 7]), " " * (10 + len(word)),
              colored("|", full_colors_list[index]), end="")
        index = index + 1 if index < 6 else 0
        if first: sleep(0.5)
        print()
        index += 13 + len(word)
        index %= 7
        for i in range(5, 0, -1):
            print(colored("–", full_colors_list[index]), end="")
            index = index - 1 if index > 0 else 6
        for i in range(len(word), 0, -1):
            print(colored("–", full_colors_list[index]), end="")
            index = index - 1 if index > 0 else 6
        for i in range(9, 0, -1):
            print(colored("–", full_colors_list[index]), end="")
            index = index - 1 if index > 0 else 6
        if first: sleep(0.5)
        print()
        sleep(0.15)
        system("cls")
        first = False


def end() -> None:
    print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿
⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿""")


def main(word: str) -> None:
    add_music()
    find_the_word(word)
    add_border(word)
    end()


if __name__ == "__main__":
    system("cls")
    user_word = input("""Список разрешённых символов: A...Z a...z ,   ! ?
Введите вашу фразу: """)
    system("cls")
    main(user_word)
