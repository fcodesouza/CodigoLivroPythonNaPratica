# é ou não primo.

n1 = 88
contador = 0

for i in range (n1, 1, -1):
    if n1 % i == 0:
        contador = contador + 1


if contador == 1:
    print(n1, 'é primo.')
else:
    print(n1, 'não é Primo.')
    print('Tem', contador, 'multiplos.')