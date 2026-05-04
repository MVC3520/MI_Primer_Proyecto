class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []  # Agregación
        self.publicaciones = []  # Composición
    
    def agregar_amigo(self, amigo):
        if amigo not in self.amigos and amigo != self:
            self.amigos.append(amigo)
            return f"✅ {self.nombre} y {amigo.nombre} ahora son amigos"
        return "❌ Ya son amigos o es el mismo usuario"
    
    def publicar(self, contenido):
        publicacion = Publicacion(self, contenido)
        self.publicaciones.append(publicacion)
        return f"📝 {self.nombre} publicó: '{contenido[:30]}...'"
    
    def __str__(self):
        return f"👤 {self.nombre} ({len(self.amigos)} amigos, {len(self.publicaciones)} publicaciones)"

class Publicacion:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        self.comentarios = []  # Composición
    
    def comentar(self, usuario, texto):
        comentario = Comentario(usuario, texto)
        self.comentarios.append(comentario)
        return f"💬 {usuario.nombre} comentó en la publicación de {self.autor.nombre}"
    
    def __str__(self):
        return f"📰 {self.autor.nombre}: '{self.contenido[:50]}...' ({len(self.comentarios)} comentarios)"

class Comentario:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
    
    def __str__(self):
        return f"  💬 {self.autor.nombre}: {self.texto}"

# Uso
if __name__ == "__main__":
    # Crear usuarios
    ana = Usuario("Ana")
    carlos = Usuario("Carlos")
    maria = Usuario("María")
    
    # Agregar amigos (agregación)
    print(ana.agregar_amigo(carlos))
    print(ana.agregar_amigo(maria))
    
    # Publicar (composición)
    print(ana.publicar("¡Hoy es un día maravilloso para aprender POO!"))
    print(carlos.publicar("Acabo de terminar mi proyecto de Python"))
    
    # Comentar en publicaciones
    publicacion_ana = ana.publicaciones[0]
    print(publicacion_ana.comentar(carlos, "¡Totalmente de acuerdo!"))
    print(publicacion_ana.comentar(maria, "¿Qué estás aprendiendo?"))
    
    # Mostrar estado
    print(f"\n{ana}")
    print(f"{carlos}")
    print(f"{maria}")
    
    # Mostrar publicaciones con comentarios
    print("\n📰 FEED:")
    for usuario in [ana, carlos]:
        for pub in usuario.publicaciones:
            print(pub)
            for comentario in pub.comentarios:
                print(comentario)