from compumedic import create_app
from compumedic.cache import cache
from compumedic.config import Config

app = create_app()


cache.init_app(app, config={
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_HOST": Config.REDIS_HOST,
    "CACHE_REDIS_DB": "0",
    "CACHE_REDIS_PORT": "6379",
    "CACHE_KEY_PREFIX": "compumedic",
    "CACHE_DEFAULT_TIMEOUT": 43200
})


if __name__ == "__main__":
    app.run(host=Config.FLASK_RUN_HOST)

with app.app_context():
    cache.clear()
    