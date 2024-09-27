#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

nasc = int(input('Digite o ano de seu nascimento: '))

idade = date.today().year - nasc

if idade <= 9:
    cat = 'MIRIM'

elif idade <= 14:
    cat = 'INFANTIL'

elif idade <= 19:
    cat = 'JÚNIOR'

elif idade <= 25:
    cat = 'SÊNIOR'

else: 
    cat = 'MASTER'

print('A sua categoria é {}.'.format(cat))