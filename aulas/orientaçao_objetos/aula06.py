class Carrinho:
    def __init__(self):
        self._produtos = []
        
    def total(self):
        return sum([p.preco for p in self._produtos])
        
    def inserir_produto(self,*produto):
        self._produtos.extend(produto)
        # for prod in produto:
        #     self._produtos.append(prod)
        
    def listar(self ):
        print()
        for prod in self._produtos:
            print(f'{prod.nome:.<10}{prod.preco:.>6}')
        print()
        
class Produto:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco
    
carrinho_compras = Carrinho()
p1 = Produto('vinho',45.99)
p2 = Produto('caneta', 1.25)
p3 = Produto('arroz', 33.99)
p4 = Produto('banana', 12.45)
p5 = Produto('alcool', 5.99)

carrinho_compras.inserir_produto(p1,p2,p3,p4,p5)
carrinho_compras.listar()
print(carrinho_compras.total())
