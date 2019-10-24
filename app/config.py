import os


class Config:
    DB_NAME = os.getenv('DB_NAME', 'category-mapping')
    DB_USER = os.getenv('DB_USER', 'admin')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'pass')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
