# Crie um decorador chamado contador_chamadas que conte quantas vezes uma 
# função foi chamada e exiba esse número a cada execução.
                        # Regras:
# O decorador deve armazenar o número de chamadas da função.
# Cada vez que a função decorada for chamada, deve imprimir 
# "Esta função foi chamada X vezes".
# Teste com uma função qualquer, como diz_ola(), que imprime "Olá, mundo!".

def decorador(funcao):
    cont = 0
    def inicia(*args,**kwargs):
        nonlocal cont
        cont += 1
        print(f'Esta função foi chamada {cont} vezes')
        return funcao(*args,**kwargs)
    return inicia

@decorador     
def diz_ola():
    print('Ola.')
    
@decorador   
def soma(a,b):
    return a + b

print(soma(4,7))
print(soma(8,7))
print(soma(65,78))

diz_ola()
diz_ola()
diz_ola()