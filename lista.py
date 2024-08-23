# append - Adiciona um item ao final
# insert - Adiciona um item no índice escolhido
# pop - Remove do final ou do índice escolhido
# del - apaga um índice
# clear - limpa a lista
# extend - estende a lista
# + - concatena listas

lista = [10, 20, 30, 40]
lista.append(50)
lista.append('60')
# Se o pop ficar vazio, ele remove o último item da lista.
item_removido = lista.pop(2)
lista.append(70)
del lista[-1]
# Primeiro insere a posição na lista e depois o que será inserido.
lista.insert(0, 'Gustavo')
# lista.clear()
print(lista, 'Item removido: ', item_removido)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
# Aqui houve a cocatenação, a lista_a uniu com a lista_b para formar a lista_c
lista_c = lista_a + lista_b
print(lista_a)
print(lista_c)
# No extend ele autera a lista_a, deixando todo o resto como estava.
lista_a.extend(lista_b)
print(lista_a)
print(lista_b)
print(lista_c)