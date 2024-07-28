from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person,backref='pets') # note back ref is pets
    # is backref used for prefetch ?
    name = CharField()
    animal_type = CharField()
    class Meta:
        database = db

db.connect()

for person in Person.select():
    print(f"{person.name} {person.birthday}")

query = Pet.select().where(Pet.animal_type=='cat')

for pet in query:
    print(f'{pet.name}')

print("CAT AND OWNER - prevent n+1 behaviour")
query =(Pet
    .select(Pet,Person)
    .join(Person)
    .where(Pet.animal_type == 'cat'))
for pet in query:
    print(pet.name,pet.owner.name,pet.owner.birthday)
print("NEXT")

for pet in Pet.select().join(Person).where(Person.name=='b'):
    print(pet.name)


# getting person object from database
# h = Pet.create(owner = Person.select().where(Person.name=='p2').get(),name= "kitten45",animal_type="cat")

print("NEST2")
for pet in Pet.select().where(Pet.owner == Person.select().where(Person.name=='p2').get()).order_by(Pet.name):
    print(f" {pet.name} ")

print("NEW YOUNGEST TO OLDEST")
query = (Person
    .select()
    .order_by(Person.birthday.desc()))

for person in query:
    print(person.name,person.birthday)

d1900 = date(1900,1,1)
d2023 = date(2023,1,1)
print("NEXT#3")
query = (Person
        .select()
        .where(
            (Person.birthday < d1900) | (Person.birthday > d2023)))
for person in query:
    print(person.name,person.birthday)

print("NEXT4")
query = (Person
    .select()
    .where(Person.birthday.between(d1900,d2023)))

for person in query:
    print(person.name,person.birthday)
print("NEXT 5")
"""
for person in Person.select():
    print(person.name, person.pets.count(), 'pets')

Once again we've run into a classic example of N+1 query behavior. In this case, we're executing an additional query for every Person returned by the original SELECT
"""
# Select seems to be the table cols we need
print("NEEW")
query = (Person
            .select(Person, fn.COUNT(Pet.id).alias('pet_count'))
            .join(Pet,JOIN.LEFT_OUTER)# include people without pets
            .group_by(Person)
            .order_by(Person.name))
for person in query:
    print(person.name,person.pet_count,'pets') 
# lowercase and uppercase treated diff
# in peewee

#one pet can only have on owner
#one person can have 0 or many pets
print("NEEEWW2")
query = (Person
            .select(Person,Pet)
            .join(Pet,JOIN.LEFT_OUTER)
            .order_by(Person.name,Pet.name))

for person in query:
    if hasattr(person,'pet'):
        print(person.name,person.pet.name)
    else :
        print(person.name,'no pets')
print("Getting person and their associated pets")
query = Person.select().order_by(Person.name).prefetch(Pet)
for person in query:
    print(person.name)
    for pet in person.pets:
        print(' *',pet.name)
db.close()