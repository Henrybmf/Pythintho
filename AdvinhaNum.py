from time import sleep
import random


def jogo_dos_numeros():

    num_usuario = int(input('Acerte o número de 1 a 10! :)  '))

    num = random.choice(range(1, 10))
    print('Conferindo resultados...')
    sleep(1)

    if num_usuario == num:

        print(f'BOA! O número era {num}><')

    else:

        print(f'BURRO! O número era {num}.')


jogo_dos_numeros()
