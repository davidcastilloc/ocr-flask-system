from compumedic import create_app
from compumedic.cache import cache
from compumedic.extensions import db

app = create_app()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_HOST'] = 'redis'
app.config['CACHE_REDIS_PORT'] = '6379'
app.config['CACHE_REDIS_DB'] = '0'
app.config['CACHE_KEY_PREFIX'] = 'compumedic'

cache.init_app(app)
db.init_app(app)

if __name__ == "__main__":
    app.run()

with app.app_context():
    cache.clear()
    db.create_all()
