python-can-canine
=================

This module is a plugin for the python-can_. module, that allows the use of canable-compatible Canine CAN interfaces.


Installation
------------

Install using pip::

    $ pip install python-can-canine


Usage
-----

In general, useage is largely the same as with the main python-can_ library, using the interface designation of "canine". When integrating the Canine interface into scripts, it is possible to import constants, device deisgnations etc from the python-can-canine module using "import can_canine". For the majority of the use cases, using a Canine interface is as simple as amending any python-can examples with the lines shown below:

Create python-can bus with the Canine USB interface:

.. code-block:: python

    import can
    from canine import Canine

    bus = can.Bus(interface="canine", bitrate=1000000)
