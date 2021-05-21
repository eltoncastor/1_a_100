# Criar um programa que gere um número de 1 a 100 e que o usuário deve ficar tentando até adivinhar
# o programa também deve dar dicas (maior ou menor) e ter uma validação de erros do tipo ValueError
import os
from random import randrange
from time import sleep


class colors():
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    yellow = '\033[33m'
    pink = '\033[35m'
    white = '\033[30m'
    end = '\033[m'
    
    red_bold = '\033[31;1m'


def clear():
    return os.system('cls' if os.name=='nt' else 'clear')

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
    
    
def gerado():
    num = randrange(1,101)
    return num


def usuario():
    print('')
    user = int(input('Que número pensei? '))
    return user


def continuar():
    while True:
        again = str(input('Deseja jogar novamente? (s/n) '))
        if again.lower().strip()[0] == 's':
            print('Ok! Vamos jogar novamente!')
            return True
        elif again.lower().strip()[0] == 'n':
            clear()
            print('Ok!')
            sleep(0.7)
            print('Finalizando jogo...')
            sleep(0.7)
            print('Até a próxima!')
            return False
        else:
            print(f'{colors.red_bold}[ERRO] {colors.red}Por favor, responda com "s" ou "n".{colors.end}')
        
        
######################################################

num = gerado()
tentativa = 0
continua = True
clear()

input('Pressione ENTER para inciar...')
while continua:
    try:
        sleep(0.3)
        clear()
        titulo()
        
        user = usuario()
        
        print(f'Você chutou {user}')
        sleep(1.5)
        if user == num and tentativa == 0:
            print('UAU! VOCÊ VENCEU DE PRIMEIRA! MUITO BEM!')
            continua = continuar()
        elif user == num:
            tentativa += 1
            print(f'Parabéns! Você acertou com um total de {tentativa} tentativas!')
            continua = continuar()
        else:
            if user > num:
                print('Não foi dessa vez. Chute um número MENOR!')
                tentativa +=1
            elif user < num:
                print('Não foi dessa vez. Chute um número MAIOR!')
                tentativa +=1
        sleep(2.5)
        
        
    except ValueError:
        print(f'{colors.red_bold}[ERRO] {colors.red}Por favor, digite um número inteiro.{colors.end}')
        sleep(2)
        
    



