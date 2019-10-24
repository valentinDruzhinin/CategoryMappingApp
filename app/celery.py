from celery import Celery
from app.config import Config

app = Celery(
    'tasks',
    broker=Config.CELERY_BROKER_URL,
    backend=Config.CELERY_RESULT_BACKEND,
    include=['app.tasks']
)
app.conf.update(Config().__dict__)

if __name__ == '__main__':
    app.start()
