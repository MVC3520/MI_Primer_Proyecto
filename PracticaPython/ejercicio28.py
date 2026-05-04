class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.pacientes = []
    
    def __str__(self):
        return f"👨‍⚕️ Dr. {self.nombre} ({self.especialidad}) - {len(self.pacientes)} pacientes"

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"👤 {self.nombre} ({self.edad} años)"

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []  # Composición
        self.pacientes = []  # Composición
    
    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)
        return f"✅ Dr. {doctor.nombre} agregado a {self.nombre}"
    
    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        return f"✅ Paciente {paciente.nombre} ingresado en {self.nombre}"
    
    def asignar_paciente_doctor(self, paciente_nombre, doctor_nombre):
        for paciente in self.pacientes:
            if paciente.nombre == paciente_nombre:
                for doctor in self.doctores:
                    if doctor.nombre == doctor_nombre:
                        doctor.pacientes.append(paciente)
                        return f"✅ {paciente.nombre} asignado a Dr. {doctor.nombre}"
        return "❌ No se pudo asignar"
    
    def contar_pacientes(self):
        return len(self.pacientes)
    
    def __str__(self):
        return f"🏥 {self.nombre}: {len(self.doctores)} doctores, {len(self.pacientes)} pacientes"

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []  # Composición
    
    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)
        return f"✅ Departamento {departamento.nombre} agregado"
    
    def mostrar_estructura(self):
        print(f"🏥 HOSPITAL: {self.nombre}")
        for depto in self.departamentos:
            print(f"\n  {depto}")
            print("  Doctores:")
            for doctor in depto.doctores:
                print(f"    {doctor}")
            print("  Pacientes:")
            for paciente in depto.pacientes:
                print(f"    {paciente}")

# Uso
if __name__ == "__main__":
    # Crear hospital y departamentos (composición)
    hospital = Hospital("Central")
    
    # Crear departamentos
    cardiologia = Departamento("Cardiología")
    pediatria = Departamento("Pediatría")
    
    # Agregar doctores (composición)
    print(cardiologia.agregar_doctor(Doctor("García", "Cardiólogo")))
    print(pediatria.agregar_doctor(Doctor("López", "Pediatra")))
    
    # Agregar pacientes (composición)
    print(cardiologia.agregar_paciente(Paciente("Juan Pérez", 65)))
    print(pediatria.agregar_paciente(Paciente("Ana Gómez", 8)))
    
    # Asignar pacientes a doctores
    print(cardiologia.asignar_paciente_doctor("Juan Pérez", "García"))
    
    # Agregar departamentos al hospital
    print(hospital.agregar_departamento(cardiologia))
    print(hospital.agregar_departamento(pediatria))
    
    # Mostrar estructura
    hospital.mostrar_estructura()
    
    # Estadísticas
    print(f"\n📊 Total pacientes: {sum(d.contar_pacientes() for d in hospital.departamentos)}")