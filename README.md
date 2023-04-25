# Adafruit Macro Pad - Custom Macros

As a developer, I picked up the Adafruit Macro Pad as a way to streamline my workflow by creating custom macros for multiple applications. Additionally, I wanted to learn CircuitPython, and the Macro Pad seemed like the perfect tool for that.

## What is the Adafruit Macro Pad?

The Adafruit Macro Pad is a compact 3x4 mechanical keypad that can be programmed to perform a wide range of functions. It features a USB-C port for easy connectivity to your computer and a built-in NeoPixel LED for visual feedback.

## Creating Custom Macros

With the Adafruit Macro Pad, you can create custom macros that are tailored to your specific needs. To create a custom macro, follow these steps:

1. Connect the Macro Pad to your computer using a USB-C cable.
2. Install the CircuitPython programming language on your computer if you haven't already done so.
3. Install the Adafruit Macro Pad library on your computer.
4. Write a program using the CircuitPython programming language that defines the functions you want your Macro Pad to perform.
5. Upload your program to the Macro Pad using the USB-C cable.

You can create custom macros for a variety of applications, such as text editing, video editing, or gaming. Here are some examples of custom macros that you can create:

```python
# Example macro for text editing
import adafruit_macropad

macropad = adafruit_macropad.MacroPad()
text_to_type = "Hello, World!"

def type_text():
    macropad.keyboard_layout.write(text_to_type)

macropad.add_macro(type_text)

while True:
    macropad.update()
    
# Example macro for video editing
import adafruit_macropad

macropad = adafruit_macropad.MacroPad()

def split_clip():
    macropad.keyboard.press(macropad.Keycode.SHIFT, macropad.Keycode.RIGHT_BRACKET)
    macropad.keyboard.release_all()

macropad.add_macro(split_clip)

while True:
    macropad.update()
    
# Example macro for gaming
import adafruit_macropad

macropad = adafruit_macropad.MacroPad()

def reload_weapon():
    macropad.keyboard.press(macropad.Keycode.R)
    macropad.keyboard.release_all()

macropad.add_macro(reload_weapon)
```
while True:
    macropad.update()

## Usong Custom Macros
To use your custom macros, simply press the corresponding key on the Macro Pad. The Macro Pad will execute the function defined in your program, allowing you to perform tasks quickly and efficiently.

## Recources

To learn more about creating custom macros with the Adafruit Macro Pad, check out the following resources:

Adafruit Macro Pad product page: https://www.adafruit.com/product/5128
Adafruit Macro Pad learning guide: https://learn.adafruit.com/adafruit-macro-pad
CircuitPython programming language: https://circuitpython.org/
Adafruit Macro Pad library: https://github.com/adafruit/Adafruit_MacroPad
