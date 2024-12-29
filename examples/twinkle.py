# SPDX-FileCopyrightText: 2024-present Martin TOUZOT <martin.touzot@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
from pixmas_star.star import Star
from time import sleep

star = Star(pwm=True)

try:
    leds = star.leds
    while True:
        for led in leds:
            led.pulse()
            sleep(.2)
except KeyboardInterrupt:
    star.close()
