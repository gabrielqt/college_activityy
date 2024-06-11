from random import randint

def randomnumbers():
    number = randint(1,100)
    return number

def randomgame(number):
    
    usuario = int(input('Tente acertar o número sorteado:'))
    
    if usuario == number:
        print('Você acertou')
        return True
    
    return usuario
    
    
def verify(randomnumber, usernumber):
    
    if randomnumber > usernumber:
        
        
        return 'O número sorteado é maior'
    
    elif randomnumber < usernumber:
        
        return 'O número sorteado é menor'
