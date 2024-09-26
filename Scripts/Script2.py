#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('digite um numero inteiro: '))

print('{}MENU{}\n[1] Converter para BINÁRIO.\n[2] Converter para OCTAL.\n[3] Converter para HEXADECIMAL\n{}'.format('=' * 14 , '=' * 14 , '=' * 32))

op = int(input('qual opção? '))

if op == 1:
    convert = bin(num)
    op = str('BINÁRIO')
elif op == 2:
    convert = oct(num)
    op = str('OCTAL')
elif op == 3:
    convert = hex(num)
    op = str('HEXADECIMAL')

else:
    print('opção invalida... PROGRAMA ENCERRADO...')

print('O numero {} convertido para {} fica: {}.'.format(num , op , convert[3:]))