# 3) Faça um algoritmo que leia um número N e imprima “F1”, “F2” ou “F3”, conforme
# a condição:
# - “F1”, se N <= 10
# - “F2”, se N > 10 e N <= 100
# - “F3”, se n > 100

numero = int(input('Digite o número: '))

if (numero <= 10):
    print('F1')
elif numero <= 100:
    print('F2')
else:
    print('F3')