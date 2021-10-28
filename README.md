# Metro-Express-Circuit
## Table of contents
* [CircuitPython Blink LED](#CircuitPython-Blink-LED)
* [Servo 180](#Servo-180)
* [Distance Sensor](#Distance-Sensor)
* [Photo interrupter](#Photo-interrupter)



#  Blink LED & code
# Reflection
My job was to make a code that told the circuit what colors to change to and a time gap in between those colors. It took lots of trial and erro and was easier on the second try. I was able to go slower and think about what i could be doing wroong, in the end this lead to my success>

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

# Reflection
I coded my servo to turn 180 degrees. I was faced with the challkenge of figuring out ewhich degrees worked bgest and how to it not spin continusly. In the long run i was able to find the coirrect code and get my servo to spin 180 degress in intervoles
# Evidence
# Servo Gif
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/servo%20gif.gif" width="250" />

---
# Distance Sensor
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/Distasnce%20sensor%20code%20photo.PNG" width="250" />

# Reflection
Wiring up the distance sensor was diffucult at first but with reserche i was able to get it
Working with number is not easy and i learned the hard way that you have to be very paerticular with your code
Though at the end i was not able to get the blue LED to flash i still think i did a good job
# Evidence
# Distance Sensor Gif
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/Distance%20Sensor%20Gif.gif" width="250" />

---
# Photo interrupter 
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/photo%20inturrupter%20SH.PNG" width="250" />
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/photo%20inturrupter%20SH2.PNG" width="250" />

# Reflection
I needed to count the interruptions and reflect that onto the serial monitor
I succeeded and the seiral counted the number or interruptions
This thought me to keeping trying even fater tyhings get hard
# Evidence
# Photo Interrupter Gif
<img src="https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/photo%20interupter%20Gif.gif" width="250" />

---
# Lcd Interuppteer
I was able to work through problmes my
When i did run into a problem i tried to fix it myself
I loved figuring out the kinks myslefg and having to think
i relly liked working with this one because i was able to think about how i can fix my problem on my own

