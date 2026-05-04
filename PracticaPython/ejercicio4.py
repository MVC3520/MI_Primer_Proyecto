#Círculo vs Cilindro: 
# Clase Circulo con radio y método area(). 
# Clase Cilindro que hereda de Circulo y agrega altura con método volumen().
import math

class Circulo:
    def __init__(self,radio) -> None:
        self.radio=radio
    def area(self):
        return self.radio*self.radio*math.pi
    def mostrar_info(self):
        print(f"Círculo - Radio: {self.radio}")
        print(f"Área: {self.area():.2f}")
        
class Cilindro(Circulo):
    def __init__(self,radio ,altura) -> None:
        # Llama al constructor de la clase padre
        super().__init__(radio)
        # Agrega atributo específico
        self.altura=altura  
    def volumen(self):
        return self.area() * self.altura
    
    def mostrar_info(self):
        """Sobrescribe método para mostrar info específica"""
        print(f"Cilindro - Radio: {self.radio}, Altura: {self.altura}")
        print(f"Volumen: {self.volumen():.2f}")

print("=== Círculo ===")
circulo = Circulo(3)
circulo.mostrar_info()

print("\n=== Cilindro ===")
cilindro = Cilindro(3, 5)
cilindro.mostrar_info()

# Demostración de herencia
print(f"\nEl cilindro ES un círculo: {isinstance(cilindro, Circulo)}")
print(f"El cilindro ES un cilindro: {isinstance(cilindro, Cilindro)}")
print(f"El círculo ES un cilindro: {isinstance(circulo, Cilindro)}")
