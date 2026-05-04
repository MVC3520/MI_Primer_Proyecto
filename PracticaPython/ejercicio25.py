class Habitacion:
    def __init__(self, tipo, tamaño):
        self.tipo = tipo
        self.tamaño = tamaño  # m²
    
    def __str__(self):
        return f"🏠 {self.tipo}: {self.tamaño}m²"

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []  # Composición
    
    def agregar_habitacion(self, tipo, tamaño):
        habitacion = Habitacion(tipo, tamaño)
        self.habitaciones.append(habitacion)
        return f"✅ {tipo} de {tamaño}m² agregada"
    
    def area_total(self):
        return sum(h.tamaño for h in self.habitaciones)
    
    def mostrar_casa(self):
        print(f"📍 CASA: {self.direccion}")
        if not self.habitaciones:
            print("  Sin habitaciones")
            return
        for hab in self.habitaciones:
            print(f"  {hab}")
        print(f"📐 Área total: {self.area_total()}m²")

# Uso
if __name__ == "__main__":
    # Crear casa y agregar habitaciones (composición)
    casa = Casa("Calle Principal 123")
    
    print(casa.agregar_habitacion("Dormitorio", 15))
    print(casa.agregar_habitacion("Cocina", 12))
    print(casa.agregar_habitacion("Baño", 8))
    print(casa.agregar_habitacion("Sala", 20))
    print(casa.agregar_habitacion("Dormitorio", 12))
    
    # Mostrar información
    casa.mostrar_casa()
    
    # Contar por tipo
    tipos = {}
    for hab in casa.habitaciones:
        tipos[hab.tipo] = tipos.get(hab.tipo, 0) + 1
    
    print("\n📊 Distribución por tipo:")
    for tipo, cantidad in tipos.items():
        print(f"  {tipo}: {cantidad}")