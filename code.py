import board
import digitalio
import usb_hid
import time

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

teclas = {

    (8,2): Keycode.KEYPAD_NUMLOCK,
    (8,3): Keycode.KEYPAD_FORWARD_SLASH,
    (8,4): Keycode.KEYPAD_ASTERISK,
    (8,5): Keycode.KEYPAD_MINUS,

    (9,2): Keycode.KEYPAD_SEVEN,
    (9,3): Keycode.KEYPAD_EIGHT,
    (9,4): Keycode.KEYPAD_NINE,

    (10,2): Keycode.KEYPAD_FOUR,
    (10,3): Keycode.KEYPAD_FIVE,
    (10,4): Keycode.KEYPAD_SIX,

    (11,2): Keycode.KEYPAD_ONE,
    (11,3): Keycode.KEYPAD_TWO,
    (11,4): Keycode.KEYPAD_THREE,

    (12,6): Keycode.KEYPAD_ZERO,

    (9,5): Keycode.KEYPAD_PLUS,
    (10,5): Keycode.KEYPAD_ENTER,
    (11,5): Keycode.KEYPAD_PERIOD,

    (7,2): Keycode.F1,
    (7,4): Keycode.F3,
    (7,5): Keycode.F4,

}

gpio = []

for i in range(2,13):

    gp = getattr(board,f"GP{i}")

    p = digitalio.DigitalInOut(gp)

    p.direction = digitalio.Direction.OUTPUT
    p.value = True

    gpio.append(p)

while True:

    for saida in range(11):

        for i in range(11):

            gpio[i].direction = digitalio.Direction.INPUT
            gpio[i].pull = digitalio.Pull.UP

        gpio[saida].direction = digitalio.Direction.OUTPUT
        gpio[saida].value = False

        for entrada in range(11):

            if entrada == saida:
                continue

            if not gpio[entrada].value:

                gp_saida = saida + 2
                gp_entrada = entrada + 2

                tecla = teclas.get((gp_saida,gp_entrada))

                if tecla:

                    kbd.press(tecla)

                    time.sleep(0.05)

                    kbd.release_all()

                while not gpio[entrada].value:

                    time.sleep(0.01)

    time.sleep(0.01)