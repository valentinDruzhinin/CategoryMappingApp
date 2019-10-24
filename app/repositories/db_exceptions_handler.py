from functools import wraps
from logging import getLogger
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from werkzeug.exceptions import BadRequest
from app.repositories.exceptions import DataBaseError

logger = getLogger(__name__)


def db_exceptions_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        this = args[0]
        try:
            return func(*args, **kwargs)
        except IntegrityError as e:
            raise BadRequest(str(e))
        except SQLAlchemyError as e:
            logger.exception(e)
            if func.__name__ != 'query':
                this.db.session.rollback()
            raise DataBaseError()
    return wrapper
