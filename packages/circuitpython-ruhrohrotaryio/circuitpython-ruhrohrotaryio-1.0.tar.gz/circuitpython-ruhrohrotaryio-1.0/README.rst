Introduction
============


.. image:: https://readthedocs.org/projects/circuitpython-ruhrohrotaryio/badge/?version=latest
    :target: https://circuitpython-ruhrohrotaryio.readthedocs.io/
    :alt: Documentation Status



.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/todbot/CircuitPython_RuhRohRotaryIO/workflows/Build%20CI/badge.svg
    :target: https://github.com/todbot/CircuitPython_RuhRohRotaryIO/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Pretend to be ``rotaryio`` for boards that need non-sequential pins.

On RP2040-based boards like the Raspberry Pi Pico and QTPy RP2040,
if you try to use "`rotaryio <https://docs.circuitpython.org/en/latest/shared-bindings/rotaryio/index.html>`_"
on pins whose GPIO numbers are not sequential, you will get a
``RuntimeError: Pins must be sequential GPIO pins``.


This package acts just like ``rotaryio`` but uses ``keypad`` and some logic to read a rotary encoder.
It is not as fast or efficient as ``rotaryio`` but it will work on RP2040 boards.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install ruhrohrotaryio

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-ruhrohrotaryio/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-ruhrohrotaryio

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-ruhrohrotaryio

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-ruhrohrotaryio

Usage Example
=============

.. code-block:: python

    import os
    import time
    import board

    # works on both QTPY M0 and QTPY RP2040

    if os.uname().machine.find("rp2040") > 0:  # RP2040
        from ruhrohrotaryio import IncrementalEncoder
    else:
        from rotaryio import IncrementalEncoder

    encoder = IncrementalEncoder( board.A3, board.A1 )

    while True:
        print(encoder.position)
        time.sleep(0.1)


Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-ruhrohrotaryio.readthedocs.io/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/todbot/CircuitPython_RuhRohRotaryIO/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
