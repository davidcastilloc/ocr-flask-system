from decouple import config


class Config():
    HOST = config('FLASK_RUN_HOST')
    REDIS_HOST= config('REDIS_HOST')


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig
}
