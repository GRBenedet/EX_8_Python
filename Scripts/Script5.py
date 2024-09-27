#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

fnota = (nota1 + nota2) / 2

if fnota < 5:
    s = 'REPROVADO'

elif fnota >= 5 and fnota <= 6.9:
    s = 'EM RECUPERAÇÃO'

else:
    s = 'APROVADO'

print('Com a media final de {:.1f} o aluno esta {}.'.format(fnota , s))