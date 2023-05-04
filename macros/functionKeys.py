from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'FunctionKeys', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x870000, 'F7', [Keycode.F7]),
        (0x873b00, 'F8', [Keycode.F8]),
        (0x876300, 'F9', [Keycode.F9]),
        # 2nd row ----------
        (0x873b00, 'F4', [Keycode.F4]),
        (0x876300, 'F5', [Keycode.F5]),
        (0x00870b, 'F6', [Keycode.F6]),
        # 3rd row ----------
        (0x876300, 'F1', [Keycode.F1]),
        (0x00870b, 'F2', [Keycode.F2]),
        (0x006a87, 'F3', [Keycode.F1]),
        # 4th row ----------
        (0x00870b, 'F10', [Keycode.F10]),
        (0x006a87, 'F11', [Keycode.F11]),
        (0x580087, 'F12', [Keycode.F12]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
