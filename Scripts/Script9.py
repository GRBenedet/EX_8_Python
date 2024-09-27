#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

preco = float(input('Qual o valor do produto: '))

print('selecione a forma de pagamento:\n{}menu{}\n[1] A vista\n[2] Parcelado\n{}'.format('=' * 10, '=' * 10 , '=' * 24))

op = int(input())

if op == 1:

    print('{}menu{}\n[1] dinheiro\n[2] Cheque\n[3] Cartão\n{}'.format('=' * 10 , '=' * 10 , '=' * 24))

    op = int(input())

    if op == 1 or op == 2:
        desc = '10% de desconto'
        fpreco = preco - preco * 10 / 100
        form = 'a vista'

    elif op == 3:
        desc = '5% de desconto'
        fpreco = preco - preco * 10 / 100
        form = 'a vista'

    else:
        print('opção invalida, DESLIGANDO...')

elif op == 2:

    print('{}menu{}\n[1] 2x sem juros\n[2] Mais vezes com juros\n{}'.format('=' * 10 , '=' * 10 , '=' * 24))

    op = int(input())

    if op == 1:
        desc  = 'nenhum desconto'
        form = 'parcelada'
        parc = 2
        fpreco = preco / parc

    elif op == 2:
        desc  = '20% de juros'
        form = 'parcelada'
        parc = int(input('quantas parcelas? '))
        fpreco = (preco + preco * 20 / 100) / parc

    else:
        print('opção invalida, DESLIGANDO...')

else:
    print('opção invalida, DESLIGANDO...')

print('Com o valor de produto sendo R${:.2f}, você escolheu a forma de pagamento {}, recebendo {}, ficando um total de {} parcelas R${:.2f}.'.format(preco , form , desc , parc , fpreco))