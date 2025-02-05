# def criar_texto(saudacao, nome):
#         def saudar():
#                 return f'{saudacao},{nome}'
#         return saudar

# teste1 = criar_texto('vai te foder','seu merda')

# print(teste1())

# livro = {
#         'nome': 'maiguel',
#         'pagina' : 123,
#         'linha' : 67,
        
# }

# livro.update(coluna=3,cidade='montevideu')
# print(livro)

# def mynput(msm=''):
#         escreva = input(msm)
#         if escreva.isdigit():
#             return int(escreva)  
#         try:
#             escrev_float = float(escreva)
#             return escrev_float
    
#         except ValueError:
#             return escreva
        
# print(type(mynput('digite int: ')))
# print(type(mynput('digite float')))
# print(type(mynput('digite str')))


# s = set()
# s.add('victor')
# s.add(1)
# s.add(4)
# s.add(7)
# s.update(('ola',))
# # s.clear()
# s.discard(4)
# print(s)

# s1 = set("victor")
# s2 = set("morais")
# s3 = s2 ^ s1
# print(s3)
# novo_nome = []
# for i in s3:
#     novo_nome.append(i)

# from random import randint
# lista = [randint(1,9) for num in range(6)]

# print(lista)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for linha in matrix:
#     for coluna in linha:
#         print(coluna,end=' ')
#     print()

# nome = 'Victor Gomes Morais'
# n_letras = 1
# nome_formatado = '*'.join([nome[i:i+ n_letras] for i in range(0,len(nome),n_letras)]) 

# print(nome_formatado)

# nomes = ['victor','maya','debora','katia','leonardo','thomas']

# # novo_nome = [i[:-1] + i[-1].upper() for i in nomes]
# print(nomes[0][:-1])

# pessoa = [
#     {'nome1', 'maya'},
#     {'nome2', 'roberth'},
#     {'nome3', 'sahra'},
#     {'nome4', 'camila'},
#     {'nome5', 'miguel'},
#     {'nome6', 'roger'},
# ]
    
# dc = {
#       k: v 
#       for k, v in pessoa
#       }

# print(dc)
# dicionario = {
#     k.upper():v if isinstance(k , str) else k for k , v in pessoa.items() if k == 'peso' 
# }

# print(dicionario)
# print(type(pessoa))

# for linha in pessoa:
#     for k,v in linha.items():
#         print(f'{k:.<8}{v:<10}',end=' ')
#     print()

# s2 = {2 ** i for i in range(10)}

# print(s2)

# def gen_sequenc(init = 0, end = 10):
#     for i in range(init,end):
#         yield i
        
# for entrada in gen_sequenc():
#         print(entrada)

# import sys

# print(sys.platform)

# import teste
# print('essa pasta se chama: ',__name__)

    #Clousure
# def gerador_contador():
#     num = 0
#     def contador():
#         nonlocal num 
#         num += 1
#         return num
#     return contador

# c = gerador_contador()
# d = gerador_contador()
# print()


# def fora():
#     a = 1
#     def dentro():
#         # nonlocal a
#         a = a + 5
#         return a
#     return dentro
    
# dentro = fora()
# print(dentro())

# def exibir(**kwargs):
#     print(kwargs)  # Apenas para entender o que chega
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")

# exibir(nome="Ana", idade=25, cidade="São Paulo")

# def somar(*args):
#     print(args)  # Apenas para entender o que chega
#     return sum(args)

# print(somar(1, 2, 3))  # (1, 2, 3)
# print(somar(10, 20))    # (10, 20)

def cria_funçao(func):
    def checa_funçao(*args,**kwargs):
        for arg in args:
            e_string(arg)
        rtn = func(*args,**kwargs)
        #
        return rtn
    return checa_funçao

def e_string(arg):
    if not isinstance(arg,str):
        raise TypeError ("a entrada deve ser uma string")   

def invert_string(msm):
    return msm[::-1]    

checando_arg = cria_funçao(invert_string)
s = checando_arg(123)
print(s)