#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import time
from threading import Thread
from ev3dev2.sensor.lego import TouchSensor, GyroSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_3, INPUT_1, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.motor import SpeedPercent, MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.led import Leds

# state constants
ON = True
OFF = False


def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


ts = TouchSensor(INPUT_3)
sound = Sound()
us = UltrasonicSensor(INPUT_4)
gs = GyroSensor(INPUT_1)
ms = MoveSteering(OUTPUT_A, OUTPUT_D)
leds = Leds()

class light_Thread(Thread):
    # 灯光测试
    def _init_(self):
        Thread.__init__(self)
        self.flag = False  # 运行标识

    def run(self):
        while True:
            if self.flag:
                # leds.animate_police_lights('RED', 'RED', duration=1)
                leds.set_color('LEFT', (0.5, 0.3))
                leds.set_color('RIGHT', (0.5, 0.3))
            else:
                leds.all_off()
                time.sleep(0.5)

    def set_flag(self, parm):
        self.flag = parm

    def get_flag(self, parm):
        return self.flag


def twenty_tones(frequency):
    # 警报声
    while True:
        sound.play_tone(frequency, 0.2)
        time.sleep(0.5)

def led_light():
    while True:
        leds.animate_police_lights('RED', 'GREEN')


def go_back():
    # 倒车入库
    ms.on_for_seconds(0, speed=SpeedPercent(-30), seconds=2)
    ms.on(100, SpeedPercent(50))
    gs.wait_until_angle_changed_by(90)
    ms.on_for_seconds(0, speed=SpeedPercent(-30), seconds=3)


if __name__ == '__main__':
    # main()
    t = Thread(target=twenty_tones, args=(1500,))
    t.setDaemon(True)
    # t2 = Thread(target=led_light)
    # t2.setDaemon(True)
    t2 = light_Thread()
    t2._init_()
    t2.setDaemon(True)
    while us.distance_centimeters_continuous > 10:
        ms.on(steering=0, speed=SpeedPercent(80))

    t.start()
    t2.start()
    t2.set_flag(True)
    go_back()

    t2.set_flag(False)
    ms.on_for_seconds(0, speed=SpeedPercent(30), seconds=3)
    # sound.speak('bye')
