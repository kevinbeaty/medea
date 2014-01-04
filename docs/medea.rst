medea
=====

`medea` is a singledispatch function for JSON encoding. 

lists, tuples and sequences are converted to lists.
Items and values of dicts are recursively dispatched.
Other types should be registered with dispatch function.

.. code-block:: python

    medea.register(date, lambda obj: obj.strftime('%Y-%m-%d'))

    dob = date(1974, 3, 1)
    assert medea(dob) == '1974-03-01'

    bob = {
        'name': 'Bob',
        'age': 38,
        'colors': ('blue', 'red'),
        'dob': dob}

    assert medea(bob) == {
        'name': 'Bob',
        'age': 38,
        'colors': ['blue', 'red'],
        'dob': '1974-03-01'}


Custom objects can be registered with a :doc:`mapper`:

MedeaEncoder
============

`MedeaEncoder` is a `JSONEncoder` using the `medea` function.
