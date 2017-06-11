from flask import Flask
from flask_testing import TestCase

from app import create_app

class TestCommon(TestCase):

    def create_app(self):
        return create_app('testing')

    def test_status_ok(self):
        response = self.client.get('/api/status')

        assert response.json == dict(status='ok'), \
                'status value should be "ok"'
