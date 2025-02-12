class Pessoa:
    from datetime import date
    atributo = date.today().year
    
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        
    def ano_nascimento(self):
        return self.atributo - self.idade
    
v = Pessoa('Victor', 26)
print(v.ano_nascimento())