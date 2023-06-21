import pyautogui
from time import sleep


def comand_one():
    sleep(3)
    pyautogui.hotkey('win', 'r')
    sleep(2)
    pyautogui.write('prefetch')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.hotkey('delete')
    sleep(3)
    pyautogui.click(x=493, y=280, clicks=1)
    sleep(2)
    pyautogui.click(x=717, y=314, clicks=1)
    sleep(3)
    pyautogui.click(x=1253, y=62, clicks=1)


def comand_two():
    sleep(3)
    pyautogui.hotkey('win', 'r')
    sleep(2)
    pyautogui.write('temp')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.hotkey('delete')
    sleep(3)
    pyautogui.click(x=493, y=280, clicks=1)
    sleep(2)
    pyautogui.click(x=717, y=314, clicks=1)
    sleep(3)
    pyautogui.click(x=493, y=280, clicks=1)
    sleep(2)
    pyautogui.click(x=716, y=277, clicks=1)
    sleep(2)
    pyautogui.click(x=1248, y=67)


def comand_three():
    sleep(3)
    pyautogui.hotkey('win', 'r')
    sleep(2)
    pyautogui.write('%temp%')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.hotkey('delete')
    sleep(3)
    pyautogui.click(x=493, y=280, clicks=1)
    sleep(2)
    pyautogui.click(x=717, y=314, clicks=1)
    sleep(2)
    pyautogui.click(x=1248, y=67)


def comand_four():
    sleep(3)
    pyautogui.hotkey('win', 'r')
    sleep(2)
    pyautogui.write('cleanmgr')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.click(x=255, y=509, clicks=1)
    sleep(10)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.click(x=276, y=474, clicks=1)
    sleep(2)
    pyautogui.click(x=681, y=389, clicks=1)
    sleep(15)
    pyautogui.click(x=1136, y=150, clicks=1)


def comand_five():
    sleep(3)
    pyautogui.click(x=35, y=36, clicks=2)
    sleep(3)
    pyautogui.hotkey('ctrl', 'a')
    sleep(2)
    pyautogui.hotkey('delete')
    sleep(2)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.click(x=1263, y=64, clicks=1)


def comand_six():
    sleep(3)
    pyautogui.click(button="right")
    sleep(2)
    pyautogui.click(x=1039, y=122, clicks=1)
