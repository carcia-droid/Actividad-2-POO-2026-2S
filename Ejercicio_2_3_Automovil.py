
from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5

class TipoAutomovil(Enum):
    CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6

class TipoColor(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8

class Automovil:
    VALOR_MULTA = 100000

    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, numero_puertas, cantidad_asientos, velocidad_maxima, color, automatico):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0
        self.automatico = automatico
        self.cantidad_multas = 0

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_motor(self):
        return self.motor

    def set_motor(self, motor):
        self.motor = motor

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def get_tipo_automovil(self):
        return self.tipo_automovil

    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def get_numero_puertas(self):
        return self.numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def get_cantidad_asientos(self):
        return self.cantidad_asientos

    def set_cantidad_asientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    def set_velocidad_actual(self, velocidad_actual):
        if 0 <= velocidad_actual <= self.velocidad_maxima:
            self.velocidad_actual = velocidad_actual
        else:
            print("La velocidad debe estar entre 0 y la velocidad máxima.")

    def get_automatico(self):
        return self.automatico

    def set_automatico(self, automatico):
        self.automatico = automatico

    def acelerar(self, incremento):
        if incremento < 0:
            print("El incremento no puede ser negativo.")
        elif self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
        else:
            self.cantidad_multas += 1
            print("No se puede superar la velocidad máxima. Se genera una multa.")

    def desacelerar(self, decremento):
        if decremento < 0:
            print("El decremento no puede ser negativo.")
        elif self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            print("No se puede calcular el tiempo con velocidad cero.")
            return None
        return distancia / self.velocidad_actual

    def tiene_multas(self):
        return self.cantidad_multas > 0

    def calcular_valor_total_multas(self):
        return self.cantidad_multas * self.VALOR_MULTA

    def imprimir(self):
        print("Marca =", self.marca)
        print("Modelo =", self.modelo)
        print("Motor =", self.motor, "litros")
        print("Tipo de combustible =", self.tipo_combustible.name)
        print("Tipo de automóvil =", self.tipo_automovil.name)
        print("Número de puertas =", self.numero_puertas)
        print("Cantidad de asientos =", self.cantidad_asientos)
        print("Velocidad máxima =", self.velocidad_maxima, "km/h")
        print("Color =", self.color.name)
        print("Velocidad actual =", self.velocidad_actual, "km/h")
        print("¿Es automático? =", self.automatico)
        print("Cantidad de multas =", self.cantidad_multas)
        print("Valor total de multas =", self.calcular_valor_total_multas())

def main():
    auto1 = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL,
                      TipoAutomovil.EJECUTIVO, 5, 6, 250,
                      TipoColor.NEGRO, False)

    auto1.imprimir()
    auto1.set_velocidad_actual(100)
    print("Velocidad actual =", auto1.get_velocidad_actual(), "km/h")

    auto1.acelerar(20)
    print("Velocidad actual =", auto1.get_velocidad_actual(), "km/h")

    auto1.desacelerar(50)
    print("Velocidad actual =", auto1.get_velocidad_actual(), "km/h")

    auto1.frenar()
    print("Velocidad actual =", auto1.get_velocidad_actual(), "km/h")

    auto1.acelerar(260)
    print("¿Tiene multas? =", auto1.tiene_multas())
    print("Valor total de multas =", auto1.calcular_valor_total_multas())

if __name__ == "__main__":
    main()
```
