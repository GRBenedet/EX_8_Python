#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('digite seu ano de nascimento: '))

idade = date.today().year - nasc

if idade == 18 or idade == 17:
    print('esta na hora de se alistar.')

elif idade > 18:
    print('Seu alistamento esta atrasado em {} anos.'.format(18 - idade))

else:
    print('falta {} anos para para seu alistamente.'.format(18 - idade))