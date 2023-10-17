Simple test for QT Py RP2040 vs QT Py M0
----------------------------------------

This example explicitly checks to see if the board is an RP2040-variant.

.. literalinclude:: ../examples/ruhrohrotaryio_simpletest.py
    :caption: examples/ruhrohrotaryio_simpletest.py
    :linenos:

Simple test for any board
-------------------------

This example first tries ``rotaryio`` and if that fail tries ``ruhrohrotaryio``.

.. literalinclude:: ../examples/ruhrohrotaryio_workanywhere.py
    :caption: examples/ruhrohrotaryio_workanywhere.py
    :linenos:
