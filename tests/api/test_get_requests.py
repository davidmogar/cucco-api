from flask import Flask
from flask_testing import TestCase

from app import create_app

class TestGetRequests(TestCase):

    def create_app(self):
        return create_app('testing')

    def _test_call(self, valid_calls, invalid_calls):
        for valid_call in valid_calls:
            assert self.client.get(valid_call).status_code == 200, \
                    'status_code should be 200'

        for invalid_call in invalid_calls:
            assert self.client.get(invalid_call).status_code == 400, \
                    'status_code should be 400'

    def test_accents_get_request(self):
        self._test_call(['/api/v1/accents?text=foo'],
                        ['/api/v1/accents?'])

    def test_characters_get_request(self):
        self._test_call(
            [
                '/api/v1/characters?text=foo',
                '/api/v1/characters?text=foo&characters=foo',
                '/api/v1/characters?text=foo&replacement=bar',
                '/api/v1/characters?text=foo&characters=foo&replacement=bar'
            ],
            [
                '/api/v1/characters?',
                '/api/v1/characters?characters=foo'
                '/api/v1/characters?replacement=bar',
                '/api/v1/characters?characters=foo&replacement=bar'
            ]
        )

    def test_emails_get_request(self):
        self._test_call(
            [
                '/api/v1/emails?text=foo',
                '/api/v1/emails?text=foo&replacement=foo'
            ],
            [
                '/api/v1/emails?',
                '/api/v1/emails?replacement=foo'
            ]
        )

    def test_emojis_get_request(self):
        self._test_call(
            [
                '/api/v1/emojis?text=foo',
                '/api/v1/emojis?text=foo&replacement=foo'
            ],
            [
                '/api/v1/emojis?',
                '/api/v1/emojis?replacement=foo'
            ]
        )

    def test_hyphens_get_request(self):
        self._test_call(
            [
                '/api/v1/hyphens?text=foo',
                '/api/v1/hyphens?text=foo&replacement=foo'
            ],
            [
                '/api/v1/hyphens?',
                '/api/v1/hyphens?replacement=foo'
            ]
        )

    def test_normalize_get_request(self):
        self._test_call(['/api/v1/normalize?text=foo'],
                        ['/api/v1/normalize?'])

    def test_punctuation_get_request(self):
        self._test_call(
            [
                '/api/v1/punctuation?text=foo',
                '/api/v1/punctuation?text=foo&excluded=foo',
                '/api/v1/punctuation?text=foo&replacement=bar',
                '/api/v1/punctuation?text=foo&excluded=foo&replacement=bar'
            ],
            [
                '/api/v1/punctuation?',
                '/api/v1/punctuation?excluded=foo',
                '/api/v1/punctuation?replacement=bar',
                '/api/v1/punctuation?excluded=foo&replacement=bar'
            ]
        )

    def test_stopwords_get_request(self):
        self._test_call(
            [
                '/api/v1/stopwords?text=foo',
                '/api/v1/stopwords?text=foo&language=en',
                '/api/v1/stopwords?text=foo&ignore_case=true',
                '/api/v1/stopwords?text=foo&ignore_case=true&language=en'
            ],
            [
                '/api/v1/stopwords?',
                '/api/v1/stopwords?language=en'
            ]
        )

    def test_symbols_get_request(self):
        self._test_call(
            [
                '/api/v1/symbols?text=foo',
                '/api/v1/symbols?text=foo&form=NFKD',
                '/api/v1/symbols?text=foo&excluded=foo',
                '/api/v1/symbols?text=foo&replacement=bar',
                '/api/v1/symbols?text=foo&form=NFKD&excluded=foo&replacement=bar'
            ],
            [
                '/api/v1/symbols?',
                '/api/v1/symbols?form=NFKD',
                '/api/v1/symbols?excluded=foo',
                '/api/v1/symbols?replacement=bar',
                '/api/v1/symbols?form=NFKD&excluded=foo&replacement=bar'
            ]
        )

    def test_urls_get_request(self):
        self._test_call(
            [
                '/api/v1/urls?text=foo',
                '/api/v1/urls?text=foo&replacement=foo'
            ],
            [
                '/api/v1/urls?',
                '/api/v1/urls?replacement=foo'
            ]
        )

    def test_whitespaces_get_request(self):
        self._test_call(['/api/v1/whitespaces?text=foo'],
                        ['/api/v1/whitespaces?'])
