import pyautogui
from time import sleep

# Função auxiliar usada somente para captar a posição do mouse.


def position_mouse():
    sleep(5)
    position = pyautogui.position()
    print(position)


position_mouse()
