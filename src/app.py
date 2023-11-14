from flask import Flask
from config import config

#importamos cors para poder utilizar la api desde otra app como svelte
from flask_cors import CORS

#ruta
from routes import Movie
from routes import User

app = Flask(__name__)

#en localhost se debe colocar el puerto de por ejemplo svelte
CORS(app, resources={"*": {"origins": "http://127.0.0.1:5173"}})

def pageNotFound(error):
    return "<h1> Not found page <h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprint
    app.register_blueprint(Movie.main, url_prefix='/api/movies')
    app.register_blueprint(User.main, url_prefix = '/app')

    #Error handlers (manejadores de error)
    app.register_error_handler(404, pageNotFound)
    app.run()