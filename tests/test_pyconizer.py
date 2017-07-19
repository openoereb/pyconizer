# -*- coding: utf-8 -*-
import os
from pyconizer import create_icons_from_scratch


def test_create_icons_from_scratch_json_only(test_path, test_config):

    path = os.path.abspath('{root}/json_only'.format(root=test_path))
    create_icons_from_scratch(test_config, path)
    assert os.path.isfile(os.path.abspath('{0}/mapping.json'.format(path)))
