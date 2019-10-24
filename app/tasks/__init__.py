from typing import List, Dict
from app.celery import app as celery
from app import app
from app.models import Category


@celery.task(bind=True)
def category_batch_processing(self, category_batch: List[Dict]):
    """Background task for processing the batch of categories"""
    self.update_state(state='PROGRESS')
    categories = []
    for raw_category in category_batch:
        categories.append(Category(**raw_category))
    with app.app_context():
        app.categories.add_batch(categories)
