def soma_digitos(n):
    if n < 10:
        return n
    return soma_digitos(n // 10) + (n % 10)

print(soma_digitos(1234))

