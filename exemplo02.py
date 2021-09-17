# Faça um algoritmo que leia dois números A e B e imprima o maior deles.

numeroA = int(input('Primeiro número: '))
numeroB = int(input('Segundo número: '))

if (numeroA > numeroB):
    print('Maior: ', numeroA)
elif numeroB > numeroA:
    print('Maior: ', numeroB)
else:
    print('Iguais')