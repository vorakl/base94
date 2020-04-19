Base94
######

A reversible translation of binary data to text with an alphabet between 2 and 94 symbols.

Description
===========

This is a binary/text converter with any base between 2 and 94. It is probably a theoretical prototype and has a purely academic flavor, since the time and space complexities make it applicable only to small files (up to a few tens of kilobytes), although it allows one to choose any base with no dependencies on powers of two, e.g. 7 or 77. Visit https://vorakl.com/articles/base94/  for more details.

How to run
==========

.. code-block:: bash

    ./base94.py <-e|-d> src dst [base=42]

For example:

.. code-block:: bash

    ./base94.py -e /bin/gethostip /tmp/gethostip.b94 94
    ./base94.py -e /bin/gethostip /tmp/gethostip.b42
    ./base94.py -d /tmp/gethostip.b42 /tmp/gethostip

There is also ``test.sh`` script that uses a small binary file ``/bin/gethostip``
for encoding/decoding and gathering different metrics. Simply run it with no arguments.

