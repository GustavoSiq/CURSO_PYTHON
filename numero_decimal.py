"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

# Podemos tratar números decimais de 3 maneiras, são elas:
# - Importando o módulo "decimal";
# - Tratando na hora do print com o ":.2f" por exemplo;
# - Usando a função "round" para aredondar o número.
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))