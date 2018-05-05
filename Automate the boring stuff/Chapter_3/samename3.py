def spam():
    global eggs
    eggs='spam' # this is the global,because there is global statement
def bacon():
    eggs='bacon' # this is a local,because there is assignment oprator
def ham():
    print(eggs) #this is global,because there is no assigment and global statement
eggs=42 # Eggs is global variable
spam()
print(eggs)
