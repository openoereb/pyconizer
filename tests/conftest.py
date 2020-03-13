# -*- coding: utf-8 -*
import sys
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


@pytest.fixture
def test_path_qgis_server():
    return '/tmp/iconizer/test_qgis_server'


@pytest.fixture
def test_config_qgis_server():
    return [
        {
            'url': 'http://wms.geo.gr.ch/nutzungsplanung?',
            'layer': 'GGP Gestaltungsbereiche',
            'get_styles': {
                'request': 'GetStyles',
                'service': 'WMS',
                'srs': 'EPSG:2056',
                'version': '1.3.0'
            },
            'get_legend': {
                'image_format': 'image/png',
                'request': 'GetLegendGraphic',
                'service': 'WMS',
                'version': '1.3.0',
                'width': 72,
                'height': 36
            }
        }
    ]


@pytest.fixture
def read_test_factory_from_string_wrong_sld_version():
    if sys.version_info.major > 2:
        f = open('tests/resources/test_factory_from_string_wrong_sld_version.xml', encoding='utf-8')
    else:
        f = open('tests/resources/test_factory_from_string_wrong_sld_version.xml')
    c = f.read()
    f.close()
    return c


@pytest.fixture
def read_test_extract_rules_no_filter_but_name():
    if sys.version_info.major > 2:
        f = open('tests/resources/test_extract_rules_no_filter_but_name.xml', encoding='utf-8')
    else:
        f = open('tests/resources/test_extract_rules_no_filter_but_name.xml')
    c = f.read()
    f.close()
    return c


@pytest.fixture
def read_test_extract_rules_no_name_but_filter():
    if sys.version_info.major > 2:
        f = open('tests/resources/test_extract_rules_no_name_but_filter.xml', encoding='utf-8')
    else:
        f = open('tests/resources/test_extract_rules_no_name_but_filter.xml')
    c = f.read()
    f.close()
    return c


@pytest.fixture
def read_test_extract_rules_no_encoding():
    if sys.version_info.major > 2:
        f = open('tests/resources/test_extract_rules_no_encoding.xml', encoding='utf-8')
    else:
        f = open('tests/resources/test_extract_rules_no_encoding.xml')
    c = f.read()
    f.close()
    return c
