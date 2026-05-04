#EJERCICIO 19: Sistema de Figuras 3D con Clase Abstracta
#Crea un sistema de figuras geométricas 3D usando clases abstractas, herencia y polimorfismo. 
# Implementa una clase abstracta Figura3D con métodos abstractos volumen() y area_superficial(), 
# y luego crea las clases concretas Cubo, Esfera y Cilindro que hereden de ella e implementen estos 
# métodos con sus fórmulas correspondientes. Finalmente, demuestra el polimorfismo creando una lista 
# con diferentes figuras 3D y calculando volúmenes y áreas superficiales de manera unificada.

#Lo que se enseña:
#Clases abstractas (ABC y @abstractmethod)
#Polimorfismo en cálculo de volumen y área
#Implementación obligatoria de métodos abstractos
#Jerarquía de herencia con clases abstractas

import math
from abc import ABC, abstractmethod

# Clase abstracta
class Figura3D(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def volumen(self):
        """Calcula el volumen de la figura 3D"""
        pass
    
    @abstractmethod
    def area_superficial(self):
        """Calcula el área superficial de la figura 3D"""
        pass
    
    def mostrar_info(self):
        """Muestra información completa de la figura"""
        vol = self.volumen()
        area = self.area_superficial()
        return (f"📐 {self.nombre} ({self.__class__.__name__})\n"
                f"   Volumen: {vol:.2f} unidades³\n"
                f"   Área superficial: {area:.2f} unidades²")

# Clases concretas
class Cubo(Figura3D):
    def __init__(self, lado):
        super().__init__(f"Cubo de lado {lado}")
        self.lado = lado
    
    def volumen(self):
        return self.lado ** 3
    
    def area_superficial(self):
        return 6 * (self.lado ** 2)

class Esfera(Figura3D):
    def __init__(self, radio):
        super().__init__(f"Esfera de radio {radio}")
        self.radio = radio
    
    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)
    
    def area_superficial(self):
        return 4 * math.pi * (self.radio ** 2)

class Cilindro(Figura3D):
    def __init__(self, radio, altura):
        super().__init__(f"Cilindro r={radio}, h={altura}")
        self.radio = radio
        self.altura = altura
    
    def volumen(self):
        return math.pi * (self.radio ** 2) * self.altura
    
    def area_superficial(self):
        return 2 * math.pi * self.radio * (self.altura + self.radio)

# Uso del sistema
if __name__ == "__main__":
    print("=== SISTEMA DE FIGURAS 3D (Clases Abstractas) ===\n")
    
    # Crear diferentes figuras 3D
    figuras = [
        Cubo(5),
        Esfera(3),
        Cilindro(2, 4),
        Cubo(2.5),
        Esfera(1.5),
    ]
    
    # Mostrar información de todas las figuras (polimorfismo)
    print("📊 INFORMACIÓN DE FIGURAS 3D:")
    print("=" * 50)
    for figura in figuras:
        print(figura.mostrar_info())
        print("-" * 50)
    
    # Cálculos polimórficos
    print("\n📈 CÁLCULOS TOTALES:")
    print("=" * 50)
    
    # Calcular volumen total
    volumen_total = 0
    for figura in figuras:
        volumen_total += figura.volumen()
    print(f"Volumen total de todas las figuras: {volumen_total:.2f} unidades³")
    
    # Calcular área superficial total
    area_total = 0
    for figura in figuras:
        area_total += figura.area_superficial()
    print(f"Área superficial total: {area_total:.2f} unidades²")
    
    # Encontrar figura con mayor volumen
    mayor_volumen = 0
    figura_mayor = None
    
    for figura in figuras:
        vol = figura.volumen()
        if vol > mayor_volumen:
            mayor_volumen = vol
            figura_mayor = figura
    
    if figura_mayor:
        print(f"\n🏆 Figura con mayor volumen:")
        print(f"   {figura_mayor.nombre}")
        print(f"   Volumen: {mayor_volumen:.2f} unidades³")
    
    # Encontrar figura con mayor área superficial
    mayor_area = 0
    figura_mayor_area = None
    
    for figura in figuras:
        area = figura.area_superficial()
        if area > mayor_area:
            mayor_area = area
            figura_mayor_area = figura
    
    if figura_mayor_area:
        print(f"\n📏 Figura con mayor área superficial:")
        print(f"   {figura_mayor_area.nombre}")
        print(f"   Área: {mayor_area:.2f} unidades²")
    
    # Verificar que todas implementan los métodos abstractos
    print("\n✅ VERIFICACIÓN DE IMPLEMENTACIÓN:")
    print("=" * 50)
    for figura in figuras:
        tipo = figura.__class__.__name__
        print(f"✓ {tipo}: Implementa volumen() y area_superficial()")
    
    # Demostrar que no se puede instanciar Figura3D directamente
    print("\n⚠️  DEMOSTRACIÓN DE CLASE ABSTRACTA:")
    print("=" * 50)
    print("Intentando crear una instancia de Figura3D...")
    
    try:
        # Esto debería fallar porque Figura3D es abstracta
        figura_abstracta = Figura3D("Figura Abstracta") # pyright: ignore[reportAbstractUsage]
        print("❌ ERROR inesperado: Se pudo instanciar la clase abstracta")
    except Exception as error:
        print(f"✅ Comportamiento esperado: {type(error).__name__}")
        print(f"   Mensaje: No se pueden crear instancias de clases abstractas")
    
    print("\n🎯 RESUMEN:")
    print("=" * 50)
    print("• Figura3D es una clase abstracta")
    print("• Cubo, Esfera y Cilindro son clases concretas")
    print("• Todas implementan volumen() y area_superficial()")
    print("• Polimorfismo permite tratar todas las figuras igual")