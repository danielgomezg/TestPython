from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
class Developmentconfig(Config):
    DEBUG = True

config = {
    'development' : Developmentconfig
}