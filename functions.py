import os
from random import randrange
from time import sleep


class colors():
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    yellow = '\033[33m'
    pink = '\033[35m'
    white = '\033[37m'
    end = '\033[m'
    
    red_bold = '\033[31;1m'
    green_bold = '\033[32;1m'
    blue_bold = '\033[36;1m'
    yellow_bold = '\033[33;1m'
    pink_bold = '\033[35;1m'
    white_bold = '\033[37;1m'

    blue_back = '\033[46;31;1m'
    yellow_back = '\033[43;31;1m'
    pink_back = '\033[45;36;1m'
    

def clear():
    return os.system('cls' if os.name=='nt' else 'clear')

def titulo():
    def traços():
        print('|'+(' '*28)+'|')
        
    print(f'{colors.blue_back}.'*30)
    traços()
    traços()
    print('|ADIVINHE O NÚMERO DE 1 A 100|'.center(30))
    traços()
    traços()
    print('.'*30)
    print(colors.end)
    
    
def gerado():
    num = randrange(1,2)
    return num


def usuario():
    print('')
    user = int(input(f'{colors.yellow}Que número pensei? {colors.end}'))
    return user


def continuar():
    while True:
        again = str(input('Deseja jogar novamente? (s/n) '))
        
        if again.lower().strip() == 's':
            print(f'{colors.green}Ok! Vamos jogar novamente!{colors.end}')
            sleep(0.8)
            return True
        elif again.lower().strip() == 'n':
            clear()
            print(f'{colors.pink}Ok!')
            sleep(0.7)
            print('Finalizando jogo...')
            sleep(0.7)
            print(f'Até a próxima!{colors.end}')
            return False
        else:
            print(f'{colors.red_bold}[ERRO] {colors.red}Por favor, responda com "s" ou "n".{colors.end}')
        
        