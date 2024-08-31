import random

nove_digitos = ''
primeiro_contador_regressivo = 10
segundo_contador_regressivo = 11
soma_primeiro_digito = 0
soma_segundo_digito = 0

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

for numero_primeiro_digito in nove_digitos:
    if primeiro_contador_regressivo > 1:
        soma_primeiro_digito += int(numero_primeiro_digito) * primeiro_contador_regressivo
        primeiro_contador_regressivo -= 1

# Calculo para descobrir se o PRIMEIRO digito está correto:
primeiro_digito = (soma_primeiro_digito * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos = nove_digitos + str(primeiro_digito)

for numero_segundo_digito in dez_digitos:
    if segundo_contador_regressivo > 1:
        soma_segundo_digito += int(numero_segundo_digito) * segundo_contador_regressivo
        segundo_contador_regressivo -= 1

# Calculo para descobrir se o SEGUNDO digito está correto:
segundo_digito = (soma_segundo_digito * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(cpf_gerado)