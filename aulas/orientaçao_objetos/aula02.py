class Camera:
    def __init__(self,nome,filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja esta filmando')
            return
        
        print(f'{self.nome} esta filmando')
        self.filmando = True
    
    def fotogradar(self):
        if self.filmando:
            print(f'{self.nome} nao pode fotografar enquanto filma')
            return 
        
        print(f'{self.nome} começou a fotografar')
        
    def parar_filmagem(self):
        print(f'{self.nome} esta parando a filmagem')
        self.filmando = False
        
        
c1 = Camera('paramont')
c1.filmar()
c1.fotogradar()
c1.parar_filmagem()
c1.fotogradar()
c1.filmar()
c1.fotogradar()
c1.filmar()