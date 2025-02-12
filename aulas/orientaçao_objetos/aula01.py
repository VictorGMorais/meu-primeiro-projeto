class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def comendo(self, alimento):
        return f'o {self.nome} esta comendo {alimento}'
    
    def executar(self,*args,**kwargs):
        return self.comendo(*args,**kwargs)
    

leao = Animal('tigre')
print(leao.executar('carne'))



