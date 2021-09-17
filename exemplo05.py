# Faça um algoritmo que leia um conjunto de números (X) e imprima sua soma
# (Soma) e sua média (Media). Admita que o valor 9999 é utilizado como sentinela
# para fim de leitura.
# Ex.: 1, 2, 3 => Soma=6 Media=2

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