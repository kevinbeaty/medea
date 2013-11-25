"""
Medea tests
"""


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
