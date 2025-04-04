from flask import Flask
from .config import Config
from .extensions import db, migrate
from .resources import user_bp, book_bp, category_bp


def create_app(config_object=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if config_object:
        app.config.from_mapping(config_object)
    else:
        app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    blueprints = [user_bp, book_bp, category_bp]
    for bp in blueprints:
        app.register_blueprint(bp)


    with app.app_context():
        from models import User, Book, Order, OrderStatus, OrderItem, Category
        db.create_all()

    return app

