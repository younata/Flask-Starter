import flask_testing
from nose.tools import eq_

from application.models.database import db
from main import app
from tests.helpers.helpers import contains_


class AppTests(flask_testing.TestCase):
    def create_app(self):
        return app

    def setUp(self):
        self.db = db
        self.app = app.test_client()
        self.db.init_app(app)

        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_index_returns_data(self):
        result = self.app.get("/")
        eq_(result.status_code, 200)

        received_string = result.data.decode("utf-8")
        contains_(received_string, "Welcome")
