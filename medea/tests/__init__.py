"""
JSONCamelMapper test
"""
from ..mapper import JSONCamelMapper


class Person(object):
    def __init__(self, first_name, last_name,
                 address='', phone_number='', dob=''):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.dob = dob

    def __repr__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


def test_object_camel_to_json():
    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')

    mapper = JSONCamelMapper('first_name', 'last_name')
    bob_json = {
        'firstName': 'Bob',
        'lastName': 'Hope'}

    assert mapper.to_json(bob) == bob_json

    mapper = JSONCamelMapper('first_name', 'last_name',
                             'address', 'phone_number', 'dob')

    bob_json = {
        'firstName': 'Bob',
        'lastName': 'Hope',
        'address': '123 Main',
        'phoneNumber': '123',
        'dob': '1903-05-29'}

    assert mapper.to_json(bob) == bob_json
