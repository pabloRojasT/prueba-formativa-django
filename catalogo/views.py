from django.http import Http404
from django.shortcuts import render

juegos = [
    {'id': 1, 'nombre': 'The Legend of Zelda: Breath of the Wild', 'genero': 'Aventura', 'precio': 59.99},
    {'id': 2, 'nombre': 'Super Mario Odyssey', 'genero': 'Plataformas', 'precio': 49.99},
    {'id': 3, 'nombre': 'Horizon Zero Dawn', 'genero': 'Acción RPG', 'precio': 39.99},
    {'id': 4, 'nombre': 'Minecraft', 'genero': 'Sandbox', 'precio': 29.99},
    {'id': 5, 'nombre': 'FIFA 25', 'genero': 'Deportes', 'precio': 69.99},
]


def inicio(request):
    contexto = {
        'titulo': 'Catálogo de videojuegos',
        'juegos': juegos,
        'total': len(juegos),
    }
    return render(request, 'catalogo/inicio.html', contexto)


def detalle(request, id):
    videojuego = next((juego for juego in juegos if juego['id'] == id), None)

    if videojuego is None:
        raise Http404('El videojuego solicitado no existe.')

    contexto = {
        'titulo': 'Detalle del videojuego',
        'videojuego': videojuego,
    }
    return render(request, 'catalogo/detalle.html', contexto)
