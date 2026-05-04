"""8. Sistema de Inscripciones a Eventos

Crear clase Inscripcion que maneje fechas usando datetime.

REQUISITOS:

1. Atributos:
   - nombre_participante (str)
   - email (str)
   - fecha_inscripcion (datetime.date) → usar datetime para fecha actual
   - fecha_evento (datetime.date)

2. Validaciones con datetime:
   - La fecha de evento debe ser FUTURA (mayor a fecha actual)
   - La inscripción debe hacerse AL MENOS 3 días antes del evento

3. Métodos usando datetime:
   - dias_para_evento(): días faltantes (fecha_evento - fecha_actual)
   - es_inscripcion_valida(): True si cumple validaciones
   - cambiar_fecha_evento(nueva_fecha): validar que sea futura

4. Métodos de formato:
   - mostrar_info(): muestra datos con fechas formateadas

5. Método de clase:
   - crear_desde_formulario(nombre, email, fecha_evento_str): 
     recibe fecha como string "dd/mm/aaaa" y la convierte con strptime

EJEMPLO:
insc = Inscripcion("Ana", "ana@email.com", "15/12/2024")
print(insc.dias_para_evento())  # días faltantes
print(insc.es_inscripcion_valida())  # True si válida
print(insc.mostrar_info())"""

from datetime import date, datetime, timedelta

class Inscripcion:
    def __init__(self, nombre, email, fecha_evento_str):
        self.nombre = nombre
        self.email = email
        self.fecha_inscripcion = date.today()
        
        # Convertir string a fecha
        self.fecha_evento = datetime.strptime(fecha_evento_str, "%d/%m/%Y").date()
    
    def dias_para_evento(self):
        """Días faltantes para el evento"""
        return (self.fecha_evento - date.today()).days
    
    def es_valida(self):
        """True si se inscribe al menos 3 días antes"""
        return (self.fecha_evento - self.fecha_inscripcion).days >= 3
    
    def mostrar_info(self):
        print(f"{self.nombre} - Evento: {self.fecha_evento.strftime('%d/%m/%Y')}")
        print(f"Días faltantes: {self.dias_para_evento()}")
        print(f"Válida: {'Sí' if self.es_valida() else 'No'}")

# Uso rápido
fecha_futura = (date.today() + timedelta(days=10)).strftime("%d/%m/%Y")
insc = Inscripcion("Ana", "ana@email.com", fecha_futura)
insc.mostrar_info()
