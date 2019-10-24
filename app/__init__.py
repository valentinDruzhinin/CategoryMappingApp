from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy(engine_options={'isolation_level': 'REPEATABLE_READ'})
app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)
Migrate(app, db)
app.db = db

from app.repositories.categories import CategoriesRepository
from app.routes import ROUTES
from app.exceptions_handler import register_exceptions_handler
from app.models import Category

app.categories = CategoriesRepository(db, Category)
register_exceptions_handler(app)
for route in ROUTES:
    app.route(route.url, **route.optional_params)(route.view)
