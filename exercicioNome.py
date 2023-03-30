nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    if ' ' in nome:
        print(f'O seu nome contém espaço.')
    else:
        print(f'Seu nome não contém espaço.')
    if ' ' not in nome:
        print(f'Seu nome contém {len(nome)} letras.')
    else:
        print(f'Seu nome contém {len(nome)-1} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')   