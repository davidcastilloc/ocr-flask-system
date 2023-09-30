from compumedic import create_app
from compumedic.cache import cache
from compumedic.extensions import db
from compumedic.config import Config
from compumedic.constants import CERT_PRIVATE_KEY, CERT_PEM
app = create_app()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

cache.init_app(app)
db.init_app(app)

if __name__ == "__main__":
    app.run(host=Config.HOST)

with app.app_context():
    cache.clear()
    db.create_all()
