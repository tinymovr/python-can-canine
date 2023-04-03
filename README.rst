python-can-canine
=================



This module is a plugin that lets you use `CANine adapters <https://tinymovr.com/products/can-bus-adapter>`_ with the `CANine firmware <https://github.com/tinymovr/CANine>`_ in python-can.


Installation
------------

Install using pip::

    $ pip install python-can-canine


Usage
-----

Overall, using this plugin is quite similar to the main Python-CAN library, with the interface named "canine". To integrate the Canine interface into your scripts, you can import constants, device designations, and more from the Python-CAN-Canine module using "import canine". For most scenarios, incorporating a Canine interface is as easy as modifying Python-CAN examples with the lines provided below:

Create python-can bus with the Canine USB interface:

.. code-block:: python

    import can
    from canine import CANineBus

    bus = can.Bus(interface="canine", bitrate=1000000)
