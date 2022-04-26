# Inicialmente temos um dicionario aluno que contem nome e notas. Em notas podemos ver um conjunto de tres notas.

aluno = {'nome' : 'Panthro', 'notas' : [7, 8, 9]}

# Calculando a media:
def calcule_pontos():
    pontos_totais = float(sum(aluno['notas'])/3)
    return pontos_totais

# Trazendo o resultado para variaveis.
nome = aluno['nome']
pontos = calcule_pontos()

# Criando um noco dicionario com nome e notas.
media_aluno = dict(keys = nome, values = pontos)
print(media_aluno)

# Provando que media_aluno é um dicionario.
print(type(media_aluno))
