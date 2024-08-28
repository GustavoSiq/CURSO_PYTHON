cpf = '746.824.890-70'
cpf = cpf.replace('.',"")
cpf = cpf.replace("-","")
contador_regressivo = 10
soma_numeros = 0
primeiro_digito = 0

for numero in cpf:
    if contador_regressivo > 1:
        numero = int(numero)
        soma_numeros += numero * contador_regressivo
        contador_regressivo -= 1

primeiro_digito = (soma_numeros * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

print(primeiro_digito)