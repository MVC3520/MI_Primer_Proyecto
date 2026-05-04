#15.Crea un sistema de pagos usando herencia y polimorfismo. 
# Implementa una clase base Pago con atributos de solo lectura: monto y procesado, y un método 
# procesar_pago() que debe ser sobrescrito. Luego crea las clases TarjetaCredito, PayPal y 
# TransferenciaBancaria que hereden de Pago y sobrescriban procesar_pago() con su lógica específica. 
# Incluye también validaciones apropiadas para cada tipo de pago. Finalmente, demuestra el polimorfismo 
# creando una lista con diferentes pagos y procesándolos de manera unificada.
#Requisitos:
#Los atributos monto y procesado deben ser de solo lectura
#Cada tipo de pago debe tener validaciones específicas
#El método procesar_pago() debe actualizar el estado


class Pago:
    def __init__(self, monto):
        self._monto = monto  # Atributo "privado"
        self._procesado = False
    
    @property
    def monto(self):
        """Monto es solo lectura"""
        return self._monto
    
    ''' @monto.setter
    def monto(self, valor):
        raise AttributeError("Monto es de solo lectura")  # Lanza error explícito'''
        
    @property
    def procesado(self):
        """Estado de procesamiento es solo lectura"""
        return self._procesado
    
    def procesar_pago(self):
        """Método base - debe ser sobrescrito"""
        self._procesado = True
        return f"Pago genérico de ${self._monto:.2f}"
    
    def __str__(self):
        tipo = self.__class__.__name__
        return f"{tipo}: ${self.monto:.2f} - {'✅' if self.procesado else '❌'}"

class TarjetaCredito(Pago):
    def __init__(self, monto, numero_tarjeta):
        super().__init__(monto)
        self.numero_tarjeta = numero_tarjeta
    
    def procesar_pago(self):
        if not self._validar_tarjeta():
            return "❌ Tarjeta inválida"
        
        self._procesado = True
        ultimos_4 = str(self.numero_tarjeta)[-4:]
        return f"✅ Pago con tarjeta ****{ultimos_4} por ${self.monto:.2f}"
    
    def _validar_tarjeta(self):
        return len(str(self.numero_tarjeta)) == 16

class PayPal(Pago):
    def __init__(self, monto, email):
        super().__init__(monto)
        self.email = email
    
    def procesar_pago(self):
        if '@' not in self.email:
            return "❌ Email inválido"
        
        self._procesado = True
        return f"✅ Pago PayPal ({self.email}) por ${self.monto:.2f}"

class TransferenciaBancaria(Pago):
    def __init__(self, monto, cuenta_destino):
        super().__init__(monto)
        self.cuenta_destino = cuenta_destino
    
    def procesar_pago(self):
        if self.monto > 5000:
            return "⚠️ Transferencia requiere verificación"
        
        self._procesado = True
        return f"✅ Transferencia a {self.cuenta_destino} por ${self.monto:.2f}"

# Uso del sistema
if __name__ == "__main__":
    print("=== SISTEMA DE PAGOS (con atributos readonly) ===\n")
    
    # Crear diferentes tipos de pagos
    pagos = [
        TarjetaCredito(150.50, "1234567812345678"),
        PayPal(75.99, "cliente@email.com"),
        TransferenciaBancaria(2000, "CUENTA-001"),
        PayPal(300, "emailinvalido"),  # Email sin @
        TarjetaCredito(500, "1234"),   # Tarjeta inválida
    ]
    
    # Procesar pagos polimórficamente
    print("Procesando pagos:")
    for pago in pagos:
        resultado = pago.procesar_pago()
        print(f"  {resultado}")
    
    # Mostrar estado final
    print("\nEstado final de los pagos:")
    for pago in pagos:
        print(f"  {pago}")
    
    # Intentar modificar atributos readonly (esto NO funcionará si están bien implementados)
    print("\n=== DEMOSTRACIÓN readonly ===")
    try:
        # Esto debería fallar o no modificar nada
        pago = pagos[0]
        print(f"Monto original: ${pago.monto}")
        # pago.monto = 1000  # Esto debería dar error si implementamos setter que lanza excepción
        print(f"Monto después de intentar modificar: ${pago.monto} (sin cambios)")
    except Exception as e:
        print(f"Error al intentar modificar: {type(e).__name__}")
    
    # Estadísticas
    print("\n=== ESTADÍSTICAS ===")
    total_procesado = sum(p.monto for p in pagos if p.procesado)
    exitosos = sum(1 for p in pagos if p.procesado)
    
    print(f"Pagos exitosos: {exitosos}/{len(pagos)}")
    print(f"Total procesado: ${total_procesado:.2f}")