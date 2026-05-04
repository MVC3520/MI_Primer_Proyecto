'''11.Figuras geométricas: Crear una jerarquía de clases que implemente diferentes figuras geométricas 
aplicando herencia y polimorfismo. Deberás desarrollar una clase base Figura con métodos para calcular 
área y perímetro, y luego crear clases derivadas Cuadrado, Rectángulo, Círculo y Triángulo que 
sobrescriban estos métodos con sus fórmulas específicas. Finalmente, demostrarás el polimorfismo 
creando una lista de figuras de diferentes tipos y calculando áreas y perímetros totales de manera 
unificada'''
import math

class Figura:
    """Clase base para figuras geométricas"""
    
    def area(self):
        """Método base - devuelve 0 si no se sobrescribe"""
        return 0
    
    def perimetro(self):
        """Método base - devuelve 0 si no se sobrescribe"""
        return 0
    
    def mostrar_info(self):
        """Muestra información de la figura"""
        nombre = self.__class__.__name__
        return f"{nombre}: Área = {self.area():.2f}, Perímetro = {self.perimetro():.2f}"

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return 4 * self.lado

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        # Para perímetro necesitamos los 3 lados
        self.lado1 = base
        self.lado2 = altura
        # Calculamos hipotenusa para triángulo rectángulo
        self.lado3 = math.sqrt(base**2 + altura**2)
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Uso del polimorfismo
if __name__ == "__main__":
    print("=== FIGURAS GEOMÉTRICAS ===")
    
    # Crear figuras
    mi_cuadrado = Cuadrado(5)
    mi_rectangulo = Rectangulo(4, 6)
    mi_circulo = Circulo(3)
    mi_triangulo = Triangulo(3, 4)
    
    # Lista polimórfica
    mis_figuras = [mi_cuadrado, mi_rectangulo, mi_circulo, mi_triangulo]
    
    # Mostrar información de cada figura
    for figura in mis_figuras:
        print(figura.mostrar_info())
    
    # Cálculos polimórficos
    print("\n=== CÁLCULOS CON POLIMORFISMO ===")
    
    # Área total
    area_total = 0
    for figura in mis_figuras:
        area_total += figura.area()  # ¡Polimorfismo en acción!
    print(f"Área total de todas las figuras: {area_total:.2f}")
    
    # Perímetro total
    perimetro_total = 0
    for figura in mis_figuras:
        perimetro_total += figura.perimetro()
    print(f"Perímetro total: {perimetro_total:.2f}")
    
    # Buscar figura con mayor área
    figura_mayor = None
    mayor_area = 0
    
    for figura in mis_figuras:
        if figura.area() > mayor_area:
            mayor_area = figura.area()
            figura_mayor = figura
    
    if figura_mayor:
        print(f"\nFigura con mayor área: {figura_mayor.__class__.__name__}")
        print(f"Área: {mayor_area:.2f}")
