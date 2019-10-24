from datetime import datetime
from app import db


class Category(db.Model):
    __tablename__ = 'Categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    date_of_creation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mapping = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'<Category id={self.id} name={self.name} mapping={self.mapping}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'dateOfCreation': self.date_of_creation,
            'mapping': self.mapping
        }
