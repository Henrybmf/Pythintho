
classif_Imc = {'PesoBaixo': 'Abaixo de 18.5', 'Ideal': 'Entre 18.5 e 24.9', 'Sobrepeso': 'Entre 25.0 e 29.9',
               'Obeso': 'Acima de 30'}


def calculadoraImc(altura_, peso_):

    imc = peso_ / (altura_ ** 2)
    return imc


def classifacaoDeImc(imc):

    if imc < 18.5:

        print('Abaixo do peso!')

    elif imc < 24.9:

        print('Peso ideal!')

    elif imc < 29.9:

        print('Sobrepeso!')

    elif imc >= 30.0:

        print('Obeso!')


def mostraTabela():

    print(f'\nCLASSIFICAÇÃO     IMC')
    for k, v in classif_Imc.items():

        print(f'{k:15} {v}')


altura = float(input('Qual a sua altura?\n'))
peso = float(input('Qual o seu peso?\n'))
seu_imc = calculadoraImc(altura, peso)

mostraTabela()

print(f'\nSEU IMC: {seu_imc:.2f}')
classifacaoDeImc(seu_imc)
