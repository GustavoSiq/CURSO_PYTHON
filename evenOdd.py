def evenOdd(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par!'
    return f'O número {numero} é ímpar!'

print(evenOdd(int(input('Digite um número: '))))
