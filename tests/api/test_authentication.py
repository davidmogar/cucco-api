from flask import Flask
from flask_testing import TestCase

from app import create_app

class TestAuthentication(TestCase):

    def create_app(self):
        app = create_app('testing')
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False

        return app

    def _test_authentication(self, endpoint):
        response = self.client.get(endpoint)

        assert ('error' in response.json and
                    response.json['error'] == 'unauthorized'), \
                'should be unauthorized'

        response = self.client.get(endpoint,
                                   headers={'Authorization': '1234'})

        assert 'error' not in response.json, \
                'should be authorized'

    def test_accents_authentication(self):
        self._test_authentication('/private/accents?text=foo')

    def test_characters_authentication(self):
        self._test_authentication('/private/characters?text=foo')

    def test_emails_authentication(self):
        self._test_authentication('/private/emails?text=foo')

    def test_emojis_authentication(self):
        self._test_authentication('/private/emojis?text=foo')

    def test_hyphens_authentication(self):
        self._test_authentication('/private/hyphens?text=foo')

    def test_normalize_authentication(self):
        self._test_authentication('/private/normalize?text=foo')

    def test_punctuation_authentication(self):
        self._test_authentication('/private/punctuation?text=foo')

    def test_stopwords_authentication(self):
        self._test_authentication('/private/stopwords?text=foo')

    def test_symbols_authentication(self):
        self._test_authentication('/private/symbols?text=foo')

    def test_urls_authentication(self):
        self._test_authentication('/private/urls?text=foo')

    def test_whitespaces_authentication(self):
        self._test_authentication('/private/whitespaces?text=foo')
