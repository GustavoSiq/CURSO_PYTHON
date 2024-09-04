def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result

multiplication = multiply(1,2,3,4,5)
print(multiplication)