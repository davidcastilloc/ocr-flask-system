from compumedic import create_app
from compumedic.extensions import db

app = create_app()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)

with app.app_context():
    db.create_all()