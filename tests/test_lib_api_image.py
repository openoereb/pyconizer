# -*- coding: utf-8 -*-
import pytest
from pyconizer.lib.api.image import download_legend_icon
from pyconizer.lib.api.structure import Rule


@pytest.mark.parametrize('rule', [
    Rule()
])
def test_download_rule_without_url(rule):
    download_legend_icon(rule)
    assert rule.rule_url is None
