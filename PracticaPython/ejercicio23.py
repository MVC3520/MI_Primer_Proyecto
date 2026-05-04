class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class Carrito:
    def __init__(self):
        self.items = {}  # {producto: cantidad} - Agregación
    
    def agregar_producto(self, producto, cantidad=1):
        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad
        return f"✅ {cantidad} x {producto.nombre} agregado"
    
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.items.items():
            total += producto.precio * cantidad
        return total
    
    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            total = self.calcular_total()
            descuento = total * (porcentaje / 100)
            return total - descuento
        return self.calcular_total()
    
    def mostrar_carrito(self):
        if not self.items:
            print("🛒 Carrito vacío")
            return
        
        print("🛒 CONTENIDO DEL CARRITO:")
        for producto, cantidad in self.items.items():
            subtotal = producto.precio * cantidad
            print(f"  {cantidad} x {producto.nombre}: ${subtotal:.2f}")
        
        total = self.calcular_total()
        print(f"💰 TOTAL: ${total:.2f}")

# Uso
if __name__ == "__main__":
    # Crear productos
    p1 = Producto("001", "Laptop", 1000)
    p2 = Producto("002", "Mouse", 50)
    p3 = Producto("003", "Teclado", 80)
    
    # Crear carrito
    carrito = Carrito()
    
    # Agregar productos (agregación)
    print(carrito.agregar_producto(p1))
    print(carrito.agregar_producto(p2, 2))
    print(carrito.agregar_producto(p3))
    
    # Mostrar carrito
    carrito.mostrar_carrito()
    
    # Aplicar descuento
    print(f"\nCon 10% de descuento: ${carrito.aplicar_descuento(10):.2f}")