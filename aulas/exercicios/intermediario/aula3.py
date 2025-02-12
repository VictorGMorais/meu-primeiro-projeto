#r (leitura)  
#w (escrita | write (para de fato escrever dentro)) 
#a (adiciona ao final sem apagar)
# caminho_arquivo = 'C:\\Users\\SAmsung\\Documents\\Nova pasta teste\\'
# caminho_arquivo = 'aula3.txt'

# # arquivo = open(caminho_arquivo, 'w')  %%% ao invez disso
# # arquivo.close()

# with open(caminho_arquivo, 'w+',encoding='utf-8') as arquivo:
#     arquivo.write('atenção\n')
#     arquivo.write('vai catar coco na praia\n')
#     arquivo.seek(0,0)
#     print(arquivo.read())
    
# with open(caminho_arquivo, 'r') as arquiv:
#     print(arquiv.read())

import json
   
dados = 'dados pessoais victor g. morais.json'   
    
dados_victor = {
    "nome":"victor",
    "sobrenome": "morais",
    "data_nascimento": 
        [{"dia": 30,  
          "mes": 5, 
          "ano": 1999}],
    "idade": 25,
    "sexo": "masculino",
    "pele": "branco",
    "status": "solteiro",
    "pefere": "animes",
    "dev" : True,
    "odio": None
}

with open(dados, 'w' , encoding='utf-8') as file:
    json.dump(dados_victor,file, indent=2)

with open(dados, 'r', encoding='utf8') as file:
    arquivo = json.load(file)
    
for k,v in arquivo.items():
    print(f'{k} {v}')