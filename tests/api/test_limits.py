from flask import Flask
from flask_testing import TestCase

from app import create_app

class TestLimits(TestCase):

    def create_app(self):
        return create_app('testing')

    def _test_rate_limit(self, endpoint, limit):
        for _ in range(limit):
            response = self.client.get(endpoint)

            assert 'error' not in response.json, \
                    'limit should not have been reached'

        response = self.client.get(endpoint)

        assert ('error' in response.json and
                    response.json['error'] == 'ratelimit exceeded'), \
                'limit should have been reached'

    def test_accents_limit(self):
        self._test_rate_limit('/api/public/accents?text=foo', 30)

    def test_characters_limit(self):
        self._test_rate_limit('/api/public/characters?text=foo', 30)

    def test_emails_limit(self):
        self._test_rate_limit('/api/public/emails?text=foo', 30)

    def test_emojis_limit(self):
        self._test_rate_limit('/api/public/emojis?text=foo', 30)

    def test_hyphens_limit(self):
        self._test_rate_limit('/api/public/hyphens?text=foo', 30)

    def test_normalize_limit(self):
        self._test_rate_limit('/api/public/normalize?text=foo', 10)

    def test_punctuation_limit(self):
        self._test_rate_limit('/api/public/punctuation?text=foo', 30)

    def test_stopwords_limit(self):
        self._test_rate_limit('/api/public/stopwords?text=foo', 10)

    def test_symbols_limit(self):
        self._test_rate_limit('/api/public/symbols?text=foo', 30)

    def test_urls_limit(self):
        self._test_rate_limit('/api/public/urls?text=foo', 30)

    def test_whitespaces_limit(self):
        self._test_rate_limit('/api/public/whitespaces?text=foo', 30)
