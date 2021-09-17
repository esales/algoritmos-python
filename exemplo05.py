numero = 0
soma = 0
media = 0
qtdNumeros = 0

numero = int(input('Digite o numero: '))

while numero != 9999:
    qtdNumeros += 1
    soma += numero

    numero = int(input('Digite o numero: '))

media = soma/qtdNumeros
print('\n')
print('Soma: ', soma)
print('Média: ', media)