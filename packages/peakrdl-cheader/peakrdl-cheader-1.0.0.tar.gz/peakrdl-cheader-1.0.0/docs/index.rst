Introduction
============

PeakRDL C-Header is a python package which can be used to generate a register
abstraction layer C Header from a SystemRDL definition.

Features:

* Generates C ``struct`` definitions that overlay your hardware address space
* Supports complex nested structures, arrays, etc.
* Field bit offset, width, mask, etc ``#define`` macros.
* Can optionally generate register bit-field structs.
* Optionally generates a test-case to validate correctness of the generated header.
* Supports the full range of GNU C Standards.


Installing
----------

Install from `PyPi`_ using pip

.. code-block:: bash

    python3 -m pip install peakrdl-cheader

.. _PyPi: https://pypi.org/project/peakrdl-cheader


Quick Start
-----------
The easiest way is to use the `PeakRDL command line tool <https://peakrdl.readthedocs.io/>`_:

.. code-block:: bash

    python3 -m pip install peakrdl
    peakrdl c-header example.rdl -o example.h

Using the generated header, you can access your device registers by name!

.. code-block:: c

    #include "example.h"

    int main void {
        volatile example_t *dev = 0x42000; // hardware address of example device

        dev->my_reg = 1234;
        for(int i=0; i<8; i++){
            dev->block[i].ctrl = 456;
        }

        return 0;
    }


.. toctree::
    :hidden:

    self
    output
    configuring
    api
    licensing
