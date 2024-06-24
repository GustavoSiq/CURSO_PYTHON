"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são? ')

try:
    hora = int(hora)
    if hora >= 0 and hora < 12:
        print('Bom dia, usuário! :D')
    elif hora >=12 and hora < 18:
        print('Boa tarde, usuário! :D')
    elif hora >= 18 and hora <= 24:
        print('Boa noite, usuário! :D')
    else:
        print('Você não digitou uma hora existente...')
except:
    print('Por favor, digite apenas números inteiros...')