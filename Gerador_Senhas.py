import random
import re

letras_maiusculas = [chr(i) for i in range(65, 91)]
letras_minusculas = [chr(i) for i in range(97, 123)]
numeros = [str(i) for i in range(10)]
simbolos = ['!', '@', '#', '$', '%']
caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos


def verificar_senha(senha):

    # Verificar se a senha contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False

    # Verificar se a senha contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False

    # Verificar se a senha contém pelo menos um número
    if not re.search(r'[0-9]', senha):
        return False

    # Verificar se a senha contém pelo menos um símbolo
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False

    # Se todas as condições forem atendidas, a senha é considerada válida
    return True


def gera_senha(tam):

    while True:

        senha_gerada = ''

        for carac in range(0, tam):

            senha_gerada += random.choice(caracteres)

        # Pega o resultado
        result = verificar_senha(senha_gerada)

        # Se falso, continua o loop
        if result:

            return senha_gerada


tamanho = 8
key = gera_senha(tamanho)
print(key)

