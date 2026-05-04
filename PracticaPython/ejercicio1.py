#Clase Persona básica:Crear una clase Persona con atributos nombre, edad y dni.
# Implementar métodos 
# mostrar()
# para mostrar datos y es_mayor_de_edad() que devuelva True/False


class Persona:
    def __init__(self,nombre ,edad,dni ) -> None:
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    def mostrar(self) : 
        print(f'EL NOMBRE ES: {self.nombre}')  
        print(f'La edad es: {self.edad}')
        print(f'El dni es: {self.dni}')
    
    def es_mayor_de_edad(self):
        return self.edad>=18


#Crearinstancias
persona1=Persona("Juan Pérez",25,"12345678A")
persona2=Persona("María López",16,"87654321B")
#Usarmétodos
print("===Persona1===")
persona1.mostrar()
print(f"Es mayor de edad:{persona1.es_mayor_de_edad()}")
print("\n===Persona2===")
persona2.mostrar()
print(f"Es mayor de edad:{persona2.es_mayor_de_edad()}")
    