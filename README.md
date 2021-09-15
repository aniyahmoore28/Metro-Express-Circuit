# Metro-Express-Circuit
## Table of contents
* [CircuitPython Blink LED](#CircuitPython-Blink-LED)




# CurcuitPython Blink LED
Description: My job was to make a code that told the circuit what colors to change to and a time gap in between those colors. It took lots of trial and erro and was easier on the second try. I was able to go slower and think about what i could be doing wroong, in the end this lead to my success>
# Photo (Code)
![](https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/Mu%20Code%20-%20Aniyah.PNG)

# LED Gif
![](https://github.com/aniyahmoore28/Metro-Express-Circuit/blob/main/Metro%20Express/LED%20gif.gif)

# Servo 180
Description: I coded my servo to turn 180 degrees

# Servo Code
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






