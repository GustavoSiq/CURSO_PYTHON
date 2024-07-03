condicao = True

while condicao:
    nome = input('Qual seu nome? ')
    if nome == 'sair' or nome == 'Sair':
        break
    print(f'Seu nome é {nome}')

print('Acabou!')