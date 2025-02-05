def decorador(funcao):
    print('recebendo')
    def verifica(*args,**kwargs):
        print('recebi')
        for arg in args:
            print('analizando')
            is_int(arg)
        resultado = funcao(*args,**kwargs)
        print('tudo ok')
        return resultado
    return verifica
            
def is_int(args):
    if not isinstance(args, int):
        raise ValueError ("Entrada invalida, informe numeros")
    elif args == 0:
        raise ZeroDivisionError ("Zero nao e permitico em divisoes")

@decorador  
def multiplica(a,b):
    res = a * b
    return res


final = multiplica(8,4)
print(final)