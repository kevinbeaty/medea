"""
Medea
-----

Simple utilities to map JSON to and from Python Objects.

MedeaMapper
```````````

Create a mapper using Python attribute names as arguments.  Attributes that are
not whitelisted will not be serialized:

.. code:: python
    class Person(object):
        def __init__(self, first_name, last_name,
                     address='', phone_number='', dob=''):
            self.first_name = first_name
            self.last_name = last_name
            self.address = address
            self.phone_number = phone_number
            self.dob = dob


    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')

    mapper = MedeaMapper('first_name', 'last_name',
                         'address', 'phone_number', 'dob')

    bob_json = {
        'first_name': 'Bob',
        'last_name': 'Hope',
        'address': '123 Main',
        'phone_number': '123',
        'dob': '1903-05-29'}

    assert mapper.to_json(bob) == bob_json

Attribute names can be overridden using `**kwargs`.

.. code:: python
    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')

    mapper = MedeaMapper('address', 'dob',
                         first_name='firstName', last_name='lastName')

    bob_json = {
        'firstName': 'Bob',
        'lastName': 'Hope',
        'address': '123 Main',
        'dob': '1903-05-29'}

    assert mapper.to_json(bob) == bob_json

MedeaCamelMapper may be useful if JSON is camel cased.

.. code:: python
    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')

    mapper = MedeaCamelMapper('first_name', 'last_name',
                              'address', 'phone_number', 'dob')

    bob_json = {
        'firstName': 'Bob',
        'lastName': 'Hope',
        'address': '123 Main',
        'phoneNumber': '123',
        'dob': '1903-05-29'}

    assert mapper.to_json(bob) == bob_json

A mapper can also map attribues from JSON onto the object:

.. code:: python
    bob = Person('Bob', 'Hope', '123 Main', '123', '1903-05-29')

    bob_json_full = {
        'firstName': 'Bob',
        'lastName': 'Hope',
        'address': '123 Main',
        'phoneNumber': '123',
        'DOB': '1903-05-29'}

    fred_json = {
        'firstName': 'Fred',
        'lastName': 'Rodgers'}

    mapper = MedeaCamelMapper('first_name', 'last_name')
    mapper_full = MedeaCamelMapper('first_name', 'last_name',
                                   'address', 'phone_number', dob='DOB')

    assert mapper.to_json(bob) == bob_json
    assert mapper_full.to_json(bob) == bob_json_full

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

MedeaEncoder
````````````

A `MedeaEncoder` extends `JSONEncoder` to encode objects using a `MedeaMapper`.
The mapper is defined as `__medea_mapper__`  on a `MedeaEncoderMixin` class.

NOTE: The `MedeaEncoder` will extend the Flask encoder if installed.

.. code:: python
    class Pet(MedeaEncoderMixin):
        __medea_mapper__ = MedeaCamelMapper('name', 'kind')


    class Dog(Pet):
        def __init__(self, name):
            self.name = name
            self.kind = 'Dog'


    class Cat(Pet):
        def __init__(self, name):
            self.name = name
            self.kind = 'Cat'


    class PetPerson(Person, MedeaEncoderMixin):
        __medea_mapper__ = MedeaCamelMapper('first_name', 'last_name', 'pets')

    encoder = MedeaEncoder()
    anne = PetPerson('Anne', 'Frank')
    fido = Dog('Fido')
    spot = Dog('Spot')
    garfield = Cat('Garfield')

    anne.pets = [fido, spot, garfield]

    assert json.loads(encoder.encode(anne)) == {
        'firstName': 'Anne',
        'lastName': 'Frank',
        'pets': [
            {'kind': 'Dog', 'name': 'Fido'},
            {'kind': 'Dog', 'name': 'Spot'},
            {'kind': 'Cat', 'name': 'Garfield'}]}

"""
from setuptools import setup

setup(
    name='Medea',
    version='0.2',
    url='http://github.com/kevinbeaty/medea',
    license='MIT',
    author='Kevin Beaty',
    author_email='kevin@simplectic.com',
    description='JSON Object Mapper / Encoder',
    long_description=__doc__,
    packages=['medea'],
    include_package_data=False,
    zip_safe=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup'],
    cmdclass={},
    test_suite=''
)
