def spam():
    eggs='span local'
    print(eggs) # print spam local
def bacon():
    eggs='bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs='global'
bacon()
print(eggs)
