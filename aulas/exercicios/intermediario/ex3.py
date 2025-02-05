#declarando as perguntas / opçoes / respostas
pergunta_n1 = 'QUAL A CAPITAL DO BRASIL ? '
pergunta_n2 = 'QUEM FOI O PRIMEIRO ASTRONAUTA A PISAR NA LUA ? '
pergunta_n3 = 'QUANTOS PAISES FAZEM PARTE DA UNIAO EUROPEIA? '

opcoes = [['Brasília' , 'São Paulo' , 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'],
          ['Buzz Aldrin' , 'Yuri Gagarin', 'Michael Collins' , 'Neil Armstrong' , 'Alan Shepard'],
          ['19 Paises' ,'28 Paises' ,'27 Paises' ,'23 Paises' ,'21 Paises']]

respostas = [1 , 4 , 3]

def linha():       #apenas imprime uma linha
    print('-'*35)

#aqui vai imprimir a pergunta e as opcoes correspondentes
def menu_opcao(pergunta, opcoes):
    linha()
    print(pergunta)
    linha()
    for n,i in enumerate(opcoes,1):
        print(f'{n}) {i}')
    print()

#aqui ele coleta a escolha do usuario, limitando apenas a numeros de 1 a 5
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

#aqui verificar se a escolha do usuario corresponde com a resposta a pergunta           
def verificaçao(escolha,num_pergunta):
    
    #essa variavel foi feita para o print nao ficar muito extenso 
    alternativa_certa = opcoes[num_pergunta][respostas[num_pergunta]-1]
    
    if escolha == respostas[num_pergunta]:
        print('Acertou! 👏')
        linha()
        print('\n')
        return 1  #retorna 1 ou 0, e um contador para imprimir no final acertos e erros
    else:
        print(f'Errou! 😒 o certo era {respostas[num_pergunta]} : {alternativa_certa}')
        linha()
        print('\n')
        return 0

#funçao principal, cria um loop para chamar as demais funçoes usando o iterador do loop para puxar
#corretamente, perguntas , opçoes e verificaçao correspondentes   
def main():
    pergunta = [pergunta_n1,pergunta_n2,pergunta_n3]
    soma = 0 #soma o retorno 1 ou 0 da verificaçao
    for i in range(3):
        
        menu_opcao(pergunta[i],opcoes[i])          
        escolha = menu_escolha()
        pontuacao = verificaçao(escolha,i)
        soma += pontuacao
              
    linha()
    print(f'VOCE ACERTOU {soma} PERGUNTA(S) E ERROU {3-soma} VEZ(ES)')
    linha()    

#aqui chama a funçao principal              
resultado = main()

#FIM da versao 0.0.1 (deixe aqui dicas e sejustao de melhorias ^^ --> )


