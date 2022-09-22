from machine import Pin
from time import sleep
from neopixel import NeoPixel
from random import randint


DIN = Pin(2, Pin.OUT)

NUMBER_OF_LED = 60

np = NeoPixel(DIN, NUMBER_OF_LED)

while True:
    r = randint(0, 255)
    g = randint(0, 255) 
    b = randint(0, 255)

    for i in range(60):
        np[i] = (r,g,b)
        np.write()
        sleep(0.01)

