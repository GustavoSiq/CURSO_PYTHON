import os


palavra = 'Gustavo'.lower()
letras_corretas = ''
repeticoes = 0
  
while True:
    letra = input('Digite uma letra: ').lower()

    if letra.isnumeric() == True or len(letra) > 1 or len(letra) < 1:
        print('SOMENTE UMA LETRA... ')
        continue

    repeticoes += 1
    
    if letra in palavra:
        letras_corretas += letra
    
    palavra_descoberta = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_descoberta += letra
        else:
            palavra_descoberta += '*'

    print(f'Palavra formada: {palavra_descoberta}')

    if palavra_descoberta == palavra:
        apresentacao = palavra.upper()
        os.system('cls')
        print(f'PARABÉNS, VOCÊ CONSEGUIU DESCOBRIR A PALAVRA DO DIA: ***** {apresentacao} *****')
        break

print(f'Você conseguiu descobrir em {repeticoes} tentativas!')