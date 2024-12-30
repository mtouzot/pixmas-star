# SPDX-FileCopyrightText: 2024-present Martin TOUZOT <martin.touzot@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
from pixmas_star.star import Star
from time import sleep

star = Star()

try:
    star.inner.on()
    while True:
        star.toggle()
        sleep(0.5)
except KeyboardInterrupt:
    star.close()
