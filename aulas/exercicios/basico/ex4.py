nome = input('nome: ')
idade = input('idade: ')

if nome and idade:
        print(f'\nSeu nome e {nome}')
        print(f'Seu nome invertido e {nome[::-1]}')
        if ' ' in nome:
            print('Seu nome contem espaços')
        else:
            print('Seu nome nao contem espaços')
        print(f'Seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome e : {nome[0]}')
        print(f'A ultima letra do seu nome e : {nome[-1]}')       
        
else:
    print('Desculpe voce nao forneceu os dados necessarios')
    
print('\n\n')