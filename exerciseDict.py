# Exercício - Sistema de Perguntas e Respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

corretas = 0
total = 0
resposta_correta = ''

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()
    print('Opções:')

    opcoes = pergunta['Opções']
    for alternativa, opcao in enumerate(opcoes):
        print(f'{alternativa+1}) {opcao}')

    print()
    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)-1

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        print('Acertou! 👍')
        corretas += 1
    else:
        print('Errou! ❌')
    
    print()
    total += 1

print(f'Você acertou {corretas} de {total} questões...')