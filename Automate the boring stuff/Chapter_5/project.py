#List to dictonary function for fantasy game inventory
#A list of string
#dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
#Function name addToInventory(inventory,addItems)
#from collections import Counter
#z=Counter(['blue', 'red', 'blue', 'yellow', 'blue', 'red'])
#print(z)
#!Python

#Chapter 5 Fantasy Game Inventory Practice
#!Python

#Chapter 5 Fantasy Game Inventory Practice

inv = {'rope': 1, 'gold coin': 42}

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']


def addToInventory(inventory, addItems):
    for k in range(len(addItems)):
        if addItems[k] in inventory.keys():
            inventory[addItems[k]] += 1
        else:
            inventory.setdefault(addItems[k], 1)
    return inventory


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

