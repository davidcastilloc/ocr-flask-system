from flask import Flask
from flask_caching import Cache

from .config import Config

app = Flask(__name__, template_folder="templates")
cache = Cache()
cache.init_app(app, {
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_HOST": "redis",
    "CACHE_REDIS_DB": "0",
    "CACHE_REDIS_PORT": "6379",
    "CACHE_KEY_PREFIX": "compumedic",
    "CACHE_DEFAULT_TIMEOUT": 43200
})


def create_app():
    from compumedic.routes.IndexRoutes import main as main_blueprint
    from compumedic.routes.CompareFeatureRoutes import compare as compare_blueprint
    from compumedic.routes.ProcessRecipe import upload as upload_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(compare_blueprint, url_prefix='/compare')
    app.register_blueprint(upload_blueprint, url_prefix='/upload')
    return app
