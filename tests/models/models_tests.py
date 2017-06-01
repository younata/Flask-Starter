import flask_testing
from nose.tools import eq_

from application.models.database import db
from main import app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __init__(self, name: str):
        self.name = name


class ModelTests(flask_testing.TestCase):
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

    def test_it_works(self):
        eq_(len(User.query.all()), 0)
        subject = User("You")
        self.db.session.add(subject)
        self.db.session.commit()

        eq_(len(User.query.all()), 1)
        eq_(User.query.all()[0].name, "You")
