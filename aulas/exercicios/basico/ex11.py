import sys
from random import randint
cpfs_validos = []
for i in range(100):
    cpf = ''
    for i in range(9):
            cpf += str(randint(0,9))

    cpf_invalido = cpf == cpf[0] * len(cpf)

    if cpf_invalido:
        print('CPF SEQUENCIAL NAO E VALIDO')
        sys.exit()
        
    nove_digi = cpf[:9]
    soma1 = soma2 = 0
    c1 = 10
    c2 = 11
        
    for i in range(9):
        soma1 += int(cpf[i]) * c1
        c1 -= 1
        
    ult_pass = soma1 * 10 % 11
    ult_pass = ult_pass if ult_pass <= 9 else 0
    cpf += str(ult_pass)

    for i in range(10):
        soma2 += int(cpf[i]) * c2
        c2 -= 1
        
    lest_pass = soma2 * 10 % 11
    lest_pass = lest_pass if lest_pass <= 9 else 0
    cpf += str(lest_pass)

    cpf_gerado = f"{nove_digi}{ult_pass}{lest_pass}"

    if cpf_gerado == cpf:
        cpfs_validos.append(cpf)
    else:
        ...
o = 1
for i in cpfs_validos:
    if o <= 5:
        print(i,end=' ')
        if o == 5:
            print('\n')
            o = 1
        else:
            o += 1 
