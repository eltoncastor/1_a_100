# Criar um programa que gere um número de 1 a 100 e que o usuário deve ficar tentando até adivinhar
# o programa também deve dar dicas (maior ou menor) e ter uma validação de erros do tipo ValueError

from time import sleep
from functions import colors, clear, titulo, gerado, usuario, continuar


num = gerado()
tentativa = 0
continua = True
clear()

input(f'{colors.yellow}Pressione ENTER para inciar...{colors.end}')
while continua:
    try:
        sleep(0.3)
        clear()
        titulo()
        
        user = usuario()
        
        print(f'Você chutou {colors.pink_bold}{user}{colors.end}')
        sleep(1.5)
        if user == num and tentativa == 0:
            print(f'{colors.green}UAU! VOCÊ VENCEU {colors.blue}DE PRIMEIRA{colors.green}! MUITO BEM!{colors.end}')
            continua = continuar()
            tentativa = 0
        elif user == num:
            tentativa += 1
            print(f'{colors.green}Parabéns! Você acertou com um total de {colors.blue}{tentativa} tentativas{colors.green}!{colors.end}')
            continua = continuar()
            tentativa = 0
        else:
            if user > num:
                print(f'Não foi dessa vez. Chute um número {colors.red_bold}MENOR!{colors.end}')
                tentativa +=1
            elif user < num:
                print(f'Não foi dessa vez. Chute um número {colors.green_bold}MAIOR!{colors.end}')
                tentativa +=1
        sleep(1.7)
        
        
    except ValueError:
        print(f'{colors.red_bold}[ERRO] {colors.red}Por favor, digite um número inteiro.{colors.end}')
        sleep(2)
        
    



