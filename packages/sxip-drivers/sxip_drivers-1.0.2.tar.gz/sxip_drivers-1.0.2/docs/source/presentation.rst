===========
phox-modbus
===========

Overview
========

This module is a Python driver for PHOXENE's SxIP flash devices

It is intended to be use by software developpers in order to speed-up the integration
of PHOXENE's flash devices by our customers.

It is realeased under a free software licence,
see the LICENSE file for more details

MIT License Copyright (c) 2023 PHOXENE


Features
========
* Allow to instanciate a SxIP communication objects
* Implements general functions
    * Read multiple registers
    * Write a single register
    * Write multiple registers
    * Write a single coil
* Implements SxIP dedicated functions:

* Optional "fast reception mode" that skip receive timeout
  by using frame lenght prediction
* Hack tools allows to test modbus server response to corrupted frames
* Optional feeeback of sent and received frames as well as Modbus events.
  Main usage is debbug.
* The files in this package are 100% pure Python.

Requirements
============
* Pyhton 3.7 or newer
* Windows 7 or newer
* Debian 10 or newer

Installation
============
phox-modbus can be installed from PyPI:

.. code-block:: console

    pip install phox-modbus

Developers also may be interested to get the source archive, because it contains examples, tests and the this documentation.
