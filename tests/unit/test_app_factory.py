from unittest import TestCase
from unittest.mock import patch
from open_oauth import app_factory
from flask import Flask
from flask_restful import Api
from app import app, api


class TestAppFactory(TestCase):

    def test_create_app(self):
        self.assertEqual(
            isinstance(app_factory.create_app(), Flask),
            True
        )
    
    def test_create_api(self):
        self.assertEqual(
            isinstance(app, Flask),
            True
        )
        self.assertEqual(
            isinstance(api, Api),
            False
        )