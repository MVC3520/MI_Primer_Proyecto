class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} (${self.precio:.2f})"

class ItemOrden:
    def __init__(self, producto, cantidad):
        self.producto = producto  # Referencia
        self.cantidad = cantidad
    
    def subtotal(self):
        return self.producto.precio * self.cantidad
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}: ${self.subtotal():.2f}"

class Orden:
    def __init__(self, numero):
        self.numero = numero
        self.items = []  # Composición
    
    def agregar_item(self, producto, cantidad=1):
        item = ItemOrden(producto, cantidad)
        self.items.append(item)
        return f"✅ {cantidad} x {producto.nombre} agregado"
    
    def calcular_total(self):
        return sum(item.subtotal() for item in self.items)
    
    def aplicar_descuento_cantidad(self, minimo=5, descuento=10):
        # Aplica descuento si algún item tiene cantidad mínima
        total = self.calcular_total()
        for item in self.items:
            if item.cantidad >= minimo:
                return total * (1 - descuento/100)
        return total
    
    def mostrar_detalle(self):
        print(f"📋 ORDEN #{self.numero}")
        if not self.items:
            print("  Sin items")
            return
        for item in self.items:
            print(f"  {item}")
        print(f"💰 Subtotal: ${self.calcular_total():.2f}")
        print(f"💰 Con descuento (si aplica): ${self.aplicar_descuento_cantidad():.2f}")

# Uso
if __name__ == "__main__":
    # Crear productos
    p1 = Producto("001", "Laptop", 1000)
    p2 = Producto("002", "Mouse", 50)
    p3 = Producto("003", "Teclado", 80)
    
    # Crear orden y agregar items (composición)
    orden = Orden("2024-001")
    print(orden.agregar_item(p1))
    print(orden.agregar_item(p2, 3))
    print(orden.agregar_item(p3, 6))  # Más de 5, aplica descuento
    
    # Mostrar detalle
    orden.mostrar_detalle()