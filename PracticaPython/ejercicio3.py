#Rectángulo con propiedades: 
# Clase Rectangulo con atributos largo y ancho (privados). 
# Métodos: calcular_area(), calcular_perimetro(). 
#  Usar getters y setters para los atributos.

class RectanguloPythonico:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho
    
    # PROPERTY para largo
    @property
    def largo(self):  # Nombre simple, sin "get_"
        """Getter para largo usando property"""
        return self.__largo
    
    @largo.setter
    def largo(self, valor):
        """Setter para largo"""
        if valor > 0:
            self.__largo = valor  
        else:
            raise ValueError("El largo debe ser positivo")
    
    # PROPERTY para ancho
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self.__ancho = valor
        else:
            raise ValueError("El ancho debe ser positivo")
    
    # PROPERTIES calculadas
    @property
    def area(self):
        """Property calculada para área"""
        return self.__largo * self.__ancho
    
    @property
    def perimetro(self):
        """Property calculada para perímetro"""
        return 2 * (self.__largo + self.__ancho)

# USO VERSIÓN PYTHONICA
print("\n=== Versión Pythonica ===")
rect2 = RectanguloPythonico(5, 3)
print(f"Largo: {rect2.largo}")      
print(f"Área: {rect2.area}")        
print(f"Perímetro: {rect2.perimetro}")

rect2.largo = 10  # Usa setter automáticamente
print(f"Nuevo área: {rect2.area}")

# Probar validación
try:
    rect2.largo = -5  # Esto lanzará ValueError
except ValueError as e:
    print(f"Error: {e}")