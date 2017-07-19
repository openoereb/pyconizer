# -*- coding: utf-8 -*-
import pytest

from pyconizer.lib import encode_correctly


@pytest.mark.parametrize('string', [
    u'Hallo',
    u'DüDüDö',
    'Hallo',
    'DüDüDö'
])
def test_encode_correctly(string):
    assert isinstance(encode_correctly(string), str)
