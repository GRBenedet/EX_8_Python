#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

from time import sleep

itens = ('Pedra' , 'Papel' , 'Tesoura')

sis = randint(0, 2)

print('escolha um opção: \n[1]Pedra\n[2]Papel\n[3]Tesoura')

op = int(input()) - 1

if sis == 0 and op == 2 or sis == 2 and op == 1 or sis == 1 and op == 0:
    win = 'machine WINS'

elif sis == op:
    win = 'empate'

else:
    win = 'player WINS'

sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔÔÔÔÔÔÔÔÔ!!!!')

print('A maquina jogou {} e você jogou {}, e o resultado foi, {}.'.format(itens[sis] , itens[op] , win))