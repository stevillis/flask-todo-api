from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# App config
app = Flask(__name__)
app.config.from_object("config")

# Database config
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# API config
api = Api(app)

from .models import todo_model
from .views import todo_view
