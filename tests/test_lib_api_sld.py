# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from pyconizer.lib.api.sld import FactoryFromString, extract_rules


def test_factory_from_string_wrong_sld_version(read_test_factory_from_string_wrong_sld_version):
    with pytest.raises(LookupError):
        FactoryFromString(
            read_test_factory_from_string_wrong_sld_version
        )


def test_extract_rules_no_filter_but_name(read_test_extract_rules_no_filter_but_name):
    layers = extract_rules(
        read_test_extract_rules_no_filter_but_name
    )
    assert len(layers[0].rules) == 6


def test_extract_rules_no_name_but_filter(read_test_extract_rules_no_name_but_filter):
    layers = extract_rules(
        read_test_extract_rules_no_name_but_filter
    )
    assert len(layers[0].rules) == 6


def test_extract_rules_no_encoding(read_test_extract_rules_no_encoding):
    layers = extract_rules(
        read_test_extract_rules_no_encoding
    )
    assert len(layers[0].rules) == 6
