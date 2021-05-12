CRUD Operations

CREATE = Add brand new item to the table
READ = Look at the table, can be 1 row or multiple or all depending on the query
UPDATE = Edit a table row.  All values but the id can be updated.  You can only edit 1 item or row at a time. 
DELETE = Remove a table row. This is only 1 item or row that will / can be removed

Table Relationships

one-to-one = example - 1 ssn can only belong to 1 person and 1 person can only have 1 ssn
one-to-many = example - 1 zoo can have more than 1 animal but that animal can only belong to 1 zoo
many-to-many = example - you can have a store type that is at multiple zoos and a zoo can have more than one store type

Create new zooApp (one that we can fully go full stack on)

Models:
zoo = one to one
animal = one to one
animal-zoo = one to many
employee's = one to one
zoo to employee = one to many
shop = one to one
shop-zoo = many to many

Class:
zoo - zooName zooLocation
animal - animalType animalName animalBirthday
animal-zoo - assign animals to a zoo while adding animal
employee - firstName lastName email
employee-zoo assign employee to specific zoo while adding employee
shop - shopName shopDescription
shop-zoo - allow to add different shops to multiple zoos

Eventually we will add organizer/owner pages where they can log in and manipulate what is at each zoo


Relationship Examples and where to put them

here is a 1 to many:
Each manuafacturer can have many cars but 1 car can only have one manufacturer
class Manufacturer:
    name

class Car:
    type
    manufacturer foreignKey

here is a many to many:
Pizza's can have many toppings and many pizzas can have different toppings

class Topping:
    toppingName

class Pizza:
    toppings  manytomany