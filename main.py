# Criar um programa que gere um número de 1 a 100 e que o usuário deve ficar tentando até adivinhar
# o programa também deve dar dicas (maior ou menor) e ter uma validação de erros do tipo ValueError
import os
from random import randrange


class colors():
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    yellow = '\033[33m'
    pink = '\033[35m'
    end = '\033[m'


def titulo():
    def traços():
        print('|'+(' '*28)+'|')
        
    os.system('cls' if os.name=='nt' else 'clear')   
    print('#'*30)
    traços()
    traços()
    print('|     ADIVINHE O NÚMERO!     |'.center(30))
    traços()
    traços()
    print('#'*30)
    
    
def gerado():
    num = randrange(1,101)
    return num


def usuario():
    user = int(input('Adivinhe o número: '))
    return user




try:
    gerado = gerado()
    while True:
        
        titulo()
        
        
    
except ValueError:
    print('[ERRO] Por favor, digite um número inteiro.')


