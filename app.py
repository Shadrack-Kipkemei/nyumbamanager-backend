from flask import Flask
from config import Config
from extensions import db, migrate, jwt, bcrypt, cors


# Import models for migration detection
from models.user import User
from models.property import Property
from models.unit import Unit
from models.tenant import Tenant
from models.payment import Payment


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)