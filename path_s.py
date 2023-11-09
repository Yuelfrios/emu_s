from keyboard import KEY_DOWN, hook, wait
from pyautogui import press
from time import sleep
barcode_data = ""
target_sequence = "123456"

def on_key_event(e):
    global barcode_data
    if e.event_type == KEY_DOWN:
        barcode_data += e.name
        if barcode_data.endswith(target_sequence):
            sleep(0.500)
            press('s')

hook(on_key_event)

wait('esc')