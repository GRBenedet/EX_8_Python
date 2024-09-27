#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida


alt = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))

imc = peso / alt**2

if imc < 18.5:
    s = 'abaixo do peso' 

elif imc < 25:
    s = 'no peso ideal'

elif imc < 30:
    s= 'no sobrepeso'

elif imc < 40:
    s = 'obsidade'
else:
    s = 'com Obesidade Mórbica'

print('Com base no seu peso ({:.2f}KG) e na sua altura ({:.2f}m) você tem um IMC de {:.1f} e está {}.'.format(peso , alt , imc , s))
