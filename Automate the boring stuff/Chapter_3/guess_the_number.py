# This is the guss the number game
import random
secretNumber=random.randint(1,20)
print('I am thinking of a number between 1 to 20')
# Ask the player to guess 6 time
for gussesTaken in range(1,7):
    print('Take a guess')
    gusses=int(input())

    if gusses<secretNumber:
        print('Your guess is too low')
    elif gusses>secretNumber:
        print('Your guess is too high')
    else:
        break
    if gusses == secretNumber:
        print('Good job...you gussed the number in '+str(gussesTaken)+'gusses')
    else:
        print('nope the number i was thinking was '+str(secretNumber))
