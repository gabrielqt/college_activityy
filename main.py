from functions import *

number = randomnumbers()

for i in range(1,11):
    
    game = randomgame(number=number)
    
    if game == True:
        print('Você ganhou :D')
        break
    if i == 10:
        print(f'Você perdeu :( o número era {number}')
        break
    print(verify(randomnumber=number, usernumber=game))
