class Equipaje:
    def __init__(self, peso, tipo="maleta"):
        self.peso = peso  # kg
        self.tipo = tipo
    
    def __str__(self):
        return f"🎒 {self.tipo}: {self.peso}kg"

class Pasajero:
    def __init__(self, nombre, pasaporte):
        self.nombre = nombre
        self.pasaporte = pasaporte
        self.equipaje = None
    
    def agregar_equipaje(self, peso):
        self.equipaje = Equipaje(peso)
        return f"✅ Equipaje de {peso}kg agregado a {self.nombre}"
    
    def __str__(self):
        equipaje_info = f", Equipaje: {self.equipaje.peso}kg" if self.equipaje else ", Sin equipaje"
        return f"👤 {self.nombre} ({self.pasaporte}{equipaje_info})"

class Vuelo:
    def __init__(self, numero, destino, capacidad=100):
        self.numero = numero
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []  # Agregación
    
    def agregar_pasajero(self, pasajero):
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            return f"✅ {pasajero.nombre} agregado al vuelo {self.numero}"
        return f"❌ Vuelo lleno, no se puede agregar a {pasajero.nombre}"
    
    def peso_total_equipaje(self):
        total = 0
        for pasajero in self.pasajeros:
            if pasajero.equipaje:
                total += pasajero.equipaje.peso
        return total
    
    def verificar_disponibilidad(self):
        disponibles = self.capacidad - len(self.pasajeros)
        return f"Disponibles: {disponibles}/{self.capacidad} asientos"
    
    def mostrar_vuelo(self):
        print(f"✈️ VUELO {self.numero} a {self.destino}")
        print(f"  {self.verificar_disponibilidad()}")
        print(f"  Peso total equipaje: {self.peso_total_equipaje()}kg")
        print("  Pasajeros:")
        for pasajero in self.pasajeros:
            print(f"    {pasajero}")

# Uso
if __name__ == "__main__":
    # Crear vuelo
    vuelo = Vuelo("IB1234", "Madrid", capacidad=3)
    
    # Crear pasajeros independientes
    p1 = Pasajero("Ana García", "AB123456")
    p2 = Pasajero("Carlos Ruiz", "CD789012")
    p3 = Pasajero("María López", "EF345678")
    p4 = Pasajero("Pedro Sánchez", "GH901234")  # No cabrá
    
    # Agregar equipaje
    print(p1.agregar_equipaje(23))
    print(p2.agregar_equipaje(15))
    print(p3.agregar_equipaje(30))
    
    # Agregar pasajeros al vuelo (agregación)
    print(vuelo.agregar_pasajero(p1))
    print(vuelo.agregar_pasajero(p2))
    print(vuelo.agregar_pasajero(p3))
    print(vuelo.agregar_pasajero(p4))  # Este fallará
    
    # Mostrar información
    vuelo.mostrar_vuelo()