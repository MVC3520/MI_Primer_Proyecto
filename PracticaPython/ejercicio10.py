class AgendaContactos:
    def __init__(self):
        self.contactos = []
    
    def __validar_telefono(self, telefono):
        """Valida que el teléfono tenga 10 dígitos numéricos"""
        if not telefono.isdigit():
            return False
        if len(telefono) != 10:
            return False
        return True
    
    def __validar_email(self, email):
        """Valida formato básico de email"""
        if "@" not in email:
            return False
        # Verificar que haya algo antes y después del @
        partes = email.split("@")
        if len(partes) != 2:
            return False
        if not partes[0] or not partes[1]:
            return False
        if "." not in partes[1]:
            return False
        return True
    
    def agregar_contacto(self, nombre, telefono, email):
        """Agrega un nuevo contacto con validación"""
        if not nombre or not telefono or not email:
            print("Error: Todos los campos son obligatorios")
            return False
        
        if not self.__validar_telefono(telefono):
            print(f"Error: Teléfono '{telefono}' debe tener 10 dígitos")
            return False
        
        if not self.__validar_email(email):
            print(f"Error: Email '{email}' no tiene formato válido")
            return False
        
        # Verificar si ya existe contacto con ese nombre
        if self.buscar_contacto(nombre):
            print(f"Error: Ya existe un contacto con nombre '{nombre}'")
            return False
        
        # Crear nuevo contacto
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email
        }
        self.contactos.append(contacto)
        print(f"Contacto '{nombre}' agregado exitosamente")
        return True
    
    def buscar_contacto(self, nombre):
        """Busca contacto por nombre (exacto)"""
        for contacto in self.contactos:
            if contacto["nombre"].lower() == nombre.lower():
                return contacto
        return None
    
    def eliminar_contacto(self, nombre):
        """Elimina contacto por nombre"""
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f"Contacto '{nombre}' eliminado exitosamente")
            return True
        else:
            print(f"Error: No se encontró contacto '{nombre}'")
            return False
    
    def mostrar_contactos(self):
        """Muestra todos los contactos ordenados alfabéticamente"""
        if not self.contactos:
            print("La agenda está vacía")
            return
        
        # Ordenar por nombre
        contactos_ordenados = sorted(self.contactos, key=lambda x: x["nombre"].lower())
        
        print("=== Lista de Contactos ===")
        for i, contacto in enumerate(contactos_ordenados, 1):
            print(f"{i}. {contacto['nombre']}: {contacto['telefono']} | {contacto['email']}")
        print(f"Total: {len(self.contactos)} contactos")
    
    def exportar_contactos(self):
        """Devuelve copia de la lista de contactos"""
        return self.contactos.copy()


# PRUEBAS
if __name__ == "__main__":
    agenda = AgendaContactos()
    
    # Agregar contactos válidos
    agenda.agregar_contacto("Ana López", "1122334455", "ana@email.com")
    agenda.agregar_contacto("Carlos Ruiz", "9988776655", "carlos@empresa.com")
    agenda.agregar_contacto("Beatriz García", "5544332211", "beatriz@gmail.com")
    
    # Intentar agregar contacto inválido
    agenda.agregar_contacto("Juan", "123", "juanemail")  # Teléfono y email inválidos
    agenda.agregar_contacto("Ana López", "1122334455", "ana2@email.com")  # Nombre duplicado
    
    # Mostrar todos los contactos
    agenda.mostrar_contactos()
    
    # Buscar contacto
    print("\nBuscando a Ana López:")
    resultado = agenda.buscar_contacto("Ana López")
    if resultado:
        print(f"Encontrado: {resultado}")
    
    # Buscar contacto inexistente
    print("\nBuscando a Pedro:")
    resultado = agenda.buscar_contacto("Pedro")
    print(f"Resultado: {resultado}")
    
    # Eliminar contacto
    agenda.eliminar_contacto("Carlos Ruiz")
    
    # Mostrar después de eliminar
    print("\nDespués de eliminar:")
    agenda.mostrar_contactos()
    
    # Exportar contactos
    print("\nContactos exportados:", agenda.exportar_contactos())
    
'''Explicación:

Estructura de datos: Lista de diccionarios para contactos

Validación: Métodos privados para validar teléfono y email

Funcionalidades CRUD: Crear, Leer, Actualizar (no implementado), Eliminar

Ordenamiento: Contactos mostrados alfabéticamente

Búsqueda insensible a mayúsculas: Usa lower() para comparar

Exportación: Método que devuelve copia para posible serialización

Características aprendidas:

Uso de diccionarios para estructuras complejas

Métodos privados con __

Validación de datos de entrada

Manejo de listas (ordenar, buscar, eliminar)

Interfaz clara para el usuario'''