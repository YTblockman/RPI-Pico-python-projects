"""
    Translated from C++ to python (sorta)
    https://create.arduino.cc/projecthub/410027/rickroll-piezo-buzzer-a1cd11?ref=part&ref_id=8233&offset=3
"""

from machine import Pin, PWM
from time import sleep
import random as r

a3f  =  208     # 208 Hz
b3f  =  233     # 233 Hz
b3   =  247     # 247 Hz
c4   =  261     # 261 Hz MIDDLE C
c4s  =  277     # 277 Hz
e4f  =  311     # 311 Hz    
f4   =  349     # 349 Hz 
a4f  =  415     # 415 Hz  
b4f  =  466     # 466 Hz 
b4   =  493     # 493 Hz 
c5   =  523     # 523 Hz 
c5s  =  554     # 554 Hz
e5f  =  622     # 622 Hz
f5   =  698     # 698 ?
f5s  =  740     # 740 Hz
a5f  =  831     # 831 Hz 
rest =  10      # rest


song1_intro_melody = (
    c5s, e5f, e5f, f5, a5f, f5s, f5, e5f, c5s, e5f, rest, a4f, a4f,
    rest, c4s, c4s, c4s, c4s, e4f, rest, c4, b3f, a3f,
    rest, b3f, b3f, c4, c4s, a3f, a4f, a4f, e4f,
    rest, b3f, b3f, c4, c4s, b3f, c4s, e4f, rest, c4, b3f, b3f, a3f,
    rest, b3f, b3f, c4, c4s, a3f, a3f, e4f, e4f, e4f, f4, e4f,
    c4s, e4f, f4, c4s, e4f, e4f, e4f, f4, e4f, a3f,
    rest, b3f, c4, c4s, a3f, rest, e4f, f4, e4f,
    b4f, b4f, a4f, a4f,
    f5, f5, e5f, b4f, b4f, a4f, a4f, e5f, e5f, c5s, c5, b4f,
    c5s, c5s, c5s, c5s,
    c5s, e5f, c5, b4f, a4f, a4f, a4f, e5f, c5s,
    b4f, b4f, a4f, a4f,
    f5, f5, e5f, b4f, b4f, a4f, a4f, a5f, c5, c5s, c5, b4f,
    c5s, c5s, c5s, c5s,
    c5s, e5f, c5, b4f, a4f, rest, a4f, e5f, c5s, rest
)

song1_intro_rhythmn = (
    6, 10, 6, 6, 1, 1, 1, 1, 6, 10, 4, 2, 10,
    2, 2, 2, 2, 2, 3, 2, 2, 2, 5,
    2, 2, 2, 2, 3, 2, 3, 2, 5,
    2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3,
    2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 4,
    5, 2, 2, 2, 2, 2, 2, 1, 2, 2,
    2, 1, 1, 1, 3, 1, 1, 1, 3,
    1, 1, 1, 1,
    3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 2,
    0, 0, 0, 0,
    3, 3, 3, 1, 2, 2, 2, 4, 8,
    1, 1, 1, 1,
    3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 2,
    1, 1, 1, 1,
    3, 3, 3, 1, 2, 2, 2, 4, 8, 4
)

pwm = PWM(Pin(0))
pwm.freq(1000)

max_ = 65025

HIGH = 1
LOW = 0

def digitalWrite(port, state):
    print("w " + str(port) + " s " + str(state))
    pass

while True:
    if not len(song1_intro_melody) == len(song1_intro_rhythmn):
        print("there is something up with list values!")
    
    index = 0
    for i in song1_intro_melody:
        print(str(i) + " : " + str(song1_intro_rhythmn[index] / 10))
        pwm.freq(i)
        pwm.duty_u16(int(i/5)) 
        
        sleep(song1_intro_rhythmn[index] / 8)
        index += 1
    
    pass
