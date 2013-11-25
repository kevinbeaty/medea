"""
MedeaMapper test
"""
from . import Person
from .. import MedeaMapper


def test_object_args_to_json():
    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')

    mapper = MedeaMapper('first_name', 'last_name')
    bob_json = {
        'first_name': 'Bob',
        'last_name': 'Hope'}

    assert mapper.to_json(bob) == bob_json

    mapper = MedeaMapper('first_name', 'last_name',
                         'address', 'phone_number', 'dob')

    bob_json = {
        'first_name': 'Bob',
        'last_name': 'Hope',
        'address': '123 Main',
        'phone_number': '123',
        'dob': '1903-05-29'}

    assert mapper.to_json(bob) == bob_json


def test_object_args_from_json():
    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')
    assert bob.first_name == 'Bob'
    assert bob.last_name == 'Hope'
    assert bob.address == '123 Main'
    assert bob.phone_number == '123'
    assert bob.dob == '1903-05-29'

    fred = Person('Fred', 'Rodgers', '234 Rock', '456', '1928-03-20')
    assert fred.first_name == 'Fred'
    assert fred.last_name == 'Rodgers'
    assert fred.address == '234 Rock'
    assert fred.phone_number == '456'
    assert fred.dob == '1928-03-20'

    bob_json = {
        'first_name': 'Bob',
        'last_name': 'Hope'}

    bob_json_full = {
        'first_name': 'Bob',
        'last_name': 'Hope',
        'address': '123 Main',
        'phone_number': '123',
        'dob': '1903-05-29'}

    fred_json = {
        'first_name': 'Fred',
        'last_name': 'Rodgers'}

    fred_json_full = {
        'first_name': 'Fred',
        'last_name': 'Rodgers',
        'address': '234 Rock',
        'phone_number': '456',
        'dob': '1928-03-20'}

    mapper = MedeaMapper('first_name', 'last_name')
    mapper_full = MedeaMapper('first_name', 'last_name',
                              'address', 'phone_number', 'dob')

    assert mapper.to_json(bob) == bob_json
    assert mapper.to_json(fred) == fred_json
    assert mapper_full.to_json(bob) == bob_json_full
    assert mapper_full.to_json(fred) == fred_json_full

    # Override Bob's name from Fred
    mapper.from_json(fred_json, bob)

    # Mapper only serializes names
    assert mapper.to_json(bob) == fred_json
    assert mapper_full.to_json(bob) != bob_json_full
    assert bob.first_name == 'Fred'
    assert bob.last_name == 'Rodgers'
    assert bob.address == '123 Main'
    assert bob.phone_number == '123'
    assert bob.dob == '1903-05-29'

    # Revert back to Bob's name
    mapper.from_json(bob_json, bob)
    assert mapper.to_json(bob) == bob_json
    assert mapper_full.to_json(bob) == bob_json_full

    # Map Fred onto Bob using only name
    mapper_full.from_json(fred_json, bob)

    assert mapper.to_json(bob) == fred_json
    assert mapper_full.to_json(bob) != bob_json_full
    assert bob.first_name == 'Fred'
    assert bob.last_name == 'Rodgers'
    assert bob.address == '123 Main'
    assert bob.phone_number == '123'
    assert bob.dob == '1903-05-29'

    # Revert back to Bob's name
    mapper.from_json(bob_json, bob)
    assert mapper.to_json(bob) == bob_json
    assert mapper_full.to_json(bob) == bob_json_full

    # Map Fred onto Bob
    mapper_full.from_json(fred_json_full, bob)
    assert mapper_full.to_json(bob) == fred_json_full

    # Map Bob back onto Bob
    mapper_full.from_json(bob_json_full, bob)
    assert mapper_full.to_json(bob) == bob_json_full


def test_object_kwargs_to_json():
    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')

    mapper = MedeaMapper(first_name='firstName', last_name='lastName')
    bob_json = {
        'firstName': 'Bob',
        'lastName': 'Hope'}

    assert mapper.to_json(bob) == bob_json

    mapper = MedeaMapper('address', 'dob',
                         first_name='firstName', last_name='lastName')

    bob_json = {
        'firstName': 'Bob',
        'lastName': 'Hope',
        'address': '123 Main',
        'dob': '1903-05-29'}

    assert mapper.to_json(bob) == bob_json


def test_object_kwargs_from_json():
    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')
    assert bob.first_name == 'Bob'
    assert bob.last_name == 'Hope'
    assert bob.address == '123 Main'
    assert bob.phone_number == '123'
    assert bob.dob == '1903-05-29'

    fred = Person('Fred', 'Rodgers', '234 Rock', '456', '1928-03-20')
    assert fred.first_name == 'Fred'
    assert fred.last_name == 'Rodgers'
    assert fred.address == '234 Rock'
    assert fred.phone_number == '456'
    assert fred.dob == '1928-03-20'

    bob_json = {
        'firstName': 'Bob',
        'lastName': 'Hope'}

    bob_json_full = {
        'firstName': 'Bob',
        'lastName': 'Hope',
        'address': '123 Main',
        'phoneNumber': '123',
        'DOB': '1903-05-29'}

    fred_json = {
        'firstName': 'Fred',
        'lastName': 'Rodgers'}

    fred_json_full = {
        'firstName': 'Fred',
        'lastName': 'Rodgers',
        'address': '234 Rock',
        'phoneNumber': '456',
        'DOB': '1928-03-20'}

    mapper = MedeaMapper(first_name='firstName', last_name='lastName')
    mapper_full = MedeaMapper('address',
                              first_name='firstName', last_name='lastName',
                              phone_number='phoneNumber', dob='DOB')

    assert mapper.to_json(bob) == bob_json
    assert mapper.to_json(fred) == fred_json
    assert mapper_full.to_json(bob) == bob_json_full
    assert mapper_full.to_json(fred) == fred_json_full

    # Override Bob's name from Fred
    mapper.from_json(fred_json, bob)

    # Mapper only serializes names
    assert mapper.to_json(bob) == fred_json
    assert mapper_full.to_json(bob) != bob_json_full
    assert bob.first_name == 'Fred'
    assert bob.last_name == 'Rodgers'
    assert bob.address == '123 Main'
    assert bob.phone_number == '123'
    assert bob.dob == '1903-05-29'

    # Revert back to Bob's name
    mapper.from_json(bob_json, bob)
    assert mapper.to_json(bob) == bob_json
    assert mapper_full.to_json(bob) == bob_json_full

    # Map Fred onto Bob using only name
    mapper_full.from_json(fred_json, bob)

    assert mapper.to_json(bob) == fred_json
    assert mapper_full.to_json(bob) != bob_json_full
    assert bob.first_name == 'Fred'
    assert bob.last_name == 'Rodgers'
    assert bob.address == '123 Main'
    assert bob.phone_number == '123'
    assert bob.dob == '1903-05-29'

    # Revert back to Bob's name
    mapper.from_json(bob_json, bob)
    assert mapper.to_json(bob) == bob_json
    assert mapper_full.to_json(bob) == bob_json_full

    # Map Fred onto Bob
    mapper_full.from_json(fred_json_full, bob)
    assert mapper_full.to_json(bob) == fred_json_full

    # Map Bob back onto Bob
    mapper_full.from_json(bob_json_full, bob)
    assert mapper_full.to_json(bob) == bob_json_full
