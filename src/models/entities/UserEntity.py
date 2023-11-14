from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class UserEntity(UserMixin):

    def __init__(self, id, username, password, fullname = "") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    #password puede ser 123; hashed_password clave transformada
    @classmethod
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def generate_password(cls, password):
        return generate_password_hash(password)

