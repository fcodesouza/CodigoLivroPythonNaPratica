msg1 = ('\nVocê errou, buáááááá... \nFIM.')
cont = 0

print('BEM VINDO AO FANTASTICO - PERGUNTAS E RESPOSTA!!!')
r1 = (int(input('VOCÊ ESTA PREPARADO? \n1 para SIM. \n2 para NÃO. \n>>> ')))

if r1 == 1:
    rp1 = int(input('\nQuando é 2  + 2? '))
    if rp1 == 4:
        cont += 1
        print('Parabens!\n')
    else:
        print(msg1)
        exit()

    print('Vamos para a próxima?')
    r1 = (int(input('VOCÊ ESTA PREPARADO? \n1 para SIM. \n2 para NÃO. \n>>> ')))

    if r1 == 1:
        rp1 = int(input('\nQual o quadrado de 9? '))
        if rp1 == 81:
            cont += 1
            print('Parabens!\n')
        else:
            print(msg1)
            exit()

    print('Vamos para a próxima?')
    r1 = (int(input('VOCÊ ESTA PREPARADO? \n1 para SIM. \n2 para NÃO. \n>>> ')))

    if r1 == 1:
        rp1 = int(input('\nQual a raiz quadrada de 49? '))
        if rp1 == 7:
            cont += 1
            print('Parabens!\n')
        else:
            print(msg1)
            exit()

else:
    print(f'Você acertou {cont} perguntas!\nFIM.')
    exit()

print(f'Você acertou {cont} perguntas!\nFIM.')