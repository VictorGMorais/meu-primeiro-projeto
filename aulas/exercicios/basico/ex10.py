import os
lista = []
while True:
    
    menu = input("\n[i] Inserir  \n[a] Apagar  \n[l] Listar  \n[s] sair \nOpçao : ").strip().lower()
    if menu not in 'ials':
        os.system('cls')
        print('\nApenas [i] [a] [l] [s] sao entradas validas!')
        continue
    
    if menu == 'i':
        os.system('cls')
        inserir = input('oque vai inserir na lista: ')
        lista.append(inserir)
    
    elif menu == 'a':
        try:
            os.system('cls')
            print('indices disponiveis!')
            print('IDC     Produto')
            if lista:
                for i, item in enumerate(lista):
                    print(f'{i}       {item}')
            else:
                print('Lista vazia no momento...')
            apagar = input('informe o indice do produto a apagar: ')
            apagar = int(apagar)
            lista.pop(apagar)
        except IndexError:
            print('esse index nao existe na lista.')
    elif menu == 'l':
        os.system('cls')
        if lista:
            print('LISTA DE PRODUTOS ')
            print('IDC     Produtos')
            for i, item in enumerate(lista):
                print(f'{i}       {item}')
            a = input('\n\nsair da lista [press qualquer tecla]')
            os.system('cls')
            
        else:
            print('Lista vazia no momento...')
            
    elif menu == 's':
        break