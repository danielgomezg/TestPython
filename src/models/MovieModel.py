from src.models.entities.MovieEntity import MovieEntity
from src.database.db import get_connection

class MovieModel():

    @classmethod
    def get_movies(cls):
        try:
            connection = get_connection()
            movies = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, titulo, duracion , lanzamiento FROM movie ORDER BY titulo ASC")
                results = cursor.fetchall()

                for row in results:
                    movie = MovieEntity(row[0], row[1], row[2], row[3])
                    movies.append(movie.toJson())
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_movie(cls, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, titulo, duracion , lanzamiento FROM movie WHERE id = %s",(id,))
                result = cursor.fetchone()

                movie = None
                if result != None:
                    movie = MovieEntity(result[0], result[1], result[2], result[3])
                    movie = movie.toJson()

            connection.close()
            return movie
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_movie(cls, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO movie (id, titulo, duracion , lanzamiento) 
                VALUES (%s, %s, %s, %s) """, (movie.id, movie.titulo, movie.duracion, movie.lanzamiento))
                filasAfectadas = cursor.rowcount
                connection.commit()

            connection.close()
            return filasAfectadas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_movie(cls, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE movie SET titulo = %s, duracion = %s , lanzamiento = %s 
                   WHERE id = %s """, (movie.titulo, movie.duracion, movie.lanzamiento, movie.id))
                filasAfectadas = cursor.rowcount
                connection.commit()

            connection.close()
            return filasAfectadas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_movie(cls, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM movie WHERE id=%s", (movie.id,))
                filasAfectadas = cursor.rowcount
                connection.commit()

            connection.close()
            return filasAfectadas
        except Exception as ex:
            raise Exception(ex)