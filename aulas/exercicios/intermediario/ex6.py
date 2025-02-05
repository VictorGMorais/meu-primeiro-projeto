#soma_com_cinco = gera_function(soma, 5)
#multiplica_por_dez = gera_funcion(mult, 10)

# def gera_func():
#     def somar(num):
#         return num + 5
#     def mult(num):
#         return num * 10
#     return somar, mult
# s , m = gera_func()

# def somando(a,b=5):
#     return a + b

# print(s(10))
# print(m(10))
# print(somando(10))

#gerador de senha
# import random
# def gerador_senha(tam):
#     def gerar_senha():
#         caracteres= '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%&*_-+=?'
#         senha_gerada = ''
#         for i in range(tam):
#             temp = random.choice(caracteres)
#             senha_gerada += temp
#         return senha_gerada
#     return gerar_senha
        
# senha_pequena = gerador_senha(6)
# senha_grande = gerador_senha(12)

# print(senha_pequena())
# print(senha_grande())
            
def somar(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def cria_funcao(funcao, x):
    def calcula(y):
        return funcao(x,y)
    return calcula

soma = cria_funcao(somar,5)

print(soma(10))