import random
from abc import ABC, abstractmethod

# Clase base Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre

# Herencia: Jugador hereda de Persona
class Jugador(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.mano = []
        self.vida = 100
        self.puntos = 0
    
    def recibir_carta(self, carta):
        self.mano.append(carta)
        return f"🃏 {self.nombre} recibe: {carta}"
    
    def jugar_carta(self, indice):
        if 0 <= indice < len(self.mano):
            carta = self.mano.pop(indice)
            return carta
        return None
    
    def mostrar_mano(self):
        print(f"👤 {self.nombre} (Vida: {self.vida}, Puntos: {self.puntos})")
        if not self.mano:
            print("  Mano vacía")
            return
        for i, carta in enumerate(self.mano):
            print(f"  {i}: {carta}")
    
    def __str__(self):
        return f"👤 {self.nombre} - Vida: {self.vida}, Puntos: {self.puntos}, Cartas: {len(self.mano)}"

# Clase base para polimorfismo
class Carta(ABC):
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo
    
    @abstractmethod
    def efecto(self, jugador, oponente):
        pass
    
    def __str__(self):
        return f"{self.nombre} (Costo: {self.costo})"

# Polimorfismo: diferentes tipos de cartas
class CartaAtaque(Carta):
    def __init__(self, nombre, costo, danio):
        super().__init__(nombre, costo)
        self.danio = danio
    
    def efecto(self, jugador, oponente):
        oponente.vida -= self.danio
        return f"⚔️ {jugador.nombre} ataca con {self.nombre} (-{self.danio} vida a {oponente.nombre})"

class CartaDefensa(Carta):
    def __init__(self, nombre, costo, defensa):
        super().__init__(nombre, costo)
        self.defensa = defensa
    
    def efecto(self, jugador, oponente):
        jugador.vida += self.defensa
        return f"🛡️ {jugador.nombre} se defiende con {self.nombre} (+{self.defensa} vida)"

class CartaEspecial(Carta):
    def __init__(self, nombre, costo, efecto_especial):
        super().__init__(nombre, costo)
        self.efecto_especial = efecto_especial
    
    def efecto(self, jugador, oponente):
        if self.efecto_especial == "robar":
            jugador.puntos += 10
            return f"🎯 {jugador.nombre} usa {self.nombre} (+10 puntos)"
        elif self.efecto_especial == "curar":
            jugador.vida += 20
            return f"💖 {jugador.nombre} usa {self.nombre} (+20 vida)"
        return f"✨ {jugador.nombre} usa {self.nombre}"

# Composición: Mazo está compuesto por Cartas
class Mazo:
    def __init__(self):
        self.cartas = []  # Composición
    
    def agregar_carta(self, carta):
        self.cartas.append(carta)
        return f"✅ {carta.nombre} agregada al mazo"
    
    def barajar(self):
        random.shuffle(self.cartas)
        return "🔀 Mazo barajado"
    
    def repartir(self, jugadores, cartas_por_jugador=3):
        for jugador in jugadores:
            for _ in range(cartas_por_jugador):
                if self.cartas:
                    carta = self.cartas.pop()
                    jugador.recibir_carta(carta)
        return f"🃏 {cartas_por_jugador} cartas repartidas a cada jugador"
    
    def __str__(self):
        return f"Mazo con {len(self.cartas)} cartas"

# Clase principal que coordina todo
class Juego:
    def __init__(self):
        self.jugadores = []
        self.mazo = Mazo()  # Composición
        self.turno = 0
    
    def agregar_jugador(self, nombre):
        jugador = Jugador(nombre)
        self.jugadores.append(jugador)
        return f"✅ Jugador {nombre} agregado"
    
    def crear_mazo_estandar(self):
        # Agregar cartas al mazo (composición)
        cartas = [
            CartaAtaque("Espada", 2, 15),
            CartaAtaque("Flecha", 1, 10),
            CartaDefensa("Escudo", 2, 20),
            CartaDefensa("Armadura", 3, 30),
            CartaEspecial("Poción", 2, "curar"),
            CartaEspecial("Tesoro", 3, "robar"),
            CartaAtaque("Hechizo", 4, 25),
            CartaDefensa("Muro", 1, 15),
        ]
        
        for carta in cartas:
            self.mazo.agregar_carta(carta)
        
        self.mazo.barajar()
        return f"✅ Mazo creado con {len(cartas)} cartas"
    
    def iniciar_partida(self):
        if len(self.jugadores) < 2:
            return "❌ Se necesitan al menos 2 jugadores"
        
        print("🎮 INICIANDO PARTIDA")
        print("=" * 40)
        
        # Repartir cartas
        self.mazo.repartir(self.jugadores, 3)
        
        # Jugar 3 rondas
        for ronda in range(3):
            print(f"\n🔄 RONDA {ronda + 1}")
            print("-" * 30)
            
            for jugador in self.jugadores:
                # Mostrar estado
                for j in self.jugadores:
                    print(f"  {j}")
                
                if jugador.mano:
                    # Elegir carta aleatoria
                    indice = random.randint(0, len(jugador.mano) - 1)
                    carta = jugador.jugar_carta(indice)
                    
                    # Encontrar oponente
                    oponentes = [j for j in self.jugadores if j != jugador]
                    oponente = random.choice(oponentes) if oponentes else jugador
                    
                    # Aplicar efecto polimórfico
                    if carta:
                        resultado = carta.efecto(jugador, oponente)
                        print(f"\n  {resultado}")
                
                print()  # Espacio entre turnos
        
        return self.determinar_ganador()
    
    def determinar_ganador(self):
        print("=" * 40)
        print("🏆 FIN DE LA PARTIDA")
        print("=" * 40)
        
        # Calcular puntuación combinada
        for jugador in self.jugadores:
            jugador.puntos += jugador.vida // 10
        
        # Encontrar ganador
        ganador = max(self.jugadores, key=lambda j: j.puntos)
        
        print("\n📊 RESULTADOS FINALES:")
        for jugador in self.jugadores:
            print(f"  {jugador}")
        
        print(f"\n🎉 GANADOR: {ganador.nombre}!")
        return ganador

# Uso
if __name__ == "__main__":
    # Crear juego
    juego = Juego()
    
    # Agregar jugadores (herencia de Persona)
    print(juego.agregar_jugador("Ana"))
    print(juego.agregar_jugador("Carlos"))
    print(juego.agregar_jugador("María"))
    
    # Crear mazo (composición)
    print(juego.crear_mazo_estandar())
    
    # Mostrar mazo inicial
    print(f"\n{juego.mazo}")
    
    # Iniciar partida
    resultado = juego.iniciar_partida()
    
    # Demostrar polimorfismo
    print("\n🎯 DEMOSTRACIÓN DE POLIMORFISMO:")
    cartas_ejemplo = [
        CartaAtaque("Ejemplo Ataque", 1, 10),
        CartaDefensa("Ejemplo Defensa", 1, 10),
        CartaEspecial("Ejemplo Especial", 1, "curar")
    ]
    
    jugador_ejemplo = Jugador("Demo")
    oponente_ejemplo = Jugador("Oponente")
    
    for carta in cartas_ejemplo:
        # Mismo método, efectos diferentes (polimorfismo)
        efecto = carta.efecto(jugador_ejemplo, oponente_ejemplo)
        print(f"  {efecto}")