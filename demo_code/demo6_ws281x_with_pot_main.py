from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel
from random import randint


led = Pin(2, Pin.OUT)
pot = ADC(Pin(4))

np = NeoPixel(led, 60)

while True:
    r = randint(0, 255)
    g = randint(0, 255) 
    b = randint(0, 255)
    raw_data = (3.3 / 4096) * pot.read() 

    print(r, g, b, raw_data)

    for i in range(60):
        np[i] = (int(255 - r*raw_data), int(255 - g*raw_data), int(255 - b*raw_data))
        np.write()
        sleep(0.01)

