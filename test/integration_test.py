import unittest
from flask import Flask, url_for
from flask_testing import TestCase

from app import app


class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_homepage(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)
        self.assertIn(b'Devops Engineer', response.data)


if __name__ == '__main__':
    unittest.main()
