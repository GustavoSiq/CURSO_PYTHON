moeda = int(input('Quantas vezes você quer que a moeda caia em determinado lado? '))
porcentagem = 100
divisao = 0
soma = 0
nova_soma = 0
soma_final = 0
resultado = 0

while moeda < porcentagem:
    divisao = int(porcentagem/moeda)
    soma = soma_final
    nova_soma = divisao
    soma_final = soma + nova_soma
    porcentagem = porcentagem - moeda

resultado = soma_final/(2**100)

print(f'A probabilidade de você tirar o mesmo lado da moeda {moeda}x é igual a {resultado} ou {resultado:,.33f}%')
