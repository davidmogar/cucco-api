from flask import Flask
from unittest import TestCase

from app.common.utils import to_boolean

class TestUtils(TestCase):

    def test_to_boolean(self):
        assert to_boolean(True), 'result should be true'
        assert to_boolean('y'), 'result should be true'
        assert to_boolean('yes'), 'result should be true'
        assert to_boolean('t'), 'result should be true'
        assert to_boolean('true'), 'result should be true'
        assert to_boolean('True'), 'result should be true'
        assert to_boolean('on'), 'result should be true'
        assert to_boolean(None, True), 'result should be true'
        assert not to_boolean(False), 'result should be false'
        assert not to_boolean('n'), 'result should be false'
        assert not to_boolean('no'), 'result should be false'
        assert not to_boolean('f'), 'result should be false'
        assert not to_boolean('false'), 'result should be false'
        assert not to_boolean('False'), 'result should be false'
        assert not to_boolean('off'), 'result should be false'
        assert not to_boolean('0'), 'result should be false'
        assert not to_boolean(None, False), 'result should be true'
