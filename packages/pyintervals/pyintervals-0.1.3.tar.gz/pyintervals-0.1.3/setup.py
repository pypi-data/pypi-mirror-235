# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyintervals']

package_data = \
{'': ['*']}

modules = \
['py']
extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1,<5']}

setup_kwargs = {
    'name': 'pyintervals',
    'version': '0.1.3',
    'description': 'Efficient interval operations.',
    'long_description': "📐 pyintervals\n===============================\n\n.. image:: https://img.shields.io/pypi/v/pyintervals.svg?style=flat-square&color=blue\n   :target: https://pypi.python.org/pypi/pyintervals\n\n.. image:: https://img.shields.io/pypi/pyversions/pyintervals.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/pyintervals\n\n.. image:: https://img.shields.io/pypi/l/pyintervals.svg?style=flat-square&color=blue\n   :target: https://pypi.python.org/pypi/pyintervals\n\n.. image:: https://img.shields.io/badge/mypy-strict-forestgreen?style=flat-square\n   :target: https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict\n\n.. image:: https://img.shields.io/badge/coverage-99%25-forestgreen?style=flat-square\n   :target: https://github.com/serkankalay/pyintervals\n\n.. image::  https://img.shields.io/github/actions/workflow/status/serkankalay/pyintervals/tests.yml?branch=master&style=flat-square\n   :target: https://github.com/serkankalay/pyintervals\n\n**Execute efficient interval operations in Python.**\n\n*(Currently in active development. Leave a* ⭐️ *on GitHub if you're interested how this develops!)*\n\nWhy?\n--------\n\nInspired by a discussion and initial implementation in a professional project\nand a library I've been using in one of my previous jobs, **pyintervals** is born.\n\nIntervals pop-up frequently in programming, specifically in domains where you\nhave an activity or a proxy for it.\n\n- Suppose you are implementing a single machine scheduling algorithm.\n  In order to schedule an operation, you need to makes sure that the machine is available\n  during your desired time of operation.\n- Or you are implementing a booking system and need to check\n  that the hotel has at least 1 room with desired number of beds for the dates selected.\n  For such cases, you need to control some information overlapping with an interval.\n\nAs the examples suggest, **pyintervals** defines intervals with date and time.\nHowever, adding support for other comparable types such as ``int``, ``float`` is also possible.\n\nHow?\n--------\n\nDeclare ``Interval`` objects with **pyintervals** and check whether they ``overlap`` with each other or\none ``contains`` the other.\n\n.. code-block:: python\n\n  from pyintervals import Interval, overlaps, contains\n  from datetime import datetime\n\n  my_first_interval = Interval(start=datetime(2017,5,20,12,15),end=datetime(2024,10,10,19,0))\n  my_second_interval = Interval(start=datetime(2024,10,6,7,21),end=datetime(2024,10,10,19,0))\n\n  overlaps(my_first_interval, my_second_interval)\n  >>> True\n\n  my_first_interval.overlaps_with(my_second_interval)\n  >>> True\n\n  contains(my_first_interval, my_second_interval)\n  >>> True\n\n  my_first_interval.contains(my_second_interval)\n  >>> True\n\n  my_third_interval=Interval(start=datetime(1988,5,21,10,45),end=datetime(1989,6,20,1,30))\n  overlaps(my_first_interval,my_third_interval)\n  >>> False\n\n  contains(my_first_interval,my_third_interval)\n  >>> False\n\n**pyintervals** also support `degenerate` intervals, which have their ``start`` equal to their ``end``.\n\n.. code-block:: python\n\n  my_degenerate_interval = Interval(start=datetime(2024,10,10,9,0), end=datetime(2024,10,10,9,0))\n\n  overlaps(my_first_interval, my_degenerate_interval)\n  >>> True\n\n  my_same_degenerate_interval = Interval(start=datetime(2024,10,10,9,0), end=datetime(2024,10,10,9,0))\n\n  overlaps(my_degenerate_interval, my_same_degenerate_interval)\n  >>> True\n\nWhat else?\n-----------\n\nInterval concept also leads to `aggregate value over time`. Let's dive with an example:\n\nLet there be a beautiful and exclusive patisserie and you heard it from a foodie friend.\nShe/he suggested you to go there as soon as possible.\nYou checked your agenda and seems you have an empty spot at your calendar starting at 12:30.\nThe place is open between 9:00-12:00 and 13:00 - 16:00 daily.\n\nIf you want to programatically check whether the shop is open at a given time **T**, then\nyou need to iterate over `all (in the worst case)` the time intervals the patisserie is open\nfor the time you are curious about, 12:30 in this case. This will take `O(n)` time.\n\nLinear time is nice but can we not improve it? Well, with **pyintervals**, you can! `(with an upcoming feature)`\nWhat we essentially are curious about is the status of that beautiful store at a given time.\n**pintervals** `will` allow you fetch this value in `O(log n)` time.\n\nSee roadmap_ for the list of available and upcoming features.\n\nWhen?\n---------\n\nStart with **pyintervals** right away with\n\n.. code-block:: bash\n\n  pip install pyintervals\n\n.. _roadmap:\n\nRoadmap\n---------\n**pyintervals** is in active development and not feature complete yet. Please see below\nfor completed and planned features.\n\nFeatures:\n\n✅ = implemented, 🚧 = planned, ❌ = not planned\n\n- Fundamentals:\n    - ✅ Overlap controls\n    - ✅ Contain controls\n- Interval Handler:\n    - 🚧 Own intervals with associated values\n    - 🚧 Provide value projection graph\n    - 🚧 Query value over time\n    - 🚧 Access intervals overlapping with a specific timespan\n- Single-level Pegging:\n    - 🚧 Introduce object association to Intervals\n    - 🚧 Single level pegging with first-in-first-out\n    - 🚧 Enable callback for pegging quantity\n    - 🚧 Enable callback for pegging matching\n- Support other comparable types\n    - 🚧 Define comparable protocol and generics\n    - 🚧 Adapt Interval and Interval Handler concepts\n\nAcknowledgements\n----------------\n\nFollowing resources and people have inspired **pyintervals**:\n\n- `Always use [closed, open) intervals <https://fhur.me/posts/always-use-closed-open-intervalshttps://fhur.me/posts/always-use-closed-open-intervals>`_\n- `Arie Bovenberg <https://github.com/ariebovenberg>`_\n- `pdfje (for initial setup of this project) <https://github.com/ariebovenberg/pdfje>`_\n- `Sam de Wringer <https://github.com/samdewr>`_\n- Tim Lamballais-Tessensohn\n",
    'author': 'Serkan Kalay',
    'author_email': 'serkanosmankalay@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/serkankalay/pyintervals',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
