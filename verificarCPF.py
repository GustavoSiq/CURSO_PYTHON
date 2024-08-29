import re
import sys

entrada = input('Digite seu CPF: ')
# cpf = '451.903.620-86' # CPF gerado pelo gerador de CPF's da 4Devs, expemplo para testes.
# Com o re.sub consigo pegar qualquer coisa que não esteja entre
# 0 e 9 (ou seja, que não seja um número) e substituir.
cpf = re.sub(r'[^0-9]','',entrada)
nove_digitos = cpf[:9]
primeiro_contador_regressivo = 10
segundo_contador_regressivo = 11
soma_primeiro_digito = 0
soma_segundo_digito = 0
primeiro_digito = 0
segundo_digito = 0
cpf_gerado = ''
entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('CPF INVÁLIDO!')
    sys.exit()

for numero in cpf:
    if primeiro_contador_regressivo > 1:
        numero = int(numero)
        soma_primeiro_digito += numero * primeiro_contador_regressivo
        primeiro_contador_regressivo -= 1

    if segundo_contador_regressivo > 1:
        numero = int(numero)
        soma_segundo_digito += numero * segundo_contador_regressivo
        segundo_contador_regressivo -= 1

# Calculo para descobrir se o PRIMEIRO digito está correto:
primeiro_digito = (soma_primeiro_digito * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# Calculo para descobrir se o SEGUNDO digito está correto:
segundo_digito = (soma_segundo_digito * 10) % 11

segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == cpf_gerado:
    print('CPF Válido!')
else:
    print('CPF INVÁLIDO!')