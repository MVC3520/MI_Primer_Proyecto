#Estudiante con notas: 
# Clase Estudiante con nombre y lista de notas. 
# Métodos: agregar_nota(), promedio(), mejor_nota(), peor_nota().

class Estudiante:
    def __init__(self, nombre) -> None:
        self.nombre=nombre
        # ==============================================================
        # ¿POR QUÉ __notas ES PRIVADA (con doble guión bajo)?
        # 
        # 1. ENCAPSULAMIENTO: Protegemos los datos internos del objeto.
        #    - Evita que se modifiquen directamente desde fuera
        #    - Garantiza que solo se modifiquen a través de métodos controlados
        #
        # 2. VALIDACIÓN CONSISTENTE: Todas las notas pasan por agregar_nota()
        #    - Se valida que estén entre 0 y 20
        #    - No se pueden agregar notas inválidas como 100 o -5
        #
        # 3. INTEGRIDAD DEL OBJETO: El estado siempre es válido
        #    - No puede asignarse None, string u otros tipos
        #    - Los métodos como promedio() siempre funcionan
        #
        # 4. BUENA PRÁCTICA DE POO: "Ocultar la implementación"
        #    - El usuario no necesita saber cómo se almacenan las notas
        #    - Si cambiamos a diccionario o tupla, el código externo no se rompe
        #
        # Alternativas:
        #   - self._notas (protegido): convención, pero se puede acceder
        #   - self.notas (público): más simple para ejercicios básicos
        # ==============================================================
        self.__notas= []  # Lista privada de notas
        
    def agregar_nota(self, nota):
        """Agrega una nota a la lista (valida rango 0-20)"""
        # ==============================================================
        # VALIDACIÓN: Garantizamos que solo entren notas válidas
        # - Rango 0-20: típico en sistemas educativos
        # - Podríamos expandir: validar tipo (int/float), decimales, etc.
        # ==============================================================
        if 0 <= nota <= 20:
            self.__notas.append(nota)
            print(f"Nota {nota} agregada para {self.nombre}")
            return True
        else:
            print(f"Nota {nota} inválida. Debe estar entre 0 y 20")
            return False
    
    def promedio(self):
        """Calcula el promedio de notas"""
        # ==============================================================
        # IMPORTANTE: Verificar lista vacía evita ZeroDivisionError
        # Pythonic way: if not self.__notas (más legible que len() == 0)
        # ==============================================================
        if not self.__notas:
            return 0  # Evitar división por cero
        return sum(self.__notas) / len(self.__notas)
    
    def mejor_nota(self):
        """Devuelve la mejor nota"""
        # ==============================================================
        # FUNCIONES BUILT-IN: max() y min() trabajan con listas
        # Pero: ¡OJO CON LISTA VACÍA! max([]) da ValueError
        # ==============================================================
        if not self.__notas:
            return None # Mejor que 0 para distinguir "sin notas"
        return max(self.__notas)
    
    def peor_nota(self):
        """Devuelve la peor nota"""
        if not self.__notas:
            return None
        return min(self.__notas)
    
    def cantidad_notas(self):
        """Devuelve cantidad de notas"""
        # ==============================================================
        # ENCAPSULAMIENTO: Este método es opcional pero útil
        # Da acceso controlado a información sin exponer la lista
        # ==============================================================
        return len(self.__notas)
    
    def estado_academico(self):
        """Determina estado según promedio"""
        # ==============================================================
        # LÓGICA DE NEGOCIO: Separada de los cálculos matemáticos
        # Ventajas:
        # 1. Fácil de modificar (ej: cambiar rangos)
        # 2. Reutilizable en otros métodos
        # 3. Más legible que ifs anidados en mostrar_notas()
        # ==============================================================
        promedio = self.promedio()
        if promedio >= 16:
            return "Excelente"
        elif promedio >= 13:
            return "Bueno"
        elif promedio >= 10:
            return "Aprobado"
        else:
            return "Reprobado"
    
    def mostrar_notas(self):
        """Muestra todas las notas"""
        # ==============================================================
        # MÉTODO DE PRESENTACIÓN: Separa lógica de visualización
        # Podría cambiarse a GUI, web, PDF sin afectar otros métodos
        # ==============================================================
        if not self.__notas:
            print(f"{self.nombre} no tiene notas registradas")
        else:
            print(f"Notas de {self.nombre}: {self.__notas}")
            print(f"Cantidad: {self.cantidad_notas()}")
            print(f"Promedio: {self.promedio():.2f}")
            print(f"Mejor nota: {self.mejor_nota()}")
            print(f"Peor nota: {self.peor_nota()}")
            print(f"Estado: {self.estado_academico()}")

# Uso

estudiante = Estudiante("Ana García")

# Agregar notas
estudiante.agregar_nota(15)
estudiante.agregar_nota(18)
estudiante.agregar_nota(12)
estudiante.agregar_nota(20)
estudiante.agregar_nota(25)  # Inválida

# Mostrar información
estudiante.mostrar_notas()

# Métodos individuales
print(f"\nPromedio calculado: {estudiante.promedio():.2f}")
print(f"Estado: {estudiante.estado_academico()}")


## **PREGUNTAS PARA DEBATIR EN CLASE:**
"""
1. ¿Por qué es importante validar las notas en `agregar_nota()` y no en el constructor?
2. ¿Qué ventajas tiene devolver `None` en `mejor_nota()` cuando no hay notas vs devolver 0?
3. Si hacemos `self.notas` pública, ¿qué problemas podrían ocurrir?
4. ¿Cómo podríamos modificar la clase para permitir ver las notas pero no modificarlas directamente?
5. ¿Por qué `mostrar_notas()` es un método separado y no parte del constructor o `__str__`?

**¿Quieres que prepare más material didáctico así para otros ejercicios?**"""