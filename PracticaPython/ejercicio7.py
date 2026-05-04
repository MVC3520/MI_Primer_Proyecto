"""7. Clase Producto con propiedades y métodos de clase

Crear clase Producto para una tienda:

ATRIBUTOS (con validación):
- codigo: auto-generado (ej: "PROD-001"), solo lectura
- nombre: string
- precio_base: > 0 (validar con @property)
- stock: ≥ 0 (validar con @property)

ATRIBUTO DE CLASE:
- IVA: 0.21 (21%) - constante para todos
- contador: cuenta productos creados

MÉTODOS:
- precio_final(): precio_base + IVA
- aplicar_descuento(%): reduce precio_base
- vender(cantidad): resta stock si hay suficiente
- __str__(): muestra código, nombre, precio y stock

MÉTODOS DE CLASE:
- crear_sin_stock(nombre, precio): crea con stock 0
- cambiar_iva(nuevo_iva): modifica IVA general

COMPARACIÓN:
- __lt__(otro): True si precio menor

EJEMPLO:
p1 = Producto("Laptop", 1000, 5)
p2 = Producto.crear_sin_stock("Mouse", 50)
p1.aplicar_descuento(10)  # 10% descuento
print(p1)  # PROD-001: Laptop - $900.00 (5 unidades)
print(p1.precio_final())  # $1089.00 (con IVA 21%)
print(p1 < p2)  # False (900 < 50? No)"""
class Producto:
    IVA = 0.21
    contador = 0
    
    def __init__(self, nombre, precio_base, stock=0):
        self._nombre = nombre
        self.precio_base = precio_base
        self.stock = stock
        
        Producto.contador += 1
        self._codigo = f"PROD-{Producto.contador:03d}"
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def precio_base(self):
        return self._precio_base
    
    @precio_base.setter
    def precio_base(self, valor):
        if valor <= 0:
            raise ValueError("Precio debe ser > 0")
        self._precio_base = valor
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("Stock no puede ser negativo")
        self._stock = valor
    
    def precio_final(self):
        return self.precio_base * (1 + Producto.IVA)
    
    def aplicar_descuento(self, porcentaje):
        if not 0 <= porcentaje <= 100:
            raise ValueError("Descuento inválido")
        descuento = self.precio_base * (porcentaje / 100)
        self.precio_base = self.precio_base - descuento
        return self.precio_base
    
    def vender(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser > 0")
        if cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True
    
    @classmethod
    def crear_sin_stock(cls, nombre, precio):
        return cls(nombre, precio, 0)
    
    @classmethod
    def cambiar_iva(cls, nuevo_iva):
        if nuevo_iva < 0:
            raise ValueError("IVA inválido")
        cls.IVA = nuevo_iva
    
    def __str__(self):
        return f"{self.codigo}: {self._nombre} - ${self.precio_base:.2f} ({self.stock} u.)"
    
    def __lt__(self, otro):
        if not isinstance(otro, Producto):
            return False
        return self.precio_base < otro.precio_base

# Ejemplo mínimo
p1 = Producto("Laptop", 1000, 5)
p2 = Producto.crear_sin_stock("Mouse", 50)
p1.aplicar_descuento(10)
print(p1)  # PROD-001: Laptop - $900.00 (5 u.)
print(p1.precio_final())  # $1089.00
print(p1 < p2)  # False
print(f"Total: {Producto.contador}")  # 2