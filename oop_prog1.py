class Parrot:

    #class attribute
    species = "bird"

    # instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age

#instance the parrot class
blue = Parrot("Blue",10)
woo = Parrot("woo",15)

# access the class attributes
print("Blu is {}".format(blue.__class__.species))
print("Woo is {}".format(woo.__class__.species))

#access the instance attributes
print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(woo.name, woo.age))