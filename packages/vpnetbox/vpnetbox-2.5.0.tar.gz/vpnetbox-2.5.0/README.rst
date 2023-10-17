
vpnetbox
=========

Python package to work with Netbox using REST API.
Facilitates low-level calls to Netbox and data parsing.
- NbApi: Requests data from the Netbox REST API using filter parameters identical to those in the web interface filter form.
- NbHandler: Retrieves and caches a bulk of data from the Netbox to local system.
- NbData: Sets of Netbox objects, like aggregates, prefixes, etc., are joined together.
- NbParser: Extracts a value from a Netbox object using a long chain of keys.
`./docs/NbHandler_diagram.rst`_

.. contents::


Introduction
------------
What is Vpnetbox? Why is it needed? Why not Pynetbox?
Pynetbox is a great tool for working with Netbox and I use it frequently.
However, I am facing some coding challenges when my scrip speed is crucial.
Vpnetbox was created to address specific issues.
issues that I regularly encountered while working with Pynetbox.
This tool covers only a subset of Netbox objects that I frequently use in my work,
such as aggregates, prefixes, addresses, devices, etc.
It does not encompass all objects, because I lack the energy to cover all of them.
So, what is the utility of this tool?
In short, to make my code faster, cache a lot of Netbox objects on the local disk
and play with them locally.

Speed
=====
Using the REST API, I can retrieve a bulk of data faster than when using Pynetbox. Typically,
I download a large amount of data to my local system, save it to cache and then start processing
the data. On the other hand, Pynetbox maintains a connection with Netbox and downloads additional
data during processing, which makes the code become veeeeryyyy slow.

Tests
=====
Code based on the REST API is much easier to cover with unittests, because the REST API returns
a simple dictionary, which is easy to mock, save to a pickle file, and so on. Testing code based
on Pynetbox presents a challenge.

Filter parameters
=================
I like the Netbox Web UI. I am familiar with it and would like to use the same search parameters
in the API. Try to retrieve a lot of specific prefixes using Pynetbox and you will understand my
frustration. Yes, it is possible, but script will look strange and veeeeryyyy slow.


Requirements
------------

Python >=3.8


Installation
------------

Install the package from pypi.org release

.. code:: bash

    pip install vpnetbox

or install the package from github.com release

.. code:: bash

    pip install https://github.com/vladimirs-git/vpnetbox/archive/refs/tags/2.5.0.tar.gz

or install the package from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/vpnetbox


Usage
-----
For more details look for use cases in examples.
`./examples`_

.. code:: python

    import logging
    from datetime import datetime
    from vpnetbox import NbApi

    # Enable DEBUG mode to demonstrate the speed of requests to the Netbox API
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())

    HOST = "demo.netbox.dev"
    TOKEN = "*****"

    # Get multiple addresses by exact address values.
    # https://demo.netbox.dev/ipam/ip-addresses/?address=10.0.0.1/24&address=10.0.0.2/24
    nb = NbApi(host=HOST, token=TOKEN)
    objects = nb.addresses.get(address=["10.0.0.1/24", "10.0.0.2/24"])
    print([d["address"] for d in objects])
    # ['10.0.0.1/24', '10.0.0.2/24']

    # Find multiple addresses by strings.
    # https://demo.netbox.dev/ipam/ip-addresses/?q=10.0.0.1
    # https://demo.netbox.dev/ipam/ip-addresses/?q=10.0.0.2
    objects = nb.addresses.get(q=["10.0.0.1", "10.0.0.2"])
    print([d["address"] for d in objects])
    # ['10.0.0.1/24', '10.0.0.2/24', '10.0.0.100/24', '10.0.0.254/24']


    # Get a lot of data in fast threading mode.
    start = datetime.now()
    nb = NbApi(host=HOST, token=TOKEN, threads=5, interval=0.1)
    objects = nb.addresses.get()
    seconds = (datetime.now() - start).seconds
    print([d["address"] for d in objects])
    print(f"{len(objects)=} {seconds=}")
    # DEBUG    https://demo.netbox.dev:443 "GET /api/ipam/addresses/?brief=1&limit=1 ...
    # DEBUG    Starting new HTTPS connection (2): demo.netbox.dev:443
    # DEBUG    Starting new HTTPS connection (3): demo.netbox.dev:443
    # DEBUG    Starting new HTTPS connection (4): demo.netbox.dev:443
    # DEBUG    Starting new HTTPS connection (5): demo.netbox.dev:443
    # DEBUG    https://demo.netbox.dev:443 "GET /api/ipam/addresses/? ...
    # DEBUG    https://demo.netbox.dev:443 "GET /api/ipam/addresses/? ...
    # DEBUG    https://demo.netbox.dev:443 "GET /api/ipam/addresses/? ...
    # DEBUG    https://demo.netbox.dev:443 "GET /api/ipam/addresses/? ...
    # DEBUG    https://demo.netbox.dev:443 "GET /api/ipam/addresses/? ...
    # len(objects)=4153 seconds=3


    # Get a lot of data in slow loop mode, to compare time performance.
    start = datetime.now()
    nb = NbApi(host=HOST, token=TOKEN)
    objects = nb.addresses.get()
    seconds = (datetime.now() - start).seconds
    print(f"{len(objects)=} {seconds=}")


NbApi
---------
Requests data from the Netbox REST API using parameters identical to those in the web interface filter form.
`./docs/NbApi.rst`_


NbParser
------------
`./docs/NbParser.rst`_
Extracts a value from a Netbox object using a long chain of keys.


NbHandler
---------
`./docs/NbHandler.rst`_
Retrieves and caches a bulk of data from the Netbox to local system.
Collects sets of aggregates, prefixes, addresses, devices, sites data from Netbox by scenarios.


.. _`./docs/NbApi.rst`: ./docs/NbApi.rst
.. _`./docs/NbHandler.rst`: ./docs/NbHandler.rst
.. _`./docs/NbHandler_diagram.rst`: ./docs/NbHandler_diagram.rst
.. _`./docs/NbParser.rst`: ./docs/NbParser.rst
.. _`./examples`: ./examples