import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

while True:
    print("Make it Light Blue")
    dot.fill((204, 255, 255))
    time.sleep(.3)
    print("make it purple")
    dot.fill((153, 102, 255))
    time.sleep(.3)
    print("Make it Pink")
    dot.fill((255, 0, 255))
    time.sleep(.3)
    print("Make it Orange")
    dot.fill((255, 102, 0))
    time.sleep(.3)
    print("Make it Brown")
    dot.fill((153, 51, 0))
    time.sleep(.3)