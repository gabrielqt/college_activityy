from functions import *

number = randomnumbers()

for i in range(1,11):
    
    game = randomgame(number=number)
    if game == True:
        break
    print(verify(randomnumber=number, usernumber=game))
