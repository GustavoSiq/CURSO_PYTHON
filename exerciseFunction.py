def multiplicar(numero):
    def multiplicador(multiplicador):
        return multiplicador * numero
    return multiplicador

contador = 1
ser_multiplicado = int(input('Digite o número: '))
multiplicador = int(input('Digite o multiplicador: '))

while contador <= multiplicador:
    resultado = multiplicar(contador)
    print(f'{ser_multiplicado} x {contador} = ', resultado(ser_multiplicado))
    contador += 1