class Jugador:
    def __init__(self, nombre, edad, posicion, valoracion=50):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.valoracion = valoracion  # 0-100
    
    def __str__(self):
        return f"⚽ {self.nombre} ({self.edad} años) - {self.posicion} [{self.valoracion}/100]"

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []  # Agregación
    
    def contratar_jugador(self, jugador):
        self.jugadores.append(jugador)
        return f"✅ {jugador.nombre} contratado por {self.nombre}"
    
    def promedio_edad(self):
        if not self.jugadores:
            return 0
        return sum(j.edad for j in self.jugadores) / len(self.jugadores)
    
    def jugador_mas_valioso(self):
        if not self.jugadores:
            return None
        return max(self.jugadores, key=lambda j: j.valoracion)
    
    def mostrar_equipo(self):
        print(f"🏆 EQUIPO: {self.nombre}")
        if not self.jugadores:
            print("  Sin jugadores")
            return
        for jugador in self.jugadores:
            print(f"  {jugador}")

# Uso
if __name__ == "__main__":
    # Crear jugadores independientes
    j1 = Jugador("Lionel Messi", 36, "Delantero", 95)
    j2 = Jugador("Sergio Ramos", 37, "Defensa", 88)
    j3 = Jugador("Luka Modric", 38, "Mediocampista", 90)
    j4 = Jugador("Thibaut Courtois", 31, "Portero", 92)
    
    # Crear equipo y agregar jugadores (agregación)
    equipo = Equipo("Real Madrid")
    print(equipo.contratar_jugador(j1))
    print(equipo.contratar_jugador(j2))
    print(equipo.contratar_jugador(j3))
    print(equipo.contratar_jugador(j4))
    
    # Mostrar equipo
    equipo.mostrar_equipo()
    
    # Estadísticas
    print(f"\n📊 Estadísticas de {equipo.nombre}:")
    print(f"Promedio de edad: {equipo.promedio_edad():.1f} años")
    mas_valioso = equipo.jugador_mas_valioso()
    if mas_valioso:
        print(f"Jugador más valioso: {mas_valioso.nombre} ({mas_valioso.valoracion}/100)")