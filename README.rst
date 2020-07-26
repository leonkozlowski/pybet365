========
pybet365
========


.. image:: https://img.shields.io/pypi/v/pybet365.svg
        :target: https://pypi.python.org/pypi/pybet365

.. image:: https://img.shields.io/travis/leonkozlowski/pybet365.svg
        :target: https://travis-ci.com/leonkozlowski/pybet365

.. image:: https://readthedocs.org/projects/pybet365/badge/?version=latest
        :target: https://pybet365.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python Wrapper for Bet365 API


* Free software: MIT license
* Documentation: https://pybet365.readthedocs.io.

Installation
------------

From source

.. code-block:: bash

    $ git clone https://github.com/leonkozlowski/pybet365.git
    $ cd pybet365

    $ python3.8 -m venv venv
    $ source venv/bin/activate
    $ pip install -e .

    # For test dependencies
    $ pip install -r requirements_dev.txt

From build

.. code-block:: bash

    $ pip install pybet365


Features
--------

GET Request to Upcoming Events Endpoint

.. code-block:: python

    from pybet365 import Bet365

    client = Bet365(api_host="someHost", api_key="someKey")
    upcoming_events = client.upcoming_events(sport_id="49")

    print(upcoming_events)

Response

.. code-block:: JSON

    {
      "success": 1,
      "pager": {
        "page": 1,
        "per_page": 50,
        "total": 102
      },
      "results": [
        {
          "id": "88107197",
          "sport_id": "92",
          "time": "1586480400",
          "time_status": "0",
          "league": {
            "id": "10036652",
            "name": "Moscow Liga Pro"
          },
          "home": {
            "id": "10423098",
            "name": "Evgenii Kryuchkov"
          },
          "away": {
            "id": "10433218",
            "name": "Aik Lulikyan"
          },
          "ss": null,
          "our_event_id": "2297143",
          "updated_at": "1586478473"
        }
      ]
    }

Access response objects with dot notation

.. code-block:: python

    from pybet365 import Bet365

    client = Bet365(api_host="someHost", api_key="someKey")
    upcoming_events = client.upcoming_events(sport_id="49")

    print(upcoming_events.success)
    >>> 1


Access of array type `results` objects

.. code-block:: python

    from pybet365 import Bet365

    client = Bet365(api_host="someHost", api_key="someKey")
    upcoming_events = client.upcoming_events(sport_id="49")

    print(upcoming_events.results[0].id)
    >>> "88107197"

Environment Variables
---------------------

* BET365_HOST
    * `$ export BET365_HOST=yourHost`


* BET365_KEY
    * `$ export BET365_KEY=yourSecretKey`


Testing
_______

.. code-block:: bash

    # Test with pytest
    make tests

    # Lint with flake8
    make lint


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
