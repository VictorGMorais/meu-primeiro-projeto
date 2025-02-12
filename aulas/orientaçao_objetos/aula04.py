#property em python funciona como um atributo mas e feita como um metodo ("funçao")
#entao no codigo ao inves de chamar caneta.cor_tinta, se chama a property apenas com
#caneta.cor, e ultil quando se quer mudar o nome mas tem de manter o antigo pois esta
#em uso e quebraria o codigo se trocasse de forma abrupta.
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        
    @property    
    def cor(self):
        return self.cor_tinta
    
caneta = Caneta('Vermelha')
print(caneta.cor)


class Pessoa:
    def __init__(self, idade):
        self.idade = idade
    @property
    def idade(self):
        print('estoi aqui veiote')
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        print('estoi aqui')
        if nova_idade < 0:
            raise ValueError ('idade negativa nao e valido!')
        self._idade = nova_idade
        
p = Pessoa(25)
print(p.idade)  # Acesso via getter
p.idade = 30       # Modificação via setter
print(p.idade)  # Saída: 30

# pessoa = Pessoa(26)    
# pessoa.get_idade = 12
# print(pessoa.get_idade)