class Desarrollador:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    def __str__(self):
        return f"👨‍💻 {self.nombre} ({self.especialidad})"

class Tarea:
    def __init__(self, descripcion, duracion_horas, desarrollador=None):
        self.descripcion = descripcion
        self.duracion_horas = duracion_horas
        self.desarrollador = desarrollador
        self.completada = False
    
    def asignar_desarrollador(self, desarrollador):
        self.desarrollador = desarrollador
        return f"✅ {desarrollador.nombre} asignado a '{self.descripcion}'"
    
    def marcar_completada(self):
        self.completada = True
        return f"✅ Tarea '{self.descripcion}' completada"
    
    def __str__(self):
        estado = "✅" if self.completada else "⏳"
        dev = f", Asignado a: {self.desarrollador.nombre}" if self.desarrollador else ""
        return f"{estado} {self.descripcion} ({self.duracion_horas}h{dev})"

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []  # Composición
    
    def agregar_tarea(self, descripcion, duracion_horas):
        tarea = Tarea(descripcion, duracion_horas)
        self.tareas.append(tarea)
        return f"✅ Tarea '{descripcion}' agregada al proyecto"
    
    def calcular_duracion_total(self):
        return sum(t.duracion_horas for t in self.tareas)
    
    def desarrolladores_involucrados(self):
        devs = set()
        for tarea in self.tareas:
            if tarea.desarrollador:
                devs.add(tarea.desarrollador)
        return list(devs)
    
    def mostrar_progreso(self):
        completadas = sum(1 for t in self.tareas if t.completada)
        total = len(self.tareas)
        porcentaje = (completadas / total * 100) if total > 0 else 0
        
        print(f"📊 PROYECTO: {self.nombre}")
        print(f"  Progreso: {completadas}/{total} tareas ({porcentaje:.1f}%)")
        print(f"  Duración total: {self.calcular_duracion_total()} horas")
        print(f"  Desarrolladores: {len(self.desarrolladores_involucrados())}")
        print("  Tareas:")
        for tarea in self.tareas:
            print(f"    {tarea}")

# Uso
if __name__ == "__main__":
    # Crear desarrolladores
    dev1 = Desarrollador("Ana", "Frontend")
    dev2 = Desarrollador("Carlos", "Backend")
    dev3 = Desarrollador("María", "BD")
    
    # Crear proyecto y tareas (composición)
    proyecto = Proyecto("Tienda Online")
    
    print(proyecto.agregar_tarea("Diseñar interfaz", 20))
    print(proyecto.agregar_tarea("Crear API REST", 30))
    print(proyecto.agregar_tarea("Modelar base de datos", 15))
    print(proyecto.agregar_tarea("Implementar carrito", 25))
    
    # Asignar desarrolladores a tareas
    print(proyecto.tareas[0].asignar_desarrollador(dev1))
    print(proyecto.tareas[1].asignar_desarrollador(dev2))
    print(proyecto.tareas[2].asignar_desarrollador(dev3))
    
    # Completar algunas tareas
    print(proyecto.tareas[0].marcar_completada())
    print(proyecto.tareas[2].marcar_completada())
    
    # Mostrar progreso
    proyecto.mostrar_progreso()
    
    # Listar desarrolladores
    print("\n👨‍💻 DESARROLLADORES INVOLUCRADOS:")
    for dev in proyecto.desarrolladores_involucrados():
        print(f"  {dev}")