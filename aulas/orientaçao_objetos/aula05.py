class foo:
    def __init__(self):
        self.public = 'Pode acessar de qualquer lugar' #uso global
        self._protected = 'isso e protegido' #uso local dentro da classe ou sub class
        self.__private_ = 'isso e privado' #uso exclusivo local da classe
    
    def metodo_publico(self):
        return 'metodo_publico'
    
    def __private(self):
        return self.__private_
        
ver =  foo()
print(ver.public)
print(ver.metodo_publico())
print(ver._protected)

    
    
    