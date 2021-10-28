# Metro-Express-Circuit
## Table of contents
* [CircuitPython Blink LED](#CircuitPython-Blink-LED)
* [Servo 180](#Servo-180)
* [Distance Sensor](#Distance-Sensor)
* [Photo interrupter](#Photo-interrupter)



#  Blink LED & code

# Reflection
My job was to make a code that told the circuit what colors to change to and a time gap in between those colors. It took lots of trial and erro and was easier on the second try. I was able to go slower and think about what i could be doing wroong, in the end this lead to my success.

```
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
   
   ```   
    
 # Evidence
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/LED%20gif.gif" width="250" />

        
# Servo 180 & code

```
import time
import board
import pwmio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
        
   ```


# Reflection
I coded my servo to turn 180 degrees. I was faced with the challkenge of figuring out ewhich degrees worked bgest and how to it not spin continusly. In the long run i was able to find the coirrect code and get my servo to spin 180 degress in intervoles
# Evidence
# Servo Gif
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/servo%20gif.gif" width="250" />

---
# Distance Sensor & code

```
import time
import board
import adafruit_hcsr04
import simpleio
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
cm = 0

while True:
    try:
        cm = sonar.distance
        print((cm,))
        if cm < 20:
            print("red")
            r = simpleio.map_range(cm, 5, 20, 255, 0)
            g = 0
            b = 0
        if cm > 20 and cm < 35:
            print("blue")
            r = 0
            g = 0
            b = simpleio.map_range(cm, 0, 20, 255, 0)

        if cm > 35:
            print("green")
            r = 0
            g = simpleio.map_range(cm, 20, 30, 0, 255)
            b = 0
        dot.fill((int(r), int(g), int(b)))

    except RuntimeError:
            print("Retrying")
            time.sleep(0.1)
            
```

# Reflection
Wiring up the distance sensor was diffucult at first but with reserche i was able to get it
Working with number is not easy and i learned the hard way that you have to be very paerticular with your code
Though at the end i was not able to get the blue LED to flash i still think i did a good job
# Evidence
# Distance Sensor Gif
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/Distance%20Sensor%20Gif.gif" width="250" />

---
# Photo interrupter 

```
from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 4
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("The number of inturrupts is:", str(counter))
        max = time.time() + 4
        counter = 0
        
  ```
        
# Reflection
I needed to count the interruptions and reflect that onto the serial monitor
I succeeded and the seiral counted the number or interruptions
This thought me to keeping trying even fater tyhings get hard
# Evidence
# Photo Interrupter Gif
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/photo%20interupter%20Gif.gif" width="250" />

---
# Lcd Interuppteer & code

```
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import touchio

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

lcd.print("Hello, Engineer!")

touch_pad = board.A0  # Will not work for Circuit Playground Express!
# touch_pad = board.A1  # For Circuit Playground Express

touch = touchio.TouchIn(touch_pad)

touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A2 = touchio.TouchIn(board.A2)  # Not a touch pin on Trinket M0!

while True:
    if touch_A1.value:
        lcd.print("Touched A1!")
    if touch_A2.value:
        lcd.print("Touched A2!")
    time.sleep(0.05)
    
  ```
    
# Reflection    
I was able to work through problmes my
When i did run into a problem i tried to fix it myself
I loved figuring out the kinks myslefg and having to think
i relly liked working with this one because i was able to think about how i can fix my problem on my own

