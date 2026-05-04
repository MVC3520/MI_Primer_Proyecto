class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"👨‍🎓 {self.nombre} ({self.edad} años)"

class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # Agregación
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        return f"Estudiante {estudiante.nombre} agregado a {self.nombre}"
    
    def contar_estudiantes(self):
        return len(self.estudiantes)

class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carreras = []  # Agregación
    
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)
        return f"Carrera {carrera.nombre} agregada a {self.nombre}"
    
    def contar_estudiantes(self):
        return sum(c.contar_estudiantes() for c in self.carreras)

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.facultades = []  # Agregación
    
    def agregar_facultad(self, facultad):
        self.facultades.append(facultad)
        return f"Facultad {facultad.nombre} agregada a {self.nombre}"
    
    def mostrar_estructura(self):
        print(f"🏛️  Universidad: {self.nombre}")
        for facultad in self.facultades:
            print(f"  📚 Facultad: {facultad.nombre}")
            for carrera in facultad.carreras:
                print(f"    🎓 Carrera: {carrera.nombre} - {carrera.contar_estudiantes()} estudiantes")
                for estudiante in carrera.estudiantes:
                    print(f"      {estudiante}")

# Uso
if __name__ == "__main__":
    # Crear estudiantes independientes (agregación)
    est1 = Estudiante("Ana García", 20)
    est2 = Estudiante("Carlos Ruiz", 22)
    est3 = Estudiante("María López", 21)
    
    # Crear carreras y agregar estudiantes
    ing = Carrera("Ingeniería")
    med = Carrera("Medicina")
    ing.agregar_estudiante(est1)
    ing.agregar_estudiante(est2)
    med.agregar_estudiante(est3)
    
    # Crear facultades
    exactas = Facultad("Ciencias Exactas")
    salud = Facultad("Ciencias de la Salud")
    exactas.agregar_carrera(ing)
    salud.agregar_carrera(med)
    
    # Crear universidad
    uni = Universidad("Nacional")
    uni.agregar_facultad(exactas)
    uni.agregar_facultad(salud)
    
    # Mostrar estructura
    uni.mostrar_estructura()
    
    # Contar estudiantes por facultad
    print(f"\nEstudiantes en Ciencias Exactas: {exactas.contar_estudiantes()}")
    print(f"Estudiantes en Ciencias de la Salud: {salud.contar_estudiantes()}")
    print(f"Total en la universidad: {exactas.contar_estudiantes() + salud.contar_estudiantes()}")