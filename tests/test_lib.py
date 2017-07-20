# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest


@pytest.mark.parametrize('string', [
    u'Hallo',
    u'DüDüDö',
    'Hallo',
    'DüDüDö'
])
def test_encode_correctly(string):
    assert isinstance(string, str)
