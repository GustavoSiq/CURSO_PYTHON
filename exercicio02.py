primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro número "{primeiro_valor}" é maior que o segundo número "{segundo_valor}"')
elif segundo_valor > primeiro_valor:
    print(f'O segundo número "{segundo_valor}" é maior que o primeiro número "{primeiro_valor}"')
else:
    print(f'Os dois números são iguais!!')