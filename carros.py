class Carros():
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color
    def __str__(self):
        return " El vehiculo de la marca {}, es de color {}".format(self.marca, self.color)

class Vehiculos(Carros):
    def __init__(self, marca, color, potencia, motor, caja):
        Carros.__init__(self, marca, color)
        self.potecia = potencia
        self.motor = motor
        self.caja = caja

    def __str__(self):
        return Carros.__str__(self) + ", {} CV y motor de {}, el carro tiene una {}".format(self.potecia, self.motor,self.caja)

mi_coche=Carros('honda','azul')
print(mi_coche)
mi_auto=Vehiculos('Mazda','negro','2200','diesel','automatico')
print(mi_auto)
