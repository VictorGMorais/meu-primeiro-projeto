nome = 'Victor Gomes Morais'
cont = 0
novo_nome = ''
s = '='

while cont < len(nome):
    novo_nome += f'{s}{nome[cont]}'
    cont += 1
novo_nome += s
    
print(novo_nome)