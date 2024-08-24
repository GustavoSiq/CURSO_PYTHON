import os

produto = ''
lista = []

while True:
    print('[i]nserir / [l]istar / [a]pagar / [s]air')
    escolha = input('Selecione UMA das opções:').lower()
    
    if escolha == 'i' or escolha == 'inserir':
        os.system('cls')
        produto = input('Produto: ')
        lista.append(produto)
    elif escolha == 'l' or escolha == 'listar':
        os.system('cls')
        if len(lista) == 0:
            print('Você ainda não adicionou produtos...')
        for indice, produto in enumerate(lista):
            print(indice, produto)
    elif escolha == 'a' or escolha == 'apagar':
        try:
            apagar = int(input('Indice do produto que quer apagar: '))
            del lista[apagar]
        except IndexError:
            print('Esse índice não foi encontrado...')
        except ValueError:
            print('Digite um número inteiro...')
    elif escolha == 's' or escolha == 'sair':
        break
    else:
        print('Opção inválida...')