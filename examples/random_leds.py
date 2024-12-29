# SPDX-FileCopyrightText: 2024-present Martin TOUZOT <martin.touzot@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
from pixmas_star.star import Star
from gpiozero.tools import random_values
from signal import pause

star = Star(pwm=True)
leds = star.leds

try:
    for led in leds:
        led.source_delay = 0.1
        led.source = random_values()
    pause()
except KeyboardInterrupt:
    star.off()
    star.close()
