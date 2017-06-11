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
        self._test_call(['/api/public/accents?text=foo'],
                        ['/api/public/accents?'])

    def test_characters_get_request(self):
        self._test_call(
            [
                '/api/public/characters?text=foo',
                '/api/public/characters?text=foo&characters=foo',
                '/api/public/characters?text=foo&replacement=bar',
                '/api/public/characters?text=foo&characters=foo&replacement=bar'
            ],
            [
                '/api/public/characters?',
                '/api/public/characters?characters=foo'
                '/api/public/characters?replacement=bar',
                '/api/public/characters?characters=foo&replacement=bar'
            ]
        )

    def test_emails_get_request(self):
        self._test_call(
            [
                '/api/public/emails?text=foo',
                '/api/public/emails?text=foo&replacement=foo'
            ],
            [
                '/api/public/emails?',
                '/api/public/emails?replacement=foo'
            ]
        )

    def test_emojis_get_request(self):
        self._test_call(
            [
                '/api/public/emojis?text=foo',
                '/api/public/emojis?text=foo&replacement=foo'
            ],
            [
                '/api/public/emojis?',
                '/api/public/emojis?replacement=foo'
            ]
        )

    def test_hyphens_get_request(self):
        self._test_call(
            [
                '/api/public/hyphens?text=foo',
                '/api/public/hyphens?text=foo&replacement=foo'
            ],
            [
                '/api/public/hyphens?',
                '/api/public/hyphens?replacement=foo'
            ]
        )

    def test_normalize_get_request(self):
        self._test_call(['/api/public/normalize?text=foo'],
                        ['/api/public/normalize?'])

    def test_punctuation_get_request(self):
        self._test_call(
            [
                '/api/public/punctuation?text=foo',
                '/api/public/punctuation?text=foo&excluded=foo',
                '/api/public/punctuation?text=foo&replacement=bar',
                '/api/public/punctuation?text=foo&excluded=foo&replacement=bar'
            ],
            [
                '/api/public/punctuation?',
                '/api/public/punctuation?excluded=foo',
                '/api/public/punctuation?replacement=bar',
                '/api/public/punctuation?excluded=foo&replacement=bar'
            ]
        )

    def test_stopwords_get_request(self):
        self._test_call(
            [
                '/api/public/stopwords?text=foo',
                '/api/public/stopwords?text=foo&language=en',
                '/api/public/stopwords?text=foo&ignore_case=true',
                '/api/public/stopwords?text=foo&ignore_case=true&language=en'
            ],
            [
                '/api/public/stopwords?',
                '/api/public/stopwords?language=en'
            ]
        )

    def test_symbols_get_request(self):
        self._test_call(
            [
                '/api/public/symbols?text=foo',
                '/api/public/symbols?text=foo&form=NFKD',
                '/api/public/symbols?text=foo&excluded=foo',
                '/api/public/symbols?text=foo&replacement=bar',
                '/api/public/symbols?text=foo&form=NFKD&excluded=foo&replacement=bar'
            ],
            [
                '/api/public/symbols?',
                '/api/public/symbols?form=NFKD',
                '/api/public/symbols?excluded=foo',
                '/api/public/symbols?replacement=bar',
                '/api/public/symbols?form=NFKD&excluded=foo&replacement=bar'
            ]
        )

    def test_urls_get_request(self):
        self._test_call(
            [
                '/api/public/urls?text=foo',
                '/api/public/urls?text=foo&replacement=foo'
            ],
            [
                '/api/public/urls?',
                '/api/public/urls?replacement=foo'
            ]
        )

    def test_whitespaces_get_request(self):
        self._test_call(['/api/public/whitespaces?text=foo'],
                        ['/api/public/whitespaces?'])
