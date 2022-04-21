from time import sleep

tempo = 20

for i in range(tempo, -1, -1):
    sleep(1)
    print(i)
print('Fim.')