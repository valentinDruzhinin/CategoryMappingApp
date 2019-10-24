from werkzeug.exceptions import BadRequest
from app.repositories.db_exceptions_handler import db_exceptions_handler


class CategoriesRepository:
    """Wrapper for Categories repository to prevent work with SqlAlchemy"""
    def __init__(self, db, model_type):
        self.db = db
        self.model_type = model_type

    @db_exceptions_handler
    def add(self, model):
        self.db.session.add(model)
        self.db.session.commit()
        return model

    @db_exceptions_handler
    def add_batch(self, models):
        for model in models:
            self.db.session.add(model)
        self.db.session.commit()
        return models

    @db_exceptions_handler
    def delete(self, model):
        self.model_type.query.filter_by(id=model.id).delete()
        self.db.session.commit()
        return model

    @db_exceptions_handler
    def update(self, model):
        db_model = self.db.session.query(self.model_type).get(model.id)
        if not db_model:
            raise BadRequest(f'Unable to find Category with id={model.id}')
        for key, value in model.to_dict().items():
            if value is not None:
                setattr(db_model, key, value)
        self.db.session.commit()
        return db_model

    @db_exceptions_handler
    def query(self, **args):
        return list(self.model_type.query.filter_by(**args))

    def __repr__(self):
        return f'<CategoriesRepository db={self.db}>'
