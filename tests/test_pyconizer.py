# -*- coding: utf-8 -*-
import os
from pyconizer import create_icons_from_scratch


def test_create_icons_from_scratch_json_only(test_path, test_config):
    path = os.path.abspath('{root}/json_only'.format(root=test_path))
    create_icons_from_scratch(test_config, path)
    assert os.path.isfile(os.path.abspath('{0}/mapping.json'.format(path)))


def test_create_icons_from_scratch_json_and_icons(test_path, test_config):
    path = os.path.abspath('{root}/json_and_icons'.format(root=test_path))
    create_icons_from_scratch(test_config, path, json_only=False)
    assert os.path.isfile(os.path.abspath('{0}/mapping.json'.format(path)))
    assert os.path.isdir(os.path.abspath('{0}/ch.bav.kataster-belasteter-standorte-oev.oereb'.format(path)))
