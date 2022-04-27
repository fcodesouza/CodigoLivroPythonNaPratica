def soma (*args):
    num = 0

    for valor in args:
        num += valor

    print(f'A soma é {num}.')

soma = soma(18, 43, 99, 1)