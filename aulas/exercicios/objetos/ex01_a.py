import json

class Pessoa:
    def __init__(self,nome,idade,peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        
a = Pessoa('victor', 26, 65.89)
b = Pessoa('carol', 23, 34)
c = Pessoa('Maya', 12, 23)

dados = [a.__dict__,b.__dict__,c.__dict__]

CAMINHO_DADOS = 'ex01.json'

with open(CAMINHO_DADOS, 'w', encoding='utf8') as file:
    json.dump(dados, file, indent=2,ensure_ascii=False)
    