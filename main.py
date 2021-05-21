# Criar um programa que gere um número de 1 a 100 e que o usuário deve ficar tentando até adivinhar
# o programa também deve dar dicas (maior ou menor) e ter uma validação de erros do tipo ValueError
import os


def titulo():
    def traços():
        print('|'+(' '*28)+'|')
        
    print('#'*30)
    traços()
    traços()
    print('|     ADIVINHE O NÚMERO!     |'.center(30))
    traços()
    traços()
    print('#'*30)
    
os.system('cls' if os.name=='nt' else 'clear')
titulo()