# Raspberry Pico USB Numpad

Projeto de teclado numérico USB customizado utilizando Raspberry Pi Pico (RP2040) e CircuitPython.

## Funcionalidades

- Num Lock
- /
- *
- -
- 0-9
- +
- Enter
- .
- F1
- F2
- F3
- F4

## Hardware

- Raspberry Pi Pico
- CircuitPython
- Biblioteca adafruit_hid

## Estrutura de GPIO

GP8 + GP2 = Num Lock
GP8 + GP3 = /
GP8 + GP4 = *
GP8 + GP5 = -

GP9 + GP2 = 7
GP9 + GP3 = 8
GP9 + GP4 = 9

GP10 + GP2 = 4
GP10 + GP3 = 5
GP10 + GP4 = 6

GP11 + GP2 = 1
GP11 + GP3 = 2
GP11 + GP4 = 3

GP12 + GP6 = 0

GP9 + GP5 = +
GP10 + GP5 = Enter
GP11 + GP5 = .

GP7 + GP2 = F1
GP7 + GP3 = F2
GP7 + GP4 = F3
GP7 + GP5 = F4

## Como instalar

1. Instale CircuitPython no Raspberry Pi Pico
2. Copie a biblioteca adafruit_hid
3. Copie code.py para CIRCUITPY
4. Conecte o Pico ao computador

## Resultado

Teclado numérico USB HID funcional utilizando Raspberry Pi Pico.
