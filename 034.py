''' O livro equivoca-se em afirmar que o numero deve dividir por 3
e se o resto for zero ele observa como impar.
Por este motivo o numero 1 fica de fora mesmo sendo impar.
'''


n1 = 1
n2 = 100
contagem = 0
acomulado = 0

for i in range(n1, n2+1):
    if i % 2 != 0:
        #print(i)
        contagem = contagem + 1
        acomulado = acomulado + i

print(contagem, 'impares.')
print(acomulado, 'é a soma de todos os 50 numeros impares.')