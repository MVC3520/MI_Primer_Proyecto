'''EJERCICIO 13: Crea un sistema de vehículos usando herencia donde diferentes tipos de vehículos 
calculen su consumo de combustible de manera distinta. Implementa una clase base Vehiculo con atributos 
marca, modelo y año, y un método calcular_consumo(kilometros) que devuelva el consumo genérico. Luego 
crea las clases Auto, Moto y Camion que hereden de Vehiculo y sobrescriban el método calcular_consumo() 
con sus fórmulas específicas: Auto 12 km/l, Moto 25 km/l, Camión 5 km/l. Finalmente, demuestra el 
polimorfismo creando una lista con diferentes vehículos y calculando el consumo total para un viaje de 
100 km.'''

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def calcular_consumo(self, kilometros):
        """Consumo base: 10 km por litro"""
        return kilometros / 10
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Auto(Vehiculo):
    def calcular_consumo(self, kilometros):
        """Auto: 12 km por litro"""
        return kilometros / 12

class Moto(Vehiculo):
    def calcular_consumo(self, kilometros):
        """Moto: 25 km por litro"""
        return kilometros / 25

class Camion(Vehiculo):
    def calcular_consumo(self, kilometros):
        """Camión: 5 km por litro"""
        return kilometros / 5

# Uso del sistema
if __name__ == "__main__":
    print("=== SISTEMA DE CONSUMO DE VEHÍCULOS ===\n")
    
    # Crear vehículos de diferentes tipos
    vehiculos = [
        Auto("Toyota", "Corolla", 2020),
        Moto("Honda", "CBR", 2021),
        Camion("Mercedes", "Actros", 2019),
        Auto("Ford", "Focus", 2018)
    ]
    
    # Mostrar información básica
    print("Vehículos en la flota:")
    for i, v in enumerate(vehiculos, 1):
        print(f"{i}. {v}")
    
    # Calcular consumo para un viaje de 100 km
    print("\nConsumo para un viaje de 100 km:")
    total_litros = 0
    
    for vehiculo in vehiculos:
        litros = vehiculo.calcular_consumo(100)
        total_litros += litros
        # Determinar tipo de vehículo
        tipo = vehiculo.__class__.__name__
        print(f"  {tipo} {vehiculo.marca}: {litros:.1f} litros")
    
    print(f"\nConsumo total: {total_litros:.1f} litros")
    
    # Demostración adicional de polimorfismo
    print("\n=== DEMOSTRACIÓN DE POLIMORFISMO ===")
    
    # Lista de diferentes distancias
    distancias = [50, 100, 200]
    
    for distancia in distancias:
        print(f"\nPara {distancia} km:")
        for vehiculo in vehiculos:
            consumo = vehiculo.calcular_consumo(distancia)
            print(f"  {vehiculo.marca}: {consumo:.1f}L", end=" | ")