#EJERCICIO 14: Animales y sonidos
#Crea un sistema de animales usando herencia y polimorfismo. Implementa una clase base Animal con 
# atributos nombre y edad, y un método hacer_sonido() que devuelva un string genérico. Luego crea las 
# clases Perro, Gato y Vaca que hereden de Animal y sobrescriban el método hacer_sonido() con sus sonidos 
# específicos: Perro "¡Guau guau!", Gato "¡Miau miau!", Vaca "¡Muuu!". Finalmente, demuestra el 
# polimorfismo creando una lista con diferentes animales y haciendo que cada uno emita su sonido 
# característico.

#Lo que se enseña:
#Polimorfismo simple
#Métodos que devuelven strings diferentes
#Herencia básica

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Hace algún sonido"
    
    def __str__(self):
        return self.nombre

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau miau!"

class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muuu!"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "¡Pío pío!"

# Uso del sistema
if __name__ == "__main__":
    print("=== SONIDOS DE ANIMALES ===\n")
    
    # Crear animales de diferentes tipos
    animales = [
        Perro("Fido"),
        Gato("Misi"),
        Vaca("Lola"),
        Pajaro("Piolín"),
        Perro("Rex")
    ]
    
    # Polimorfismo: todos hacen sonido diferente
    print("Sonidos de los animales:")
    for animal in animales:
        tipo = animal.__class__.__name__
        print(f"  {tipo} {animal.nombre}: {animal.hacer_sonido()}")
    
    # Demostración adicional de polimorfismo
    print("\n=== CORO DE ANIMALES ===")
    for i in range(3):
        print(f"\nRonda {i+1}:")
        for animal in animales:
            print(f"  {animal.hacer_sonido()}", end=" ")
    
    # Mostrar todos los animales
    print("\n\n=== LISTA DE ANIMALES ===")
    for i, animal in enumerate(animales, 1):
        print(f"{i}. {animal.__class__.__name__}: {animal.nombre}")

