from src.database.db import get_connection
from src.models.entities.UserEntity import UserEntity

class UserModel:

    @classmethod
    def login(cls, user):

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id, username, password, fullname FROM usuario
                WHERE username = %s""", (user.username,))
                filasAfectadas = cursor.fetchone()
                if filasAfectadas != None:
                    print("filas afectadas: " + filasAfectadas[0])
                    passCorrecto = UserEntity.check_password(filasAfectadas[2], user.password)
                    print(passCorrecto)
                    #print("id: " + filasAfectadas[0])
                    user = UserEntity(filasAfectadas[0], filasAfectadas[1], passCorrecto, filasAfectadas[3])
                    return user
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getById(cls, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, fullname FROM usuario WHERE id = %s",(id,))
                result = cursor.fetchone()

                #user = None
                if result != None:
                    user = UserEntity(result[0], result[1], None, result[2])
                    #user = user.toJson()
                else:
                    return None
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(cls, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario (id, username, password, fullname) 
                    VALUES (%s, %s, %s, %s) """, (user.id, user.username, user.password, user.fullname))
                filasAfectadas = cursor.rowcount
                connection.commit()

            connection.close()
            return filasAfectadas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(cls, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE usuario SET username = %s, password = %s , fullname = %s 
                       WHERE id = %s """, (user.username, user.password, user.fullname, user.id))
                filasAfectadas = cursor.rowcount
                connection.commit()

            connection.close()
            return filasAfectadas
        except Exception as ex:
            raise Exception(ex)