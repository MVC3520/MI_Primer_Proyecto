class Calculadora:
    def __init__(self):
        self.__historial = []  # Atributo privado
        
    def sumar(self, a, b):
        resultado = a + b
        self.__guardar_operacion(f"{a} + {b} = {resultado}")
        return resultado
    
    def restar(self, a, b):
        resultado = a - b
        self.__guardar_operacion(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a, b):
        resultado = a * b
        self.__guardar_operacion(f"{a} × {b} = {resultado}")
        return resultado
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        resultado = a / b
        self.__guardar_operacion(f"{a} ÷ {b} = {resultado}")
        return resultado
    
    def __guardar_operacion(self, operacion):
        """Método privado para guardar operación en historial"""
        self.__historial.append(operacion)
        # Mantener solo las últimas 5 operaciones
        if len(self.__historial) > 5:
            self.__historial.pop(0)
    
    def mostrar_historial(self):
        """Muestra todas las operaciones guardadas"""
        if not self.__historial:
            print("Historial vacío")
            return
        
        print("=== Historial de Operaciones (últimas 5) ===")
        for i, op in enumerate(self.__historial, 1):
            print(f"{i}. {op}")
    
    def limpiar_historial(self):
        """Limpia todo el historial"""
        self.__historial.clear()
        print("Historial limpiado")


# PRUEBAS
if __name__ == "__main__":
    calc = Calculadora()
    
    # Realizar operaciones
    print("Resultado suma:", calc.sumar(5, 3))          # 8
    print("Resultado resta:", calc.restar(10, 4))       # 6
    print("Resultado multiplicación:", calc.multiplicar(3, 7))  # 21
    
    try:
        print("Resultado división:", calc.dividir(15, 3))  # 5.0
        print("Resultado división:", calc.dividir(8, 2))   # 4.0
    except ValueError as e:
        print(f"Error: {e}")
    
    # Agregar más operaciones para probar límite de 5
    calc.sumar(100, 50)
    calc.sumar(200, 300)
    
    # Mostrar historial (solo las últimas 5)
    calc.mostrar_historial()
    
    # Probar división por cero
    try:
        calc.dividir(10, 0)
    except ValueError as e:
        print(f"Error esperado: {e}")
        
'''Explicación:

Encapsulamiento: El historial es privado (__historial) con método privado __guardar_operacion

Lógica de negocio: Cada operación guarda en formato string y limita a 5 elementos

Validación: División por cero lanza excepción

Interfaz pública: Métodos claros para operaciones y ver historial'''