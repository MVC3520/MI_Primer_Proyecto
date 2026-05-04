"""
6. Libro con atributos estáticos:
   Clase Libro con título, autor, año. 
   Atributo de clase contador_libros que lleve la cuenta de libros creados.
   ISBN único auto-generado basado en contador_libros (ej: "LIB-0001").
   Método mostrar_info() que muestre todos los datos del libro.
   
   Ejemplo de uso:
   libro1 = Libro("Cien años de soledad", "García Márquez", 1967)
   libro2 = Libro("1984", "George Orwell", 1949)
   print(libro1.isbn)  # "LIB-0001"
   print(libro2.isbn)  # "LIB-0002"
   print(Libro.contador_libros)  # 2
"""
class Libro:
    # Atributo de clase (estático)
    contador_libros = 0
    
    def __init__(self, titulo, autor, año):
        """
        Constructor de la clase Libro.
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            año (int): Año de publicación
        """
        self.titulo = titulo
        self.autor = autor
        self.año = año
        
        # Incrementar el contador de libros (atributo de clase)
        Libro.contador_libros += 1
        
        # Generar ISBN único basado en el contador
        # :04d significa: 4 dígitos con ceros a la izquierda
        self.isbn = f"LIB-{Libro.contador_libros:04d}"
    
    def mostrar_info(self):
        """
        Muestra toda la información del libro.
        """
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año}")
    
    def obtener_info(self):
        """
        Devuelve la información como string (alternativa a mostrar_info).
        Útil si queremos usar la información sin imprimirla.
        """
        return f"ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Año: {self.año}"

# Ejemplo de uso
if __name__ == "__main__":
    print("=== CREACIÓN DE LIBROS ===\n")
    
    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("1984", "George Orwell", 1949)
    libro3 = Libro("El código Da Vinci", "Dan Brown", 2003)
    
    # Mostrar información de cada libro
    print("--- Información del Libro 1 ---")
    libro1.mostrar_info()
    
    print("\n--- Información del Libro 2 ---")
    libro2.mostrar_info()
    
    print("\n--- Información del Libro 3 ---")
    libro3.mostrar_info()
    
    # Acceder directamente a los atributos
    print("\n=== ACCESO DIRECTO A ATRIBUTOS ===")
    print(f"ISBN libro1: {libro1.isbn}")
    print(f"ISBN libro2: {libro2.isbn}")
    print(f"ISBN libro3: {libro3.isbn}")
    
    # Mostrar contador de libros (atributo de clase)
    print(f"\nTotal de libros creados: {Libro.contador_libros}")
    
    # Demostrar que el contador es de clase, no de instancia
    print("\n=== DEMOSTRACIÓN ATRIBUTO DE CLASE ===")
    print(f"Libro.contador_libros: {Libro.contador_libros}")
    print(f"libro1.contador_libros: {libro1.contador_libros} (accediendo desde instancia)")
    print(f"libro2.contador_libros: {libro2.contador_libros} (mismo valor para todas)")
    
    # Crear un libro más para demostrar que el contador sigue incrementando
    print("\n=== CREANDO UN LIBRO ADICIONAL ===")
    libro4 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997)
    libro4.mostrar_info()
    print(f"Total libros actualizado: {Libro.contador_libros}")