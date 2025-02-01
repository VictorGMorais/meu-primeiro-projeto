pergunta_n1 = 'capital do brazil? '
pergunta_n2 = 'quem foi o primeiro astronalta a pisar na lua? '
pergunta_n3 = 'quantos paises tem na asia? '

opcoes = [('Brasília' , 'São Paulo' , 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'),
             ( 'Buzz Aldrin' , 'Yuri Gagarin', 'Michael Collins' , 'Neil Armstrong' , 'Alan Shepard'),
             (35 , 54 , 49 , 42 , 60)]

respostas = [1 , 4 , 3]


def linha():
    print('-'*35)
    
def menu_opcao(pergunta, resposta):
    linha()
    print(pergunta)
    linha()
    for n,i in enumerate(resposta,1):
        print(f'{n}) {i}')
    print()

def menu_escolha(msm='escolha uma das alternativas [1...5]: '):
    while True:
        try:
            num = int(input(msm))
            if num >= 1 and num <= 5:
                return num
        except ValueError:
            print('Digite numeros inteiros!')
        except Exception:
            print('Erro desconhecido')
            
def verificaçao(escolha,num_pergunta):
    alternativa_certa = opcoes[num_pergunta][respostas[num_pergunta]-1]
    if escolha == respostas[num_pergunta]:
        print('Acertou!')
        linha()
        print('\n')
        return 1
    else:
        print(f'Errou! o certo era {respostas[num_pergunta]} : {alternativa_certa}')
        linha()
        print('\n')
        return 0
    
def main():
    soma = 0
    menu_opcao(pergunta_n1,opcoes[0])          
    escolha = menu_escolha()
    pontuacao = verificaçao(escolha,0)
    soma += pontuacao
    
    menu_opcao(pergunta_n2,opcoes[1])
    escolha = menu_escolha()
    pontuacao = verificaçao(escolha,1)
    soma += pontuacao
    
    menu_opcao(pergunta_n3,opcoes[2])
    escolha = menu_escolha()
    pontuacao = verificaçao(escolha,2)
    soma += pontuacao
    return soma
    
resultado = main()
linha()
print(f'VOCE ACERTOU {resultado} PERGUNTA E ERROU {3-resultado} VEZES')
linha()



