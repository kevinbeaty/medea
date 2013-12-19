import json
from . import Person
from .. import MedeaCamelMapper, MedeaEncoder, register_mapper, medea


class Pet(object):
    pass

register_mapper(Pet, MedeaCamelMapper('name', 'kind'))


class Dog(Pet):
    def __init__(self, name):
        self.name = name
        self.kind = 'Dog'


class Cat(Pet):
    def __init__(self, name):
        self.name = name
        self.kind = 'Cat'


class PetPerson(Person):
    pass

register_mapper(PetPerson, MedeaCamelMapper('first_name', 'last_name', 'pets'))


def test_medea_mapper():
    anne = PetPerson('Anne', 'Frank')
    assert medea(anne) == {
        'firstName': 'Anne',
        'lastName': 'Frank'}

    fido = Dog('Fido')
    assert medea(fido) == {
        'kind': 'Dog', 'name': 'Fido'}

    spot = Dog('Spot')
    assert medea(spot) == {
        'kind': 'Dog', 'name': 'Spot'}

    garfield = Cat('Garfield')
    assert medea(garfield) == {
        'kind': 'Cat', 'name': 'Garfield'}

    anne.pets = [fido, spot, garfield]
    assert medea(anne) == {
        'firstName': 'Anne',
        'lastName': 'Frank',
        'pets': [
            {'kind': 'Dog', 'name': 'Fido'},
            {'kind': 'Dog', 'name': 'Spot'},
            {'kind': 'Cat', 'name': 'Garfield'}]}


def test_encoder_dumps():
    anne = PetPerson('Anne', 'Frank')
    assert json.loads(json.dumps(anne, cls=MedeaEncoder)) == {
        'firstName': 'Anne',
        'lastName': 'Frank'}

    fido = Dog('Fido')
    assert json.loads(json.dumps(fido, cls=MedeaEncoder)) == {
        'kind': 'Dog', 'name': 'Fido'}

    spot = Dog('Spot')
    assert json.loads(json.dumps(spot, cls=MedeaEncoder)) == {
        'kind': 'Dog', 'name': 'Spot'}

    garfield = Cat('Garfield')
    assert json.loads(json.dumps(garfield, cls=MedeaEncoder)) == {
        'kind': 'Cat', 'name': 'Garfield'}

    anne.pets = [fido, spot, garfield]
    assert json.loads(json.dumps(anne, cls=MedeaEncoder)) == {
        'firstName': 'Anne',
        'lastName': 'Frank',
        'pets': [
            {'kind': 'Dog', 'name': 'Fido'},
            {'kind': 'Dog', 'name': 'Spot'},
            {'kind': 'Cat', 'name': 'Garfield'}]}


def test_encoder():
    encoder = MedeaEncoder()
    anne = PetPerson('Anne', 'Frank')
    assert json.loads(encoder.encode(anne)) == {
        'firstName': 'Anne',
        'lastName': 'Frank'}

    fido = Dog('Fido')
    assert json.loads(encoder.encode(fido)) == {
        'kind': 'Dog', 'name': 'Fido'}

    spot = Dog('Spot')
    assert json.loads(encoder.encode(spot)) == {
        'kind': 'Dog', 'name': 'Spot'}

    garfield = Cat('Garfield')
    assert json.loads(encoder.encode(garfield)) == {
        'kind': 'Cat', 'name': 'Garfield'}

    anne.pets = [fido, spot, garfield]
    assert json.loads(encoder.encode(anne)) == {
        'firstName': 'Anne',
        'lastName': 'Frank',
        'pets': [
            {'kind': 'Dog', 'name': 'Fido'},
            {'kind': 'Dog', 'name': 'Spot'},
            {'kind': 'Cat', 'name': 'Garfield'}]}
