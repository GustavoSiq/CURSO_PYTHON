produto = ''
lista = []

while True:
    print('[i]nserir / [l]istar / [a]pagar / [s]air')
    escolha = input('Selecione UMA das opções:').lower()
    
    if escolha == 'i' or escolha == 'inserir':
        produto = input('Produto: ')
        lista.append(produto)
    elif escolha == 'l' or escolha == 'listar':
        for indice, produto in enumerate(lista):
            print(indice, produto)
    elif escolha == 'a' or escolha == 'apagar':
        apagar = int(input('Indice do que quer apagar: '))
        del lista[apagar]
    elif escolha == 's' or escolha == 'sair':
        break
    else:
        print('Opção inválida...')