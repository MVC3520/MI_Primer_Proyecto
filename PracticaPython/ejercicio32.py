class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class ProductoFisico(Producto):
    def __init__(self, codigo, nombre, precio, peso):
        super().__init__(codigo, nombre, precio)
        self.peso = peso
        self.tipo = "Físico"
    
    def calcular_envio(self):
        return self.peso * 0.5  # $0.5 por kg

class ProductoDigital(Producto):
    def __init__(self, codigo, nombre, precio, tamano_mb):
        super().__init__(codigo, nombre, precio)
        self.tamano_mb = tamano_mb
        self.tipo = "Digital"
    
    def calcular_envio(self):
        return 0  # Envío gratuito para digital

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Agregación
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        return f"✅ {producto.nombre} agregado a {self.nombre}"

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.carrito = Carrito()  # Inicializar carrito aquí
    
    def __str__(self):
        return f"👤 {self.nombre} ({self.email})"

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
            # Polimorfismo: envío diferente por tipo
            if hasattr(producto, 'calcular_envio'):
                total += producto.calcular_envio() * cantidad
        return total
    
    def generar_orden(self, cliente):
        if not self.items:
            return None
        orden = Orden(cliente, self.items.copy())
        self.items.clear()  # Vaciar carrito
        return orden
    
    def mostrar(self):
        if not self.items:
            print("🛒 Carrito vacío")
            return
        
        print("🛒 CONTENIDO DEL CARRITO:")
        for producto, cantidad in self.items.items():
            subtotal = producto.precio * cantidad
            envio = producto.calcular_envio() * cantidad if hasattr(producto, 'calcular_envio') else 0
            print(f"  {cantidad} x {producto.nombre}: ${subtotal:.2f} + ${envio:.2f} envío")
        
        total = self.calcular_total()
        print(f"💰 TOTAL: ${total:.2f}")

class Orden:
    def __init__(self, cliente, items):
        self.cliente = cliente
        self.items = items  # Composición
        self.total = self.calcular_total()
        self.numero = f"ORD-{hash(self) % 10000:04d}"
    
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.items.items():
            total += producto.precio * cantidad
            if hasattr(producto, 'calcular_envio'):
                total += producto.calcular_envio() * cantidad
        return total
    
    def mostrar(self):
        print(f"📋 ORDEN #{self.numero}")
        print(f"  Cliente: {self.cliente.nombre}")
        print("  Productos:")
        for producto, cantidad in self.items.items():
            subtotal = producto.precio * cantidad
            envio = producto.calcular_envio() * cantidad if hasattr(producto, 'calcular_envio') else 0
            print(f"    {cantidad} x {producto.nombre}")
            print(f"      Precio: ${producto.precio:.2f} x {cantidad} = ${subtotal:.2f}")
            if envio > 0:
                print(f"      Envío: ${envio:.2f}")
        print(f"  💰 TOTAL: ${self.total:.2f}")

# Uso CORREGIDO
if __name__ == "__main__":
    print("=== TIENDA ONLINE COMPLETA ===\n")
    
    # Crear productos con herencia
    laptop = ProductoFisico("001", "Laptop", 1000, 2.5)
    ebook = ProductoDigital("002", "E-book Python", 50, 5)
    mouse = ProductoFisico("003", "Mouse", 30, 0.3)
    
    print(f"📦 Productos creados:")
    print(f"  {laptop} ({laptop.tipo}, {laptop.peso}kg)")
    print(f"  {ebook} ({ebook.tipo}, {ebook.tamano_mb}MB)")
    print(f"  {mouse} ({mouse.tipo}, {mouse.peso}kg)")
    
    # Crear categorías
    electronica = Categoria("Electrónica")
    libros = Categoria("Libros")
    
    print(f"\n📂 Categorías:")
    print(electronica.agregar_producto(laptop))
    print(electronica.agregar_producto(mouse))
    print(libros.agregar_producto(ebook))
    
    # Crear cliente (con carrito automático)
    cliente = Cliente("Ana García", "ana@email.com")
    print(f"\n👤 Cliente creado: {cliente}")
    print(f"  Carrito automáticamente creado ✓")
    
    # Agregar productos al carrito (agregación)
    print(f"\n🛒 Agregando al carrito:")
    print(cliente.carrito.agregar_producto(laptop))
    print(cliente.carrito.agregar_producto(ebook))
    print(cliente.carrito.agregar_producto(mouse, 2))
    
    # Mostrar carrito
    print()
    cliente.carrito.mostrar()
    
    # Calcular total (con envíos polimórficos)
    total = cliente.carrito.calcular_total()
    print(f"\n💰 Resumen de costos:")
    print(f"  Productos físicos incluyen envío basado en peso")
    print(f"  Productos digitales: envío gratuito")
    print(f"  Total final: ${total:.2f}")
    
    # Generar orden (composición)
    print(f"\n📋 Generando orden...")
    orden = cliente.carrito.generar_orden(cliente)
    
    if orden:
        orden.mostrar()
        print(f"\n✅ Orden generada exitosamente")
        print(f"   Carrito ahora está vacío")
        
        # Verificar carrito vacío
        print()
        cliente.carrito.mostrar()
    else:
        print("❌ No se pudo generar orden (carrito vacío)")
    
    # Demostrar herencia
    print(f"\n🎯 DEMOSTRACIÓN DE HERENCIA:")
    productos = [laptop, ebook, mouse]
    for producto in productos:
        print(f"  {producto.nombre}:")
        print(f"    Tipo: {producto.__class__.__name__}")
        print(f"    Precio base: ${producto.precio:.2f}")
        if hasattr(producto, 'calcular_envio'):
            print(f"    Costo envío: ${producto.calcular_envio():.2f}")
            print(f"    Polimorfismo: método calcular_envio()")