# Metro-Express-Circuit
## Table of contents
* [CircuitPython Blink LED](#CircuitPython-Blink-LED)




# CurcuitPythoon Blink LED
Description: My job was to make a code that told the circuit what colors to change to and a time gap in between those colors. It took lots of trial and erro and was easier on the second try. I was able to go slower and think about what i could be doing wroong, in the end this lead to my success>
# Photo (Code)
![](https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/Mu%20Code%20-%20Aniyah.PNG)

# Servo 180
Descriptionz; i was able to code my circuit python so it told the servo to rotate 180 degrees


# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## LED_CircuitPython
Description: My job was to make a code that told the circuit what colors to change to and a time gap in between those colors. It took lots of trial and erro and was easier on the second try. I was able to go slower and think about what i could be doing wroong, in the end this lead to my success>
# Photo (Code)
![](https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/Mu%20Code%20-%20Aniyah.PNG)

### Description & Code
i was able to code my circuit python so it told the servo to rotate 180 degrees

Here's how you make code look like code:

```import board
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

### Evidence
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code
i was able to code my circuit python so it told the servo to rotate 180 degrees
```python
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

### Evidence

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection


























