from abc import ABC, abstractmethod
from datetime import date

class Habitacion(ABC):
    def __init__(self, numero):
        self.numero = numero
        self.reservada = False
        self.fecha_reserva = None
    
    @abstractmethod
    def calcular_precio(self):
        pass
    
    def reservar(self):
        if not self.reservada:
            self.reservada = True
            self.fecha_reserva = date.today()
            return f"✅ Habitación {self.numero} reservada por ${self.calcular_precio()}"
        return f"❌ Habitación {self.numero} ya está reservada"
    
    def liberar(self):
        self.reservada = False
        self.fecha_reserva = None
        return f"✅ Habitación {self.numero} liberada"

class Simple(Habitacion):
    def calcular_precio(self):
        return 100

class Doble(Habitacion):
    def calcular_precio(self):
        return 150

class Suite(Habitacion):
    def calcular_precio(self):
        return 300

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []  # Composición
    
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        return f"✅ Habitación {habitacion.numero} agregada al hotel"
    
    def reservar_habitacion(self, tipo_habitacion):
        for hab in self.habitaciones:
            if hab.__class__.__name__ == tipo_habitacion and not hab.reservada:
                return hab.reservar()
        return f"❌ No hay {tipo_habitacion} disponibles"
    
    def calcular_ingresos(self):
        total = 0
        for hab in self.habitaciones:
            if hab.reservada:
                total += hab.calcular_precio()
        return total
    
    def verificar_disponibilidad(self, tipo=None):
        disponibles = []
        for hab in self.habitaciones:
            if not hab.reservada:
                if tipo is None or hab.__class__.__name__ == tipo:
                    disponibles.append(hab)
        return disponibles
    
    def mostrar_estado(self):
        print(f"🏨 HOTEL: {self.nombre}")
        print(f"  Ingresos actuales: ${self.calcular_ingresos()}")
        print("  Habitaciones:")
        for hab in self.habitaciones:
            estado = "✅ Disponible" if not hab.reservada else f"❌ Reservada (${hab.calcular_precio()})"
            print(f"    {hab.__class__.__name__} #{hab.numero}: {estado}")

# Uso
if __name__ == "__main__":
    # Crear hotel
    hotel = Hotel("Plaza")
    
    # Agregar habitaciones (composición)
    print(hotel.agregar_habitacion(Simple("101")))
    print(hotel.agregar_habitacion(Simple("102")))
    print(hotel.agregar_habitacion(Doble("201")))
    print(hotel.agregar_habitacion(Suite("301")))
    
    # Reservar habitaciones (polimorfismo)
    print(hotel.reservar_habitacion("Simple"))
    print(hotel.reservar_habitacion("Doble"))
    
    # Mostrar estado
    hotel.mostrar_estado()
    
    # Verificar disponibilidad
    print("\n📋 Disponibilidad:")
    disponibles = hotel.verificar_disponibilidad()
    print(f"  Total disponibles: {len(disponibles)}")
    
    # Precios diferentes por tipo (polimorfismo)
    print("\n💰 Precios por tipo:")
    for hab in hotel.habitaciones[:3]:  # Mostrar primeros 3 tipos
        print(f"  {hab.__class__.__name__}: ${hab.calcular_precio()}")