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


##################################################################################

def decoradora(func):
    def inicia(*args,**kwargs):
        for i in args:
            verifica_se_positivo(i)
        for value in kwargs.values():
            verifica_se_positivo(value)
            
        return func(*args,**kwargs)
    return inicia

@decoradora
def somar(a,b):
    return a + b 

def verifica_se_positivo(args):
    if args < 0:
        raise ValueError("o numero tem que ser positivo")

print(somar(5,-6))