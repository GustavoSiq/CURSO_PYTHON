cpf = input('Digite seu CPF: ')
# cpf = '451.903.620-86'
cpf = cpf.replace('.',"")
cpf = cpf.replace("-","")
nove_digitos = cpf[:9]
primeiro_contador_regressivo = 10
segundo_contador_regressivo = 11
soma_primeiro_digito = 0
soma_segundo_digito = 0
primeiro_digito = 0
segundo_digito = 0
cpf_gerado = ''

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