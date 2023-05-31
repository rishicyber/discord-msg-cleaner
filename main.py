from pyautogui import click, hotkey, press, PAUSE
from time import sleep

sleep(2)

PAUSE = 0.1

while True:
    press(["up"])
    hotkey('ctrl', 'a')
    press(["backspace"])
    press(["enter"])
    press(["enter"])
    click()

