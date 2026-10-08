from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3

class Planeta:
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, observable, periodo_orbital, periodo_rotacion):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.observable = observable
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    def imprimir(self):
        print("Nombre del planeta =", self.nombre)
        print("Cantidad de satélites =", self.cantidad_satelites)
        print("Masa del planeta =", self.masa)
        print("Volumen del planeta =", self.volumen)
        print("Diámetro del planeta =", self.diametro)
        print("Distancia al Sol =", self.distancia_sol)
        print("Tipo de planeta =", self.tipo.name)
        print("Es observable =", self.observable)
        print("Período orbital =", self.periodo_orbital)
        print("Período de rotación =", self.periodo_rotacion)

    def calcular_densidad(self):
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        limite = 149597870 * 3.4
        return self.distancia_sol > limite

def main():
    p1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000, TipoPlaneta.TERRESTRE, True, 365.25, 1)
    p2 = Planeta("Júpiter", 79, 1.899E27, 1.4313E15, 139820, 750000000, TipoPlaneta.GASEOSO, True, 4332.59, 0.41)

    p1.imprimir()
    print("Densidad del planeta =", p1.calcular_densidad())
    print("Es planeta exterior =", p1.es_planeta_exterior())
    print()

    p2.imprimir()
    print("Densidad del planeta =", p2.calcular_densidad())
    print("Es planeta exterior =", p2.es_planeta_exterior())

if __name__ == "__main__":
    main()
