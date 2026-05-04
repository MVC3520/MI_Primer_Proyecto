class Cuenta:
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"✅ ${monto:.2f} depositado en cuenta {self.numero}"
        return "❌ Monto inválido"
    
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return f"✅ ${monto:.2f} retirado de cuenta {self.numero}"
        return "❌ Fondos insuficientes o monto inválido"
    
    def calcular_interes(self):
        return 0  # Método base, será sobrescrito
    
    def __str__(self):
        return f"Cuenta {self.numero}: ${self.saldo:.2f}"

class Ahorros(Cuenta):
    def __init__(self, numero, cliente, saldo=0):
        super().__init__(numero, cliente, saldo)
        self.tasa_interes = 0.03  # 3%
    
    def calcular_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        return f"💰 Interés aplicado: ${interes:.2f}"

class Corriente(Cuenta):
    def __init__(self, numero, cliente, saldo=0, limite_descubierto=500):
        super().__init__(numero, cliente, saldo)
        self.limite_descubierto = limite_descubierto
    
    def retirar(self, monto):
        disponible = self.saldo + self.limite_descubierto
        if 0 < monto <= disponible:
            self.saldo -= monto
            return f"✅ ${monto:.2f} retirado (incluye descubierto)"
        return "❌ Excede límite de descubierto"

class PlazoFijo(Cuenta):
    def __init__(self, numero, cliente, saldo=0, plazo_meses=12):
        super().__init__(numero, cliente, saldo)
        self.plazo_meses = plazo_meses
        self.tasa_interes = 0.05  # 5%
    
    def calcular_interes(self):
        if self.plazo_meses >= 12:
            interes = self.saldo * self.tasa_interes
            self.saldo += interes
            return f"💰 Interés anual aplicado: ${interes:.2f}"
        return "⏳ Aún no vence el plazo"

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.cuentas = []  # Agregación
    
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        return f"✅ Cuenta {cuenta.numero} agregada a {self.nombre}"
    
    def __str__(self):
        return f"👤 {self.nombre} (DNI: {self.dni}) - {len(self.cuentas)} cuentas"

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []  # Agregación
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        return f"✅ Cliente {cliente.nombre} agregado al banco"
    
    def transferir(self, origen_num, destino_num, monto):
        # Buscar cuentas
        cuenta_origen = None
        cuenta_destino = None
        
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.numero == origen_num:
                    cuenta_origen = cuenta
                if cuenta.numero == destino_num:
                    cuenta_destino = cuenta
        
        if cuenta_origen and cuenta_destino:
            if cuenta_origen.retirar(monto).startswith("✅"):
                cuenta_destino.depositar(monto)
                return f"✅ Transferencia de ${monto:.2f} completada"
            return "❌ Transferencia fallida"
        return "❌ Cuentas no encontradas"
    
    def generar_reporte(self):
        print(f"🏦 BANCO: {self.nombre}")
        print(f"  Total clientes: {len(self.clientes)}")
        
        total_saldos = 0
        for cliente in self.clientes:
            print(f"\n  {cliente}")
            for cuenta in cliente.cuentas:
                print(f"    {cuenta}")
                total_saldos += cuenta.saldo
        
        print(f"\n💰 Total saldos: ${total_saldos:.2f}")

# Uso
if __name__ == "__main__":
    # Crear banco
    banco = Banco("Nacional")
    
    # Crear clientes
    cliente1 = Cliente("12345678", "Ana García")
    cliente2 = Cliente("87654321", "Carlos Ruiz")
    
    print(banco.agregar_cliente(cliente1))
    print(banco.agregar_cliente(cliente2))
    
    # Crear cuentas con herencia
    c1 = Ahorros("001", cliente1, 1000)
    c2 = Corriente("002", cliente1, 500)
    c3 = PlazoFijo("003", cliente2, 2000)
    
    print(cliente1.agregar_cuenta(c1))
    print(cliente1.agregar_cuenta(c2))
    print(cliente2.agregar_cuenta(c3))
    
    # Operaciones
    print(c1.depositar(500))
    print(c2.retirar(200))
    print(c3.calcular_interes())
    
    # Transferencia
    print(banco.transferir("001", "003", 300))
    
    # Reporte
    banco.generar_reporte()