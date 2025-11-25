from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# create single shared instances for the entire app
db = SQLAlchemy()
bcrypt = Bcrypt()
