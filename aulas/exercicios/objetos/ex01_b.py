import json
from ex01_a import CAMINHO_DADOS, Pessoa

try:
    with open(CAMINHO_DADOS, 'r', encoding='utf8') as file:
        dado = json.load(file)
        p1 = Pessoa(**dado[0])
        p2 = Pessoa(**dado[1])
        p3 = Pessoa(**dado[2])
        
        print(p1.nome, p1.idade, p1.peso)
        print(p2.nome, p2.idade, p2.peso)
        print(p3.nome, p3.idade, p3.peso)
except FileNotFoundError:
    print('o arquivo nao existe!')