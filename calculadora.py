continuar = 'sim'

while continuar == 'sim' or continuar == 'yes' or continuar == 's' or continuar == 'y':
    numero1 = input('Digite o primeiro número: ')
    operador = input('Diga qual tipo de operação você quer fazer("+", "-", "*" ou "/"): ').lower()
    numero2 = input('Digite o segundo número: ')
    
    numeros_validos = None

    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+' or operador == 'adição' or operador == 'soma' or operador == 'mais':
        resultado = float(numero1) + float(numero2)
        print(f'{numero1} + {numero2} = {resultado}')
    elif operador == '-' or operador == 'subtração' or operador == 'menos':
        resultado = float(numero1) - float(numero2)
        print(f'{numero1} - {numero2} = {resultado}')
    elif operador == '*' or operador == 'x' or operador == 'multiplicação':
        resultado = float(numero1) * float(numero2)
        print(f'{numero1} x {numero2} = {resultado}')
    elif operador == '/' or operador == 'divisão':
        resultado = float(numero1) / float(numero2)
        print(f'{numero1} ÷ {numero2} = {resultado}')
    else:
        print('Você não digitou um operador válido...')

    print('----------------------------------------------------')
    continuar = input('Deseja efetuar outro calculo? ').lower()

print('Até a próxima!')