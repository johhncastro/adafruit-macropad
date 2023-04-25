import adafruit_hid.keyboard as keyboard
from adafruit_hid.keycode import Keycode
import time
from bongo.bongo import Bongo


# Create a keyboard object to detect key presses
kbd = keyboard.Keyboard()


def my_macro(event):
    print(f"Key pressed: {event.key_number}")

# Loop indefinitely
while True:
    # Call run_bongo_animation() to check for key presses and update the sprite
    run_bongo_animation()
