#EJERCICIO 20: Sistema educativo
#Crea un sistema educativo usando herencia y polimorfismo. Implementa una clase base Persona con 
# atributos nombre, edad y método presentarse(). Luego crea las clases Estudiante y Profesor que 
# hereden de Persona y sobrescriban el método presentarse(). Cada una debe tener métodos específicos: 
# estudiar(materia) para estudiantes y enseñar(materia) para profesores. Finalmente, demuestra el 
# polimorfismo creando una lista con diferentes personas y haciendo que cada una se presente y realice 
# su actividad específica de manera unificada.

#Lo que se enseña:
#Herencia de Persona a Estudiante y Profesor
#Polimorfismo en métodos de presentación
#Atributos específicos por rol

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años"
    
    def es_mayor(self):
        return self.edad >= 18

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.notas = []
    
    def presentarse(self):
        base = super().presentarse()
        return f"{base}, estudio {self.carrera}"
    
    def estudiar(self, materia):
        return f"📚 {self.nombre} estudia {materia}"
    
    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return f"Nota {nota} agregada"
        return "Nota inválida"
    
    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
        self.cursos = []
    
    def presentarse(self):
        base = super().presentarse()
        return f"{base}, enseño {self.materia}"
    
    def enseñar(self, tema):
        return f"👨‍🏫 Prof. {self.nombre} enseña {tema}"
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)
        return f"Curso '{curso}' agregado"

class Administrativo(Persona):
    def __init__(self, nombre, edad, area):
        super().__init__(nombre, edad)
        self.area = area
    
    def presentarse(self):
        base = super().presentarse()
        return f"{base}, trabajo en {self.area}"
    
    def trabajar(self):
        return f"📋 {self.nombre} realiza tareas administrativas"

# Uso del sistema
if __name__ == "__main__":
    print("=== SISTEMA EDUCATIVO SIMPLIFICADO ===\n")
    
    # Crear comunidad educativa
    comunidad = [
        Estudiante("Ana García", 20, "Ingeniería"),
        Estudiante("Carlos Ruiz", 22, "Medicina"),
        Profesor("Dr. Martínez", 45, "Matemáticas"),
        Profesor("Dra. López", 38, "Biología"),
        Administrativo("Sofía Ramírez", 32, "Admisiones"),
    ]
    
    # Agregar algunas notas
    comunidad[0].agregar_nota(9)
    comunidad[0].agregar_nota(8)
    comunidad[1].agregar_nota(7)
    comunidad[1].agregar_nota(6)
    
    # POLIMORFISMO: Todas se presentan de manera diferente
    print("🎤 PRESENTACIONES:")
    for persona in comunidad:
        print(f"  👤 {persona.presentarse()}")
    
    # Actividades específicas
    print("\n📚 ACTIVIDADES:")
    for persona in comunidad:
        if isinstance(persona, Estudiante):
            print(f"  {persona.estudiar('Programación')}")
        elif isinstance(persona, Profesor):
            print(f"  {persona.enseñar('su materia')}")
        elif isinstance(persona, Administrativo):
            print(f"  {persona.trabajar()}")
    
    # Información adicional
    print("\n📊 INFORMACIÓN ADICIONAL:")
    estudiantes = [p for p in comunidad if isinstance(p, Estudiante)]
    if estudiantes:
        promedios = [e.promedio() for e in estudiantes]
        promedio_total = sum(promedios) / len(promedios)
        print(f"  Estudiantes: {len(estudiantes)}")
        print(f"  Promedio general: {promedio_total:.2f}")
    
    profesores = [p for p in comunidad if isinstance(p, Profesor)]
    if profesores:
        print(f"  Profesores: {len(profesores)}")
        print(f"  Materias: {', '.join(p.materia for p in profesores)}")
    
    # Verificar mayoría de edad
    print("\n✅ VERIFICACIÓN MAYORÍA DE EDAD:")
    for persona in comunidad:
        mayor = "✅ Mayor" if persona.es_mayor() else "❌ Menor"
        print(f"  {persona.nombre}: {mayor}")
    
    # Resumen estadístico
    print("\n📈 RESUMEN ESTADÍSTICO:")
    total = len(comunidad)
    print(f"Total personas: {total}")
    print(f"Estudiantes: {len(estudiantes)} ({len(estudiantes)/total*100:.0f}%)")
    print(f"Profesores: {len(profesores)} ({len(profesores)/total*100:.0f}%)")
    print(f"Administrativos: {total - len(estudiantes) - len(profesores)}")