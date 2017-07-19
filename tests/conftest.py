# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def test_path():
    return '/tmp/iconizer/test'


@pytest.fixture
def test_config():
    return [
        {
            'url': 'https://wms.geo.admin.ch/?',
            'layer': 'ch.bav.kataster-belasteter-standorte-oev.oereb',
            'get_styles': {
                'request': 'GetStyles',
                'service': 'WMS',
                'srs': 'EPSG:2056',
                'version': '1.1.1'
            },
            'get_legend': {
                'image_format': 'image/png',
                'request': 'GetLegendGraphic',
                'service': 'WMS',
                'version': '1.1.1',
                'width': 72,
                'height': 36
            }
        }
    ]
