#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

val = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário mensal? '))
temp = int(input('Em quantos anos vai pagar o emprestimo? '))

prest = val / (temp * 12)

if prest < sal * 30 / 100:
    s = 'aprovado'

else:
    s = 'negado'

print('A casa de R${:.2f} financiada em {} anos, tera {} prestações de R${:.2f}.\nPortanto o emprestimo foi {}!'.format(val , temp , temp * 12 , prest , s))