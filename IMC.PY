# calculadora de IMC

def principal():
    print("-=" * 20)
    peso = input('Peso (kg): ')
    peso_real = peso
    peso = peso[0:peso.find(".")]
    if peso.isnumeric():
        peso = float(peso_real)

    while type(peso) != float:
        peso = input('Peso inválido, digite novamente!\n'
                     'Peso (kg): ')
        peso_real = peso
        peso = peso[0:peso.find(".")]
        if peso.isnumeric():
            peso = float(peso_real)

    altura = input('Altura (m): ')
    altura_real = altura
    altura = altura[0:altura.find(".")]
    if altura.isnumeric():
        altura = float(altura_real)

    while type(altura) != float:
        altura = input('Altura inválida, digite novamente!\n'
                       'Altura (m): ')

        altura_real = altura
        altura = altura[0:altura.find(".")]
        if altura.isnumeric():
            altura = float(altura_real)

    imc = peso / (altura ** 2)
    situacao = situacao_por_imc(imc)

    print("-=" * 20)
    print(f'Seu IMC e = {imc}')
    print(f'Situação e {situacao}')
    print("-=" * 20)


def situacao_por_imc(imc):
    if imc < 17:
        situacao = 'muito abaixo do peso'
    elif imc >= 17 and imc < 18.49:
        situacao = 'Abaixo do peso'
    elif imc < 24.99:
        situacao = 'Peso normal'
    elif imc < 29.99:
        situacao = ' Acima do peso'
    elif imc < 34.99:
        situacao = 'Obesodade I'
    elif imc < 39.99:
        situacao = 'Obesodade II'
    elif imc:
        situacao = 'Obesodade III'
    return situacao


principal()
