"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print('O número digitado é par!')
    else:
        print('o número digitado é ímpar!')    
except:
    print('Você não digitou um número inteiro...')