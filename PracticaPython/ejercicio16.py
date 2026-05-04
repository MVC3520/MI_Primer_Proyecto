#EJERCICIO 16: Notificaciones
#Crea un sistema de notificaciones usando herencia y polimorfismo. 
# Implementa una clase base Notificacion con un método enviar(mensaje) y 
# atributos id (único y auto-generado) y timestamp. Luego crea las clases Email, SMS y PushNotification 
# que hereden de Notificacion y sobrescriban el método enviar() con su lógica específica. Asegúrate 
# que cada notificación tenga un ID único. Finalmente, demuestra el polimorfismo creando una lista 
# con diferentes tipos de notificaciones y enviándolas de manera unificada.
##Requisitos adicionales:
###Cada notificación debe tener un id único auto-generado
###Incluir timestamp de creación
###Validaciones básicas para cada tipo


#Lo que se enseña:
#Polimorfismo con diferentes implementaciones
#Atributos específicos por tipo de notificación
#Métodos comunes con comportamiento diferente

import datetime

class Notificacion:
    _contador = 0  # Atributo de clase para ID único
    
    def __init__(self, mensaje):
        Notificacion._contador += 1
        self.id = f"NOTIF-{Notificacion._contador:03d}"
        self.mensaje = mensaje
        self.timestamp = datetime.datetime.now()
        self.enviada = False
    
    def enviar(self):
        self.enviada = True
        return f"{self.id}: Enviada"
    
    def info(self):
        hora = self.timestamp.strftime("%H:%M:%S")
        return f"{self.id} [{hora}] {self.__class__.__name__}"

class Email(Notificacion):
    def __init__(self, mensaje, destinatario):
        super().__init__(mensaje)
        self.destinatario = destinatario
    
    def enviar(self):
        if '@' not in self.destinatario:
            return f"{self.id}: ❌ Email inválido"
        self.enviada = True
        return f"{self.id}: 📧 Enviado a {self.destinatario}"

class SMS(Notificacion):
    def __init__(self, mensaje, telefono):
        super().__init__(mensaje)
        self.telefono = telefono
    
    def enviar(self):
        if len(str(self.telefono)) != 10:
            return f"{self.id}: ❌ Teléfono inválido"
        self.enviada = True
        return f"{self.id}: 📱 Enviado al {self.telefono}"

class PushNotification(Notificacion):
    def __init__(self, mensaje, dispositivo):
        super().__init__(mensaje)
        self.dispositivo = dispositivo
    
    def enviar(self):
        self.enviada = True
        return f"{self.id}: 🔔 Enviado a {self.dispositivo}"

# Uso del sistema
if __name__ == "__main__":
    print("=== SISTEMA DE NOTIFICACIONES ===\n")
    
    # Crear notificaciones
    notificaciones = [
        Email("Reunión a las 15:00", "juan@email.com"),
        SMS("Código: 1234", "1122334455"),
        PushNotification("Actualización disponible", "dispositivo-001"),
        Email("Promoción especial", "correo-mal"),  # Inválido
        SMS("Oferta limitada", "123"),  # Inválido
    ]
    
    # Mostrar información
    print("Notificaciones creadas:")
    for n in notificaciones:
        print(f"  {n.info()}")
    
    # Enviar (polimorfismo)
    print("\nEnviando notificaciones:")
    for n in notificaciones:
        print(f"  {n.enviar()}")
    
    # Verificar IDs
    print(f"\nIDs generados: {[n.id for n in notificaciones]}")
    
    # Contar éxitos
    exitosas = sum(1 for n in notificaciones if n.enviada)
    print(f"\n✅ Exitosa: {exitosas}/{len(notificaciones)}")