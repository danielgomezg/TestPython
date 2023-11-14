from flask import Flask, request, jsonify, Blueprint, session
from flask_login import LoginManager, login_user, logout_user, login_required
import uuid

#ntity
from src.models.entities.UserEntity import UserEntity

#model
from src.models.UserModel import UserModel

main = Blueprint('user_blueprint', __name__)

login_manager = LoginManager(main)

@login_manager.user_loader
def load_user(id):
    return UserModel.getById(id)

# @main.route('/login', methods=['GET','POST'])
# def login():
#     try:
#         print("inicio metodo login")
#         username = request.json['username']
#         password = request.json['password']
#         print("username: " + username + " password: " + password)
#         user = UserEntity(0, username, password)
#         loggedUser = UserModel.login(user)
#         if loggedUser != None:
#             if loggedUser.password:
#                 login_user(loggedUser)
#                 return loggedUser
#             else:
#                 return jsonify({'message':'Contraseña invalida'}), 404
#         else:
#             return jsonify({'message': 'Nombre de usuario invalido'}), 404
#     except Exception as ex:
#         return jsonify({'message': str(ex)}), 500

@main.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        user = UserEntity(0, username, password)
        loggedUser = UserModel.login(user)
        if loggedUser != None:
            if loggedUser.password:
                #print(loggedUser.password)
                #print("id: " + loggedUser.id)
                #login_user(loggedUser)
                session.clear()
                session['user_id'] = loggedUser.id
                return jsonify({ 'id': loggedUser.id,
                                 'username' : loggedUser.username,
                                 'password': password,
                                 'fullname': loggedUser.fullname})
            else:
                #return jsonify({'message':'Contraseña invalida'}), 404
                # le saque el 404 para mostrar mensaje en el front
                return jsonify({'message': 'Contraseña invalida'}), 404
        else:
            return jsonify({'message': 'Nombre de usuario invalido'}),404
    else:
        return jsonify({'message': 'No se ha podido iniciar sesión'}), 404

@main.route('/add', methods=['POST'])
def add_user():
    try:
        username = request.json['username']
        password = request.json['password']
        fullname = request.json['fullname']
        id = uuid.uuid4()
        passHash = UserEntity.generate_password(password)
        print(passHash)
        #id es un objeto por lo que hay que transformalo en str
        user = UserEntity(str(id), username, passHash, fullname)

        filasAfectadas = UserModel.add_user(user)
        print(filasAfectadas)
        if filasAfectadas == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': 'Error al crear usuario'}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/update/<id>', methods=['PUT'])
def update_user(id):
    try:
        username = request.json['username']
        password = request.json['password']
        fullname = request.json['fullname']
        passHash = UserEntity.generate_password(password)
        user = UserEntity(id, username, passHash, fullname)

        filasAfectadas = UserModel.update_user(user)
        if filasAfectadas == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': 'No se pudo editar usuario'}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/logout')
def logOut():
    return logout_user()



