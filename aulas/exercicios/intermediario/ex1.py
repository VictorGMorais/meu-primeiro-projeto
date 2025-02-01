def multiplica(*num):
    res = 1
    for n in num:
        res *= n 
    return res

print(multiplica(45))

def par_ou_impar(*num):
        for n in num:
            if n % 2 == 0:
                print(f'{n} e par')
            else:
                print(f'{n} e impar')
 

par_ou_impar(23)