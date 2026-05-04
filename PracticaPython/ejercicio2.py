#Cuenta Bancaria: 
# Crear clase CuentaBancaria con atributos titular (Persona), saldo (privado) y número_cuenta. 
# Métodos: depositar(monto), retirar(monto) (validar saldo) y mostrar_saldo().



class CuentaBancaria:
    def __init__(self,titular, numero_cuenta, saldo_inicial=0) -> None:
        self.titular=titular #Objeto Persona (agregación)
        self.numero_cuenta = numero_cuenta
        self.__saldo=saldo_inicial #Atributo privado
    def depositar(self,monto):
        if monto>0:
            self.__saldo +=monto
            print(f'El monto actual es: {self.__saldo}$.')
            return True
        else:
            print(f'El monto debe ser positivo.')
            return False
    def retirar(self,monto):
        if monto <= 0:
            print(f'El monto debe ser positivo.')
            return False
        elif monto > self.__saldo:
            print(f'Saldo insuficiente.')
            return False        
        else:
            self.__saldo -=monto
            print(f'El monto actual es: {self.__saldo}$.')
            return True
    
    def mostrar_saldo(self):
        print(f"Saldo actual:${self.__saldo:.2f}")
        return self.__saldo
    
    #Getterparasaldo(buenapráctica)
    def get_saldo(self):
        return self.__saldo

from ejercicio1 import Persona  # Importar clase del ejercicio anterior

titular = Persona("Carlos Ruiz", 30, "11223344B")
cuenta = CuentaBancaria(titular, "001-123456", 1000)

print(f"Titular: {cuenta.titular.nombre}")
cuenta.mostrar_saldo()

cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(2000)  # Debe fallar
cuenta.mostrar_saldo()        
        

        