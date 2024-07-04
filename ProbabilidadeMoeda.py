"""Considerando cara a letra C e coroa a letra K, teríamos o espaço amostral de CCC...C (100 vezes), variando até (KKK...K) 100 vezes), 
ou se fosse fazer a analogia com bits: de 000...0 (100 zeros) a 111...1 (100 uns).
Sendo assim, no total (cara ou coroa) temos 2100 possibilidades. Agora vamos discutir as 8 repetições de coroas:

1) Apenas 8 coroas: Dividindo 100 por 8 dá 12,5, então é póssível obter até 12 repetições de 8 coroas
2) 2 repetições de 8 coroas: 100 - 8 (tira a primeira sequencia de 8 coroas) = 92, dividindo por 8 dá 11,5 possibilidades, 
ou seja, até 11 repetições de duas sequências de 8 coroas seguidas.
3) Seguindo o raciocínio -> 3 sequencias de 8 coroas: 84/8 = 10,5 -> 10 repetições

4) 76/8 = 9,5 -> 9
5) 68/8 -> 8
6) 60/8 -> 7
7) 52/8  -> 6
8) 44/8 -> 5
9) 36/8 -> 4
10) 28/8 -> 3
11) 20/8 -> 2
12) 12/8 -> 1

Agora somamos estas possibilidades e dividimos pelo total: p = (12+11+...+1)/2**100 = 78/2**100 = 6,1531x10-29(6.1531*10**-29)"""

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
