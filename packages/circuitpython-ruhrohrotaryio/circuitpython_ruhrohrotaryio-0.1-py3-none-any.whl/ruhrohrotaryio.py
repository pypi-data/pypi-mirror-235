# SPDX-FileCopyrightText: Copyright (c) 2023 Tod Kurt
#
# SPDX-License-Identifier: MIT
"""
`ruhrohrotaryio`
================================================================================

Pretend to be 'rotaryio' for boards that need non-sequential pins


* Author(s): Tod Kurt / @todbot

Implementation Notes
--------------------

**Hardware:**

Any CircuitPython device with `keypad` support

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

# imports

import keypad
import digitalio

__version__ = "0.1"
__repo__ = "https://github.com/todbot/CircuitPython_RuhRohRotaryIO.git"


class IncrementalEncoder:
    """
    A simple drop-in replacement for rotaryio.IncrementalEncoder that works
    on non-sequential pins on RP2040
    """

    def __init__(self, pin_a, pin_b, divisor=4):  # divisor is unused currently
        pin = digitalio.DigitalInOut(pin_a)
        pin.switch_to_input(pull=digitalio.Pull.UP)
        self._key1_val = pin.value  # get initial pin state
        pin.deinit()  # just needed it to check pin state
        self._divisor = divisor
        self._encoder_keys = keypad.Keys(
            (pin_a, pin_b), value_when_pressed=False, pull=True
        )
        self._position = 0
        self._update()  # do an initial read
        self._position = 0  # and then zero it out

    def _update(self):
        while key := self._encoder_keys.events.get():
            if key.key_number == 0:
                if key.pressed:
                    if self._key1_val:
                        self._position -= 1
                    else:
                        self._position += 1
                else:
                    if self._key1_val:
                        self._position += 1
                    else:
                        self._position -= 1

            if key.key_number == 1:
                self._key1_val = key.pressed

    @property
    def position(self):
        """The current position in terms of pulses.
        The number of pulses per rotation is defined by the specific hardware and by the divisor.
        """
        self._update()
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
