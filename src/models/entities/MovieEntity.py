from src.utils.DateFormat import Dateformat

class MovieEntity():

    def __init__(self,id, titulo=None, duracion=None, lanzamiento=None):
        self.id = id
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

    def toJson(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'duracion': self.duracion,
            'lanzamiento': Dateformat.convertDate(self.lanzamiento)
        }