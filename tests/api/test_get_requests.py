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
        self._test_call(['/v1/accents?text=foo'],
                        ['/v1/accents?'])

    def test_characters_get_request(self):
        self._test_call(
            [
                '/v1/characters?text=foo',
                '/v1/characters?text=foo&characters=foo',
                '/v1/characters?text=foo&replacement=bar',
                '/v1/characters?text=foo&characters=foo&replacement=bar'
            ],
            [
                '/v1/characters?',
                '/v1/characters?characters=foo'
                '/v1/characters?replacement=bar',
                '/v1/characters?characters=foo&replacement=bar'
            ]
        )

    def test_emails_get_request(self):
        self._test_call(
            [
                '/v1/emails?text=foo',
                '/v1/emails?text=foo&replacement=foo'
            ],
            [
                '/v1/emails?',
                '/v1/emails?replacement=foo'
            ]
        )

    def test_emojis_get_request(self):
        self._test_call(
            [
                '/v1/emojis?text=foo',
                '/v1/emojis?text=foo&replacement=foo'
            ],
            [
                '/v1/emojis?',
                '/v1/emojis?replacement=foo'
            ]
        )

    def test_hyphens_get_request(self):
        self._test_call(
            [
                '/v1/hyphens?text=foo',
                '/v1/hyphens?text=foo&replacement=foo'
            ],
            [
                '/v1/hyphens?',
                '/v1/hyphens?replacement=foo'
            ]
        )

    def test_normalize_get_request(self):
        self._test_call(['/v1/normalize?text=foo'],
                        ['/v1/normalize?'])

    def test_punctuation_get_request(self):
        self._test_call(
            [
                '/v1/punctuation?text=foo',
                '/v1/punctuation?text=foo&excluded=foo',
                '/v1/punctuation?text=foo&replacement=bar',
                '/v1/punctuation?text=foo&excluded=foo&replacement=bar'
            ],
            [
                '/v1/punctuation?',
                '/v1/punctuation?excluded=foo',
                '/v1/punctuation?replacement=bar',
                '/v1/punctuation?excluded=foo&replacement=bar'
            ]
        )

    def test_stopwords_get_request(self):
        self._test_call(
            [
                '/v1/stopwords?text=foo',
                '/v1/stopwords?text=foo&language=en',
                '/v1/stopwords?text=foo&ignore_case=true',
                '/v1/stopwords?text=foo&ignore_case=true&language=en'
            ],
            [
                '/v1/stopwords?',
                '/v1/stopwords?language=en'
            ]
        )

    def test_symbols_get_request(self):
        self._test_call(
            [
                '/v1/symbols?text=foo',
                '/v1/symbols?text=foo&form=NFKD',
                '/v1/symbols?text=foo&excluded=foo',
                '/v1/symbols?text=foo&replacement=bar',
                '/v1/symbols?text=foo&form=NFKD&excluded=foo&replacement=bar'
            ],
            [
                '/v1/symbols?',
                '/v1/symbols?form=NFKD',
                '/v1/symbols?excluded=foo',
                '/v1/symbols?replacement=bar',
                '/v1/symbols?form=NFKD&excluded=foo&replacement=bar'
            ]
        )

    def test_urls_get_request(self):
        self._test_call(
            [
                '/v1/urls?text=foo',
                '/v1/urls?text=foo&replacement=foo'
            ],
            [
                '/v1/urls?',
                '/v1/urls?replacement=foo'
            ]
        )

    def test_whitespaces_get_request(self):
        self._test_call(['/v1/whitespaces?text=foo'],
                        ['/v1/whitespaces?'])
