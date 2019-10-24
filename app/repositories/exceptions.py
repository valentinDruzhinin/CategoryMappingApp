from werkzeug.exceptions import InternalServerError


class DataBaseError(InternalServerError):
    description = 'Unable to process the operation'
