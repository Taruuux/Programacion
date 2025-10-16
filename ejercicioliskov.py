

class vehiculo:
    def __init__(self, velocidad = 0):
        self.velocidad = velocidad
        

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"velocidad: {self.velocidad} km/h")
    
    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad <= 0:
            self.velocidad = 0
        print(f"velocidad: {self.velocidad} km/h")
    
class coche(vehiculo):
    def acelerar(self, incremento):
        print("El coche acelera")
        incremento += 2
        super().acelerar(incremento)
    
    def frenar(self, decremento):
        print("El coche frena")
        decremento += 2
        super().frenar(decremento)
        
class moto(vehiculo):
    def acelerar(self, incremento):
        print("La moto acelera")
        incremento += 3
        super().acelerar(incremento)

    def frenar(self, decremento):
        print("La moto frena")
        decremento += 1
        super().frenar(decremento)   

class camion(vehiculo):
    def acelerar(self, incremento):
        print("El camion acelera")
        super().acelerar(incremento)

    def frenar(self, decremento):
        print("El camion frena")
        decremento += 2
        super().frenar(decremento)    


def test_vehiculo(vehiculo):
    vehiculo.acelerar(2)
    vehiculo.frenar(1)

vehiculo = vehiculo()
coche = coche()
moto = moto()
camion = camion()
test_vehiculo(coche)
test_vehiculo(moto)
test_vehiculo(camion)