class Auto:
    def __init__(self, marca, modelo, a�o,velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.a�o = a�o
        self.velocidad_maxima = velocidad_maxima

    def presentarse(self):
        return f"Soy un {self.marca} {self.modelo} del a�o {self.a�o} con una velocidad maxima {self.velocidad_maxima}."


class Sedan(Auto):
    def __init__(self, marca, modelo, a�o,velocidad_maxima, puertas):
        super().__init__(marca, modelo, a�o, velocidad_maxima)
        self.velocidad_maxima = velocidad_maxima
        self.puertas = puertas

    def tipo(self):
        return "Soy un sed�n."


class SUV(Auto):
    def __init__(self, marca, modelo, a�o, velocidad_maxima, traccion):
        super().__init__(marca, modelo, a�o, velocidad_maxima)
        self.velocidad_maxima = velocidad_maxima
        self.traccion = traccion

    def tipo(self):
        return "Soy un SUV."


class Deportivo(Auto):
    def __init__(self, marca, modelo, a�o, velocidad_maxima):
        super().__init__(marca, modelo, a�o , velocidad_maxima)
        self.velocidad_maxima = velocidad_maxima

    def tipo(self):
        return "Soy un deportivo."


# Ejemplo de uso
sedan = Sedan("Toyota", "Corolla", 2022, 4)
print(sedan.presentarse())  # Salida: Soy un Toyota Corolla del a�o 2022.
print(sedan.tipo())          # Salida: Soy un sed�n.

suv = SUV("Ford", "Explorer", 2023, "4x4")
print(suv.presentarse())  # Salida: Soy un Ford Explorer del a�o 2023.
print(suv.tipo())         # Salida: Soy un SUV.

deportivo = Deportivo("Ferrari", "488 GTB", 2024, 330)
print(deportivo.presentarse())    # Salida: Soy un Ferrari 488 GTB del a�o 2024.
print(deportivo.tipo())           # Salida: Soy un deportivo.