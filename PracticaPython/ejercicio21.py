#EJERCICIO 21: Biblioteca con Composición
#Crea un sistema de biblioteca usando composición. Implementa una clase Biblioteca que contenga una 
# lista de objetos Libro (relación de composición: los libros existen mientras exista la biblioteca). 
# La clase Libro debe tener título, autor y año. La Biblioteca debe tener métodos para agregar libros, 
# buscar libros por autor, y listar libros prestados. Los libros prestados deben marcarse con un 
# atributo prestado.

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = False
    
    def __str__(self):
        estado = "📖" if not self.prestado else "📚"
        return f"{estado} {self.titulo} - {self.autor} ({self.año})"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Composición: libros pertenecen a la biblioteca
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado a {self.nombre}"
    
    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
    
    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower() and not libro.prestado:
                libro.prestado = True
                return f"Libro '{titulo}' prestado"
        return f"No se puede prestar '{titulo}'"
    
    def libros_prestados(self):
        return [libro for libro in self.libros if libro.prestado]
    
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca")
            return
        print(f"📚 Biblioteca {self.nombre}:")
        for libro in self.libros:
            print(f"  {libro}")

# Uso
if __name__ == "__main__":
    biblioteca = Biblioteca("Central")
    
    # Agregar libros (composición)
    biblioteca.agregar_libro(Libro("El Quijote", "Cervantes", 1605))
    biblioteca.agregar_libro(Libro("Cien años de soledad", "García Márquez", 1967))
    biblioteca.agregar_libro(Libro("Rayuela", "Cortázar", 1963))
    
    biblioteca.mostrar_libros()
    
    # Prestar libro
    print(biblioteca.prestar_libro("El Quijote"))
    
    # Buscar por autor
    print("\nLibros de Cortázar:")
    for libro in biblioteca.buscar_por_autor("Cortázar"):
        print(f"  {libro}")
    
    # Listar prestados
    print("\nLibros prestados:")
    for libro in biblioteca.libros_prestados():
        print(f"  {libro}")