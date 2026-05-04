"""EJERCICIO 12:
Crea un sistema de nómina usando herencia y polimorfismo. Implementa una clase base Empleado con 
atributos nombre, id_empleado y un método calcular_salario(). Luego crea las clases EmpleadoTiempoCompleto
(con salario mensual y bono), EmpleadoMedioTiempo (con horas semanales y tarifa por hora) y 
EmpleadoPorProyecto (con proyectos completados y pago por proyecto), que hereden de Empleado y 
sobrescriban el método calcular_salario() según su fórmula específica. Además, cada clase debe tener 
un método trabajar() que describa su jornada laboral. Finalmente, demuestra el polimorfismo creando una 
lista con diferentes tipos de empleados, calculando la nómina total y mostrando información de cada 
empleado."""
#Lo que se enseña:
#Herencia con constructores diferentes
#Polimorfismo en métodos de cálculo
#Atributos específicos por clase

class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = 1000  # Salario base por defecto
    
    def calcular_salario(self):
        """Calcula el salario total - método base"""
        return self.salario_base
    
    def mostrar_datos(self):
        """Muestra información del empleado"""
        return f"{self.id_empleado} - {self.nombre}: ${self.calcular_salario():.2f}"
    
    def trabajar(self):
        """Método genérico para trabajar"""
        return f"{self.nombre} está trabajando"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id_empleado, salario_mensual, bono=0):
        super().__init__(nombre, id_empleado)
        self.salario_mensual = salario_mensual
        self.bono = bono
    
    def calcular_salario(self):
        """Sobrescribe cálculo de salario para tiempo completo"""
        return self.salario_mensual + self.bono
    
    def trabajar(self):
        """Sobrescribe método trabajar"""
        return f"{self.nombre} trabaja 40 horas semanales"

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, id_empleado, horas_semanales, tarifa_hora):
        super().__init__(nombre, id_empleado)
        self.horas_semanales = horas_semanales
        self.tarifa_hora = tarifa_hora
    
    def calcular_salario(self):
        """Sobrescribe cálculo para medio tiempo"""
        # 4 semanas por mes
        horas_mensuales = self.horas_semanales * 4
        return horas_mensuales * self.tarifa_hora
    
    def trabajar(self):
        """Sobrescribe método trabajar"""
        return f"{self.nombre} trabaja {self.horas_semanales} horas semanales"

class EmpleadoPorProyecto(Empleado):
    def __init__(self, nombre, id_empleado, proyectos_completados, pago_por_proyecto):
        super().__init__(nombre, id_empleado)
        self.proyectos_completados = proyectos_completados
        self.pago_por_proyecto = pago_por_proyecto
    
    def calcular_salario(self):
        """Sobrescribe cálculo por proyecto"""
        return self.proyectos_completados * self.pago_por_proyecto
    
    def agregar_proyecto(self, cantidad=1):
        """Método específico de esta clase"""
        self.proyectos_completados += cantidad
        return f"Proyectos actualizados: {self.proyectos_completados}"
    
    def trabajar(self):
        """Sobrescribe método trabajar"""
        return f"{self.nombre} completa proyectos: {self.proyectos_completados}"

# Uso
if __name__ == "__main__":
    print("=== SISTEMA DE NÓMINA ===")
    
    # Crear empleados de diferentes tipos
    empleados = [
        EmpleadoTiempoCompleto("Ana García", "EMP-001", 3000, 500),
        EmpleadoMedioTiempo("Carlos Ruiz", "EMP-002", 20, 25),
        EmpleadoPorProyecto("María López", "EMP-003", 5, 800),
        EmpleadoTiempoCompleto("Pedro Sánchez", "EMP-004", 3500, 300),
    ]
    
    # Mostrar información de cada empleado
    print("\n--- Información de Empleados ---")
    for emp in empleados:
        print(emp.mostrar_datos())
        print(f"  {emp.trabajar()}")
    
    # Cálculos polimórficos
    print("\n--- Cálculos de Nómina ---")
    
    # Calcular nómina total
    nomina_total = 0
    for emp in empleados:
        nomina_total += emp.calcular_salario()
    print(f"Nómina total mensual: ${nomina_total:.2f}")
    
    # Calcular promedio salarial
    promedio_salario = nomina_total / len(empleados)
    print(f"Salario promedio: ${promedio_salario:.2f}")
    
    # Encontrar empleado con mayor salario
    mayor_salario = 0
    empleado_mayor = None
    
    for emp in empleados:
        salario = emp.calcular_salario()
        if salario > mayor_salario:
            mayor_salario = salario
            empleado_mayor = emp
    
    if empleado_mayor:
        print(f"\nEmpleado con mayor salario: {empleado_mayor.nombre}")
        print(f"Salario: ${mayor_salario:.2f}")
        print(f"Tipo: {empleado_mayor.__class__.__name__}")
    
    # Ejecutar método específico si está disponible
    print("\n--- Métodos Específicos ---")
    for emp in empleados:
        if hasattr(emp, 'agregar_proyecto'):
            print(emp.agregar_proyecto(2))
