# class Carro:
#     def __init__(self,nome):
#         self.nome_carro = nome
#         self.motor = None
#         self.fabricante = None
          
#     def recebe_motor(self, motor):
#         self.motor = motor
        
#     def recebe_fabricante(self,fabricante):
#         self.fabricante = fabricante
  
#     def mostar_dados_carro(self):
#         print(f'{self.nome_carro} {self.fabricante.nome_fabricante} {self.motor.nome_motor} ')
        
# class Motor:
#     def __init__(self,nome):
#         self.nome_motor = nome
        
# class Fabricante:
#     def __init__(self,nome):
#         self.nome_fabricante = nome

# hb20 = Carro('HB20')
# motor1 = Motor('1.0')
# motor2 = Motor('2.0')
# motor3 = Motor('3.0')
# fabricante = Fabricante('Hyundai')
# hb20.recebe_motor(motor1)
# hb20.recebe_fabricante(fabricante)

# fusca = Carro('fusca')
# fusca.recebe_motor(motor3)
# fusca.recebe_fabricante(fabricante)
# hb20.mostar_dados_carro()
# fusca.mostar_dados_carro()


class Car:
    def __init__(self,name):
        self.name = name
        self._engine = None
        self._manufacturer = None
        
    @property    
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self,value):
        self._engine = value
        
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value):
        self._manufacturer = value

class Engine:
    def __init__(self,name):
        self.name = name

class Manufacturer:
    def __init__(self,name):
        self.name = name
        
gol = Car('Gol')
motor_1_0 = Engine('1.0')
ford = Manufacturer('Ford')

gol.manufacturer = ford
gol.engine = motor_1_0
print(gol.name, gol.manufacturer.name, gol.engine.name)

