import flask_testing
from flask import Flask
from nose.tools import eq_

from application.controllers import main_controller


class MainControllerTests(flask_testing.TestCase):
    def create_app(self):
        app = Flask(__name__, template_folder="../../application/templates")
        app.register_blueprint(main_controller.blueprint)
        return app

    def setUp(self):
        self.test_app = self.app.test_client()

    def test_returns_welcome(self):
        result = self.test_app.get("/")

        eq_(result.status_code, 200)

        self.assert_template_used('page.html.jinja2')
        self.assert_context("context", {"title": "Welcome"})
