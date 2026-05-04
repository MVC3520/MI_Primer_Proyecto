#EJERCICIO 17: Instrumentos musicales
#Crea un sistema de instrumentos musicales usando herencia y polimorfismo. Implementa una clase base 
# Instrumento con atributos nombre y afinado, y un método tocar() que devuelva un sonido genérico. 
# Luego crea las clases Guitarra, Piano y Bateria que hereden de Instrumento y sobrescriban el método 
# tocar() con su sonido específico. Incluye también un método afinar() que cambie el estado a afinado. 
# Finalmente, demuestra el polimorfismo creando una lista "orquesta" con diferentes instrumentos y 
# haciendo que cada uno toque de manera unificada.

#Lo que se enseña:
#Polimorfismo con comportamiento diferente
#Atributos específicos por instrumento
#Lista polimórfica (orquesta)

class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.afinado = False
    
    def tocar(self):
        return f"{self.nombre} está sonando"
    
    def afinar(self):
        self.afinado = True
        return f"{self.nombre} ha sido afinado"
    
    def __str__(self):
        estado = "✅" if self.afinado else "❌"
        return f"{estado} {self.nombre} ({self.__class__.__name__})"

class Guitarra(Instrumento):
    def tocar(self):
        if not self.afinado:
            return f"🎸 {self.nombre}: ¡Está desafinada!"
        return f"🎸 {self.nombre}: ¡Strum strum!"

class Piano(Instrumento):
    def tocar(self):
        if not self.afinado:
            return f"🎹 {self.nombre}: ¡Necesita afinación!"
        return f"🎹 {self.nombre}: ¡Do re mi fa sol!"

class Bateria(Instrumento):
    def tocar(self):
        return f"🥁 {self.nombre}: ¡Boom tss boom!"

# Uso del sistema
if __name__ == "__main__":
    print("=== ORQUESTA DE INSTRUMENTOS ===\n")
    
    # Crear instrumentos para la orquesta
    orquesta = [
        Guitarra("Fender Stratocaster"),
        Piano("Yamaha Grand"),
        Bateria("Pearl Export"),
        Guitarra("Gibson Les Paul"),
        Piano("Casio Digital"),
        Bateria("Ludwig Classic"),
    ]
    
    # Afinar algunos instrumentos
    print("Afianando instrumentos:")
    for instrumento in orquesta[:3]:  # Afinar primeros 3
        print(f"  {instrumento.afinar()}")
    
    # Mostrar estado de los instrumentos
    print("\nInstrumentos en la orquesta:")
    for instrumento in orquesta:
        print(f"  {instrumento}")
    
    # Tocar la orquesta (polimorfismo)
    print("\n🎶 CONCIERTO DE LA ORQUESTA 🎶")
    for instrumento in orquesta:
        print(f"  {instrumento.tocar()}")
    
    # Contar instrumentos afinados
    print("\n=== ESTADÍSTICAS ===")
    afinados = sum(1 for i in orquesta if i.afinado)
    total = len(orquesta)
    
    print(f"Total instrumentos: {total}")
    print(f"Afinados: {afinados}")
    print(f"Por afinar: {total - afinados}")
    
    # Distribución por tipo
    print("\nDistribución por tipo:")
    tipos = {}
    for instrumento in orquesta:
        tipo = instrumento.__class__.__name__
        tipos[tipo] = tipos.get(tipo, 0) + 1
    
    for tipo, cantidad in tipos.items():
        print(f"  {tipo}: {cantidad}")
    
    # Tocando todos juntos (ejemplo final)
    print("\n🎵 ¡TODOS JUNTOS! 🎵")
    for instrumento in orquesta:
        # Solo los afinados suenan bien
        if instrumento.afinado:
            print(f"  {instrumento.tocar()}")
        else:
            print(f"  {instrumento.nombre}: (silencio - necesita afinarse)")