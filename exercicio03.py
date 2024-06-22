nome = input('Qual seu nome? ')
contador = 0
novo_nome = ''

while contador < len(nome):
    letra = nome[contador]
    novo_nome += f'{letra}-'
    contador += 1

print(f'-{novo_nome}')