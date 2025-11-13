from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MissingPerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    last_seen_location = db.Column(db.String(200))
    last_seen_date = db.Column(db.DateTime)
    photo_url = db.Column(db.String(300))
    status = db.Column(db.String(50), default='missing')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
