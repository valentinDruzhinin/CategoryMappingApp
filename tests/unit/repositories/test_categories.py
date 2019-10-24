import pytest
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from app import CategoriesRepository
from tests.unit.mocks import DB, Category


class TestCategoriesRepository:

    def setup(self):
        self.db = DB()
        self.repo = CategoriesRepository(self.db, Category)

    def test_add_new_category(self):
        category = Category()
        self.repo.add(category)

        self.db.session.add.assert_called_with(category)
        self.db.session.commit.assert_called()

    def test_add_existing_category(self):
        category = Category()
        self.db.session.commit.side_effect = IntegrityError(statement='test', params={}, orig=[])

        with pytest.raises(BadRequest):
            self.repo.add(category)

    def test_add_batch_new_unique_categories(self):
        categories = [Category()]
        self.repo.add_batch(categories)

        self.db.session.add.assert_called_with(categories[0])
        self.db.session.commit.assert_called()

    def test_add_batch_existing_categories(self):
        categories = [Category()]
        self.db.session.commit.side_effect = IntegrityError(statement='test', params={}, orig=[])

        with pytest.raises(BadRequest):
            self.repo.add_batch(categories)

    def test_delete_category(self):
        category = Category(id=1)
        actual_category = self.repo.delete(category)

        Category.query.filter_by.assert_called_with(id=1)
        self.db.session.commit.assert_called()
        assert category == actual_category

    def test_update_existing_category(self):
        category = Category(id=1)
        actual_category = self.repo.update(category)

        self.db.session.query.assert_called_with(Category)
        self.db.session.commit.assert_called()
        assert category.id == actual_category.id

    def test_query(self):
        actual_result =self.repo.query(id=1)

        Category.query.filter_by.assert_called_with(id=1)
        assert [] == actual_result
