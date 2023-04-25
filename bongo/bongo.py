# SPDX-License-Identifier: MIT

import board
import displayio
import adafruit_imageload
import adafruit_hid.keyboard as keyboard
from adafruit_hid.keycode import Keycode
from adafruit_macropad import MacroPad
import time


# Create a display object
display = board.DISPLAY

# Load the BMP image
bitmap, palette = adafruit_imageload.load("/bongo/bongo.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)

# Calculate the width and height of each sprite
sprite_width = 57  # Replace with the width of each sprite in pixels
sprite_height = 35  # Replace with the height of each sprite in pixels

# Calculate the number of sprites in the sprite sheet
num_sprites = 8  # Replace with the number of sprites in the sprite sheet

# Create a Group object to hold the Bitmap object
group = displayio.Group()

# Add the first sprite to the Group
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, width=1, height=1, tile_width=sprite_width, tile_height=sprite_height, default_tile=0)
group.append(tile_grid)

# Display the Group on the MacroPad's display
display.show(group)

# Define a function to update the sprite animation
def update_animation(current_sprite):
    # Calculate the x and y coordinates of the current sprite in the sprite sheet
    sprite_x = (current_sprite % (bitmap.width // sprite_width)) * sprite_width
    sprite_y = (current_sprite // (bitmap.width // sprite_width)) * sprite_height

    # Update the TileGrid to display the current sprite
    tile_grid[0] = (sprite_x, sprite_y, sprite_width, sprite_height)

# Define a function to handle key presses
def handle_key(key, kbd):
    # Map each key to a sprite index
    key_to_sprite = {
        Keycode.ONE: 0,
        Keycode.TWO: 1,
        Keycode.THREE: 2,
        Keycode.FOUR: 3,
        Keycode.FIVE: 4,
        Keycode.SIX: 5,
        Keycode.SEVEN: 6,
        Keycode.EIGHT: 7,
    }
    # Check if the pressed key is mapped to a sprite index
    if key in key_to_sprite:
        # Update the animation with the corresponding sprite index
        update_animation(key_to_sprite[key])

while True:
    # Check for key presses
    keys = kbd.pressed_keys
    for key in keys:
        # Handle the current pressed key
        if key == Keycode.M:  # Replace with the desired key for the macro
            my_macro(key)
            run_bongo_animation(kbd)
    # Wait for a short delay before checking for key presses again
    time.sleep(0.1)  # Replace with the desired delay in seconds
