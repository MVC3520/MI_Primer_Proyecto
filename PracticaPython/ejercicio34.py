from abc import ABC, abstractmethod

# Interfaz base
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @abstractmethod
    def presentarse(self):
        pass
    
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

# Interfaces específicas
class EstudianteInterface(ABC):
    @abstractmethod
    def estudiar(self, materia):
        pass
    
    @abstractmethod
    def tomar_examen(self):
        pass

class TrabajadorInterface(ABC):
    @abstractmethod
    def trabajar(self, horas):
        pass
    
    @abstractmethod
    def cobrar_salario(self):
        pass

# Implementaciones concretas
class Estudiante(Persona, EstudianteInterface):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.horas_estudio = 0
    
    def presentarse(self):
        return f"👨‍🎓 Soy {self.nombre}, estudio {self.carrera}"
    
    def estudiar(self, materia):
        self.horas_estudio += 2
        return f"📚 {self.nombre} estudia {materia} (+2 horas)"
    
    def tomar_examen(self):
        return f"✏️ {self.nombre} toma un examen de {self.carrera}"
    
    def get_horas_estudio(self):
        return self.horas_estudio

class Trabajador(Persona, TrabajadorInterface):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto
        self.horas_trabajo = 0
        self.salario_acumulado = 0
    
    def presentarse(self):
        return f"👨‍💼 Soy {self.nombre}, trabajo como {self.puesto}"
    
    def trabajar(self, horas):
        self.horas_trabajo += horas
        return f"💼 {self.nombre} trabaja {horas} horas como {self.puesto}"
    
    def cobrar_salario(self):
        pago = self.horas_trabajo * 50  # $50 por hora
        self.salario_acumulado += pago
        self.horas_trabajo = 0  # Resetear horas
        return f"💰 {self.nombre} cobra ${pago:.2f} (Total: ${self.salario_acumulado:.2f})"
    
    def get_horas_trabajo(self):
        return self.horas_trabajo

# Herencia múltiple - VERSIÓN CORREGIDA
class Asistente(Estudiante, Trabajador):
    def __init__(self, nombre, edad, carrera, puesto):
        # Solución: NO usar super(), llamar a cada constructor directamente
        Persona.__init__(self, nombre, edad)  # Llamar al constructor base
        # Inicializar atributos de ambas clases
        self.carrera = carrera
        self.puesto = puesto
        self.horas_estudio = 0
        self.horas_trabajo = 0
        self.salario_acumulado = 0
        self.rol = "Asistente"
    
    def presentarse(self):
        return f"👨‍🏫 Soy {self.nombre}, estudio {self.carrera} y trabajo como {self.puesto}"
    
    # Reimplementar métodos que necesitan acceso a atributos específicos
    def estudiar(self, materia):
        self.horas_estudio += 2
        return f"📚 {self.nombre} estudia {materia} como asistente (+2 horas)"
    
    def trabajar(self, horas):
        self.horas_trabajo += horas
        return f"💼 {self.nombre} trabaja {horas} horas como {self.puesto}"
    
    def cobrar_salario(self):
        pago = self.horas_trabajo * 50
        self.salario_acumulado += pago
        self.horas_trabajo = 0
        return f"💰 {self.nombre} cobra ${pago:.2f} (Total: ${self.salario_acumulado:.2f})"
    
    def calcular_carga_total(self):
        return self.horas_estudio + self.horas_trabajo
    
    def tiene_permiso(self, accion):
        permisos = {
            "estudiar": True,
            "trabajar": True,
            "cobrar": True,
            "examen": True,
            "investigar": True
        }
        return permisos.get(accion, False)
    
    def mostrar_estado(self):
        print(f"👨‍🏫 {self.nombre} - {self.rol}")
        print(f"  📚 Horas estudio: {self.horas_estudio}")
        print(f"  💼 Horas trabajo: {self.horas_trabajo}")
        print(f"  📊 Carga total: {self.calcular_carga_total()} horas")
        print(f"  💰 Salario acumulado: ${self.salario_acumulado:.2f}")

# Sistema de gestión
class SistemaEducativo:
    def __init__(self):
        self.personas = []
    
    def agregar_persona(self, persona):
        self.personas.append(persona)
        return f"✅ {persona.nombre} agregado al sistema"
    
    def mostrar_todos(self):
        print("👥 SISTEMA EDUCATIVO:")
        for persona in self.personas:
            print(f"  {persona.presentarse()}")
            # Determinar tipo
            tipos = []
            if isinstance(persona, Estudiante):
                tipos.append("Estudiante")
            if isinstance(persona, Trabajador):
                tipos.append("Trabajador")
            if isinstance(persona, Asistente):
                tipos.append("Asistente (Herencia múltiple)")
            print(f"    Tipo: {', '.join(tipos)}")

# Uso
if __name__ == "__main__":
    # Crear sistema
    sistema = SistemaEducativo()
    
    # Crear personas de diferentes tipos
    estudiante = Estudiante("Ana García", 20, "Ingeniería")
    trabajador = Trabajador("Carlos Ruiz", 35, "Administrativo")
    asistente = Asistente("María López", 25, "Medicina", "Ayudante de Cátedra")
    
    # Agregar al sistema
    print(sistema.agregar_persona(estudiante))
    print(sistema.agregar_persona(trabajador))
    print(sistema.agregar_persona(asistente))
    
    # Mostrar todos
    sistema.mostrar_todos()
    
    # Acciones específicas
    print("\n📚 ACTIVIDADES:")
    print(estudiante.estudiar("Matemáticas"))
    print(trabajador.trabajar(8))
    print(asistente.estudiar("Anatomía"))
    print(asistente.trabajar(4))
    
    # Cobrar salarios
    print("\n💰 FINANZAS:")
    print(trabajador.cobrar_salario())
    print(asistente.cobrar_salario())
    
    # Verificar que Asistente tiene métodos de ambas clases
    print("\n🎯 ASISTENTE HEREDA DE AMBAS CLASES:")
    print(f"  De Estudiante: {asistente.tomar_examen()}")
    print(f"  De Trabajador: {asistente.trabajar(2)}")
    print(f"  Propio: {asistente.presentarse()}")
    
    # Estado del asistente
    print("\n📊 ESTADO DEL ASISTENTE:")
    asistente.mostrar_estado()
    
    # Verificar permisos
    print("\n🔐 PERMISOS DEL ASISTENTE:")
    for accion in ["estudiar", "trabajar", "cobrar", "examen", "investigar", "admin"]:
        permiso = "✅" if asistente.tiene_permiso(accion) else "❌"
        print(f"  {accion}: {permiso}")
    
    # Demostrar MRO (Method Resolution Order)
    print("\n🔍 MRO (Method Resolution Order) de Asistente:")
    for i, clase in enumerate(Asistente.__mro__):
        print(f"  {i+1}. {clase.__name__}")