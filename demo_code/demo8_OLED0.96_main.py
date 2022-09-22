from machine import Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C
import framebuf

WIDTH = 128
HEIGHT = 64

# buffer = bytearray(b'\x00\x00\x00\x00\x01\xf0\x0f\x00\x06\x860\xb0\x04\x01@\x10\x04\x01\x000\x02\x10\x89 \x02\x05\xd2 \x01\x03\xe0@\x01\x87\xe0\x80\x10~?\x00\x00\x88\x11\x80\x01\x18\x08@\x02><@\x02a\xc3@C\xc1\x81\xe0\x05\x80\x90\x91\x08\x80\x80\x98\x08\x81\xc0\x88\t\x83\xe1\x98)\xe4\x1f\x98\x07\xf8\x0e0\x068\x0c \x02\x18\x080\x02\x88\x08 \x03\x0e0A\x01\x8f\xf8\x80\x00|\x1f\x00\x008\x0c\x00\x00\x0c0\x02\x00\x03\xe0\x00\x00\x00\x80\x00\x01\x00\x00\x04')

# fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

# initializing i2c, using hard I2C 0.
# ------------------------
# |    | I2C(0) | I2C(1) |
# ------------------------
# |scl | 18     | 25     |
# ------------------------
# |sda | 19     | 26     | 
# ------------------------
i2c = I2C(0, sda=Pin(19), scl=Pin(18), freq=400000)


devices = i2c.scan()
if len(devices) == 0:
    print("No i2c device detected, please check the wiring cable !")
else:
    print('i2c devices found: {}'.format(len(devices)))

for device in devices:
    print("At address: {}".format(hex(device)))


# create oled object 
oled = SSD1306_I2C(WIDTH, HEIGHT,i2c)


while True:
    oled.fill(0)
    # oled.blit(fb, x, y)
    oled.text("hello ESP32", 0, 0) # text, x cord, y cord
    oled.text("hello wrover", 0, 10) 
    oled.text("hello 52Pi", 0, 20) 
    oled.show()

    sleep(5)
