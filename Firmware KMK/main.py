print("Starting KMK boot for Macropad...")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rotary_encoder import RotaryEncoderHandler
from kmk.extensions.display import Display, TextEntry, Display_I2C

keyboard = KMKKeyboard()

# 1. Define Matrix Pins (Columns and Rows)
keyboard.col_pins = (
    board.GP26,  # Col 1 (Pin 1)[cite: 5]
    board.GP27,  # Col 2 (Pin 2)[cite: 5]
    board.GP28,  # Col 3 (Pin 3)[cite: 5]
)
keyboard.row_pins = (
    board.GP4,   # Row 1 (Pin 10)[cite: 5]
    board.GP2,   # Row 2 (Pin 9)[cite: 5]
    board.GP1,   # Row 3 (Pin 8)[cite: 5]
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 2. Keymap (3x3 grid mapped to numbers 1-8)
keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.NO,  # Bottom-right is empty
    ]
]

# 3. Rotary Encoder Setup (Pins A, B, and Push Switch)
encoder_handler = RotaryEncoderHandler(
    pin_a=board.GP29,     # Pin 4[cite: 5]
    pin_b=board.GP0,      # Pin 7[cite: 5]
    button_pin=board.GP3, # Pin 11 (SW1)[cite: 5]
)
encoder_handler.map = (
    # (Counter-clockwise, Clockwise, Button Press)
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
)
keyboard.extensions.append(encoder_handler)

# 4. I2C OLED Display Setup (128x64 SSD1306)
i2c_bus = board.I2C()  # Uses GP6 (SDA) and GP7 (SCL)[cite: 5]
display = Display(
    display=Display_I2C(i2c_bus=i2c_bus, width=128, height=64),
    entries=[
        TextEntry(text="RP2040 Macropad", x=0, y=0),
        TextEntry(text="Layer: 0", x=0, y=20),
    ],
    width=128,
    height=64,
)
keyboard.extensions.append(display)

if __name__ == "__main__":
    keyboard.go()
