from flask import Blueprint, jsonify, request
import uuid

#Entity
from src.models.entities.MovieEntity import MovieEntity

#models
from src.models.MovieModel import MovieModel

main = Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/add', methods=['POST'])
def add_movie():
    try:
        titulo = request.json['titulo']
        duracion = request.json['duracion']
        lanzamiento = request.json['lanzamiento']
        id = uuid.uuid4()
        #id es un objeto por lo que hay que transformalo en str
        movie = MovieEntity(str(id), titulo, duracion, lanzamiento)

        filasAfectadas = MovieModel.add_movie(movie)
        if filasAfectadas == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'Error al crear pelicula'}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        titulo = request.json['titulo']
        duracion = request.json['duracion']
        lanzamiento = request.json['lanzamiento']
        movie = MovieEntity(id, titulo, duracion, lanzamiento)

        filasAfectadas = MovieModel.update_movie(movie)
        if filasAfectadas == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'No se pudo editar pelicula'}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = MovieEntity(id)

        filasAfectadas = MovieModel.delete_movie(movie)
        if filasAfectadas == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'Pelicula no encontrada'}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500