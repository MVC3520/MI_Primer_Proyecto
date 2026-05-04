#EJERCICIO 18: Documentos y formatos
#Crea un sistema de conversión de documentos usando herencia y polimorfismo. Implementa una clase base 
# Documento con atributos titulo, contenido y tamaño, y un método exportar(formato) que convierta el 
# documento a diferentes formatos. Luego crea clases específicas para cada tipo de documento 
# (PDFDocumento, WordDocumento, HTMLDocumento) que hereden de Documento y tengan métodos adicionales 
# específicos de su formato. Incluye un método de clase convertir() que pueda convertir entre formatos. 
# Finalmente, demuestra el polimorfismo creando un sistema donde un mismo contenido pueda exportarse a 
# múltiples formatos.

#Característica nueva: Métodos de clase para conversión entre formatos.

#Lo que se enseña:
#Polimorfismo en exportación de documentos
#Atributos específicos por formato
#Métodos con diferentes comportamientos

class Documento:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
        self.tamaño = len(contenido)  # en caracteres
    
    def exportar(self, formato):
        """Exporta el documento a un formato específico"""
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
    def info(self):
        return f"📄 '{self.titulo}' ({self.tamaño} chars)"
    
    @classmethod
    def convertir(cls, documento_origen, formato_destino):
        """Convierte un documento a otro formato (método de clase)"""
        # Diccionario de conversiones soportadas
        conversiones = {
            ('PDF', 'Word'): "Convirtiendo PDF a Word (preservando formato)",
            ('Word', 'PDF'): "Convirtiendo Word a PDF (manteniendo diseño)",
            ('HTML', 'PDF'): "Convirtiendo HTML a PDF (con estilos CSS)",
            ('HTML', 'Word'): "Convirtiendo HTML a Word (extraendo contenido)",
            ('Word', 'HTML'): "Convirtiendo Word a HTML (generando código)",
        }
        
        origen = documento_origen.__class__.__name__.replace('Documento', '')
        clave = (origen, formato_destino)
        
        if clave in conversiones:
            return f"✅ {conversiones[clave]}"
        else:
            return f"❌ Conversión {origen} → {formato_destino} no soportada"

class PDFDocumento(Documento):
    def __init__(self, titulo, contenido, protegido=False):
        super().__init__(titulo, contenido)
        self.protegido = protegido
        self.paginas = (len(contenido) // 1000) + 1
    
    def exportar(self, formato="PDF"):
        if self.protegido:
            return f"🔒 PDF protegido: '{self.titulo}' ({self.paginas} páginas) - No se puede exportar"
        return f"📄 PDF exportado: '{self.titulo}' ({self.paginas} páginas)"
    
    def proteger(self, contraseña=""):
        self.protegido = True
        return f"🔒 PDF protegido {'con contraseña' if contraseña else ''}"

class WordDocumento(Documento):
    def __init__(self, titulo, contenido, version="docx"):
        super().__init__(titulo, contenido)
        self.version = version
        self.palabras = len(contenido.split())
    
    def exportar(self, formato="Word"):
        return f"📝 Word (.{self.version}) exportado: '{self.titulo}' ({self.palabras} palabras)"
    
    def revisar_ortografia(self):
        # Simulación simple
        errores = self.contenido.count('error')  # Busca la palabra 'error'
        return f"✏️ Revisión ortográfica: {errores} errores encontrados"

class HTMLDocumento(Documento):
    def __init__(self, titulo, contenido, estilos="estilos.css"):
        super().__init__(titulo, contenido)
        self.estilos = estilos
        self.lineas = contenido.count('\n') + 1
    
    def exportar(self, formato="HTML"):
        return f"🌐 HTML exportado: '{self.titulo}' ({self.lineas} líneas, CSS: {self.estilos})"
    
    def generar_html(self):
        return f"""<!DOCTYPE html>
<html>
<head><title>{self.titulo}</title><link rel="stylesheet" href="{self.estilos}"></head>
<body><h1>{self.titulo}</h1><p>{self.contenido[:100]}...</p></body>
</html>"""

# Uso del sistema
if __name__ == "__main__":
    print("=== SISTEMA DE CONVERSIÓN DE DOCUMENTOS ===\n")
    
    # Crear documentos en diferentes formatos
    contenido = "Este es un documento de ejemplo con contenido para demostrar la conversión entre formatos."
    
    documentos = [
        PDFDocumento("Reporte Financiero", contenido * 20),
        WordDocumento("Tesis Doctoral", contenido * 15, "docx"),
        HTMLDocumento("Mi Sitio Web", contenido, "estilos.css"),
    ]
    
    # Proteger el PDF
    documentos[0].proteger("secreto123")
    
    # Mostrar información de documentos
    print("Documentos creados:")
    for doc in documentos:
        print(f"  {doc.info()}")
    
    # Exportar documentos (polimorfismo)
    print("\nExportando documentos:")
    for doc in documentos:
        print(f"  {doc.exportar()}")
    
    # Métodos específicos
    print("\nOperaciones específicas:")
    print(f"  {documentos[1].revisar_ortografia()}")
    print(f"  {documentos[2].generar_html()[:100]}...")
    
    # DEMOSTRACIÓN DE LA NUEVA FUNCIONALIDAD: CONVERSIÓN
    print("\n" + "="*50)
    print("CONVERSIÓN ENTRE FORMATOS (métodos de clase)")
    print("="*50)
    
    # Crear un documento de prueba
    doc_prueba = WordDocumento("Documento de prueba", "Contenido para conversión")
    
    # Intentar diferentes conversiones
    conversiones = [
        ("Word", "PDF"),
        ("PDF", "Word"),
        ("HTML", "PDF"),
        ("Word", "HTML"),
        ("PDF", "HTML"),  # No soportada
    ]
    
    for origen, destino in conversiones:
        resultado = Documento.convertir(doc_prueba, destino)
        print(f"  {origen} → {destino}: {resultado}")
    
    # Mostrar qué conversiones son posibles
    print("\nResumen de conversiones soportadas:")
    print("  ✓ Word → PDF, HTML")
    print("  ✓ PDF → Word")
    print("  ✓ HTML → PDF, Word")
    print("  ✗ Otras combinaciones no están implementadas")
    
    # Estadísticas finales
    print("\n" + "="*50)
    print("ESTADÍSTICAS FINALES")
    print("="*50)
    
    total_caracteres = sum(doc.tamaño for doc in documentos)
    print(f"Total documentos: {len(documentos)}")
    print(f"Total caracteres: {total_caracteres}")
    
    # Por tipo de documento
    tipos = {}
    for doc in documentos:
        tipo = doc.__class__.__name__.replace('Documento', '')
        tipos[tipo] = tipos.get(tipo, 0) + 1
    
    print("\nDistribución por tipo:")
    for tipo, cantidad in tipos.items():
        print(f"  {tipo}: {cantidad}")