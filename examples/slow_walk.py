# SPDX-FileCopyrightText: 2024-present Martin TOUZOT <martin.touzot@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
from pixmas_star.star import Star
from time import sleep

step = 0.5
count = 0
star = Star(pwm=True)
leds = star.leds

try:
    while True:
        if(count%26!=0):
            leds[count%26].on()
            sleep(step)
            leds[count%26].off()

        count += 1
        step = step*0.99

        if(step <= 0.0001):
            star.inner.blink(on_time=0.5,off_time=0.5,n=5)
            sleep(5)
            count = 0
            step = 2

except KeyboardInterrupt:
    star.close()
