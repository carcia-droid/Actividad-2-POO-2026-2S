
from enum import Enum

class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2

class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta, porcentaje_interes):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0
        self.porcentaje_interes = porcentaje_interes

    def imprimir(self):
        print("Nombres del titular =", self.nombres_titular)
        print("Apellidos del titular =", self.apellidos_titular)
        print("Número de cuenta =", self.numero_cuenta)
        print("Tipo de cuenta =", self.tipo_cuenta.name)
        print("Saldo =", self.saldo)
        print("Interés mensual =", self.porcentaje_interes, "%")

    def consultar_saldo(self):
        print("El saldo actual es =", self.saldo)
        return self.saldo

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Se han consignado $", valor, ". Nuevo saldo =", self.saldo)
            return True
        print("El valor a consignar debe ser mayor que cero.")
        return False

    def retirar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print("Se han retirado $", valor, ". Nuevo saldo =", self.saldo)
            return True
        print("El retiro debe ser positivo y no superar el saldo actual.")
        return False

    def aplicar_interes(self):
        interes = self.saldo * self.porcentaje_interes / 100
        self.saldo += interes
        print("Interés aplicado =", interes)
        print("Nuevo saldo con interés =", self.saldo)
        return self.saldo

def main():
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS, 1.0)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    cuenta.aplicar_interes()
    cuenta.consultar_saldo()

if __name__ == "__main__":
    main()
```
