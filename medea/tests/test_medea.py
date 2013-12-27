from .. import medea
from datetime import date


def test_medea():
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
