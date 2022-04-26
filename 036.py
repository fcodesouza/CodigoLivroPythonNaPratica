# Iniciando a variavel que recebe um nome.
entrada = input('Digite um nome ou frase: ')

# Todos os caracteres em minusculo.
nome = entrada.lower()
#print (nome)

# Invertendo a variavel.
inverte = nome[::-1]
#print (inverte)

# Retirando os espaços entres as palavras.
nome1 = nome.replace(" ", "")
#print (nome1)

nome2 = inverte.replace(" ", "")
#print (nome2)

if nome1 == nome2:
    print(entrada)
    print('É um palindromo.')
else:
    print(entrada)
    print('Não é um palindromo.')