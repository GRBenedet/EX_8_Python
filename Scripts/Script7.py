#Refaça o EX_7_parte_8, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = int(input('defina a primeira reta: '))
b = int(input('defina a segunda reta: '))
c = int(input('defina a terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    tf = 'pode'

    if a == b and a == c and b == c:
        tipo = 'Equilátero'

    elif a == b and a != c or a == c and a != b:
        tipo = 'Isósceles'

    elif a != b and a != c and b != c:
        tipo = 'Escaleno'
    
    print('as retas {}, {} e {} {} formar um triangulo {}.'.format(a , b , c , tf, tipo))

else:
    print('as retas {}, {} e {} não pode formar um triangulo.'.format(a , b , c))