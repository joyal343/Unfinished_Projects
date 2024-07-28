# Peewee will automatically infer the database table name from the name of the class. You can override the default name by specifying a table_name attribute in the inner “Meta” class

from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person,backref='pets')
    name = CharField()
    animal_type = CharField()
    class Meta:
        database = db

db.connect()

# db.create_tables([Person,Pet])

# x = Person(name = 'Han',birthday= date(1960,1,15))
# x.save()

# y = Person.create(name = 'xyz',birthday=date(1822,11,2))

# y.save()

# z = Person.select().where(Person.name=='Han').get()

# print(z.name)

# for person in Person.select():
    # print(person.name)

x = Person.create(name = 'a',birthday= date(7122,11,2))
y = Person.create(name = 'b',birthday= date(2022,11,2))
k1 = Pet.create(owner = x,name="k1",animal_type="cat")
k2 = Pet.create(owner = y,name="k2",animal_type="dog")

