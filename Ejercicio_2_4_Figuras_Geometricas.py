
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        lados = [self.base, self.altura, self.calcular_hipotenusa()]
        if lados[0] == lados[1] == lados[2]:
            return "Equilátero"
        elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
            return "Isósceles"
        return "Escaleno"

class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def calcular_area(self):
        return self.diagonal_mayor * self.diagonal_menor / 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

class PruebaFiguras:
    @staticmethod
    def main():
        circulo = Circulo(2)
        rectangulo = Rectangulo(1, 2)
        cuadrado = Cuadrado(3)
        triangulo = TrianguloRectangulo(3, 5)
        rombo = Rombo(8, 6, 5)
        trapecio = Trapecio(8, 4, 3, 3, 5)

        figuras = [
            ("Círculo", circulo),
            ("Rectángulo", rectangulo),
            ("Cuadrado", cuadrado),
            ("Triángulo rectángulo", triangulo),
            ("Rombo", rombo),
            ("Trapecio", trapecio)
        ]

        for nombre, figura in figuras:
            print(nombre)
            print("Área =", figura.calcular_area())
            print("Perímetro =", figura.calcular_perimetro())
            if isinstance(figura, TrianguloRectangulo):
                print("Hipotenusa =", figura.calcular_hipotenusa())
                print("Tipo =", figura.determinar_tipo_triangulo())
            print()

if __name__ == "__main__":
    PruebaFiguras.main()
```
