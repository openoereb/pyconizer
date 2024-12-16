# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import base64
import filetype
import os
import datetime
import time

from pyconizer import create_icons_from_scratch, update_icon_content_by_layer_name, \
    delete_from_structure_by_layer_name, get_icon
from pyconizer.lib.api.structure import read


def test_create_icons_from_scratch_json_only(test_path, test_config):
    path = os.path.abspath('{root}/json_only'.format(root=test_path))
    create_icons_from_scratch(test_config, path)
    assert os.path.isfile(os.path.abspath('{0}/mapping.json'.format(path)))


def test_create_icons_from_scratch_json_and_images(test_path, test_config):
    path = os.path.abspath('{root}/json_and_images'.format(root=test_path))
    create_icons_from_scratch(test_config, path, images=True)
    assert os.path.isfile(os.path.abspath('{0}/mapping.json'.format(path)))
    assert os.path.isdir(os.path.abspath('{0}/ch.bav.kataster-belasteter-standorte-oev.oereb'.format(path)))


def test_create_icons_from_scratch_json_and_images_and_svgs(test_path, test_config):
    path = os.path.abspath('{root}/json_and_images_and_svgs'.format(root=test_path))
    create_icons_from_scratch(test_config, path, images=True, svgs=True)
    assert os.path.isfile(os.path.abspath('{0}/mapping.json'.format(path)))
    assert os.path.isdir(os.path.abspath('{0}/ch.bav.kataster-belasteter-standorte-oev.oereb'.format(path)))


def test_update_icon_content_json_only(test_path, test_config):
    path = os.path.abspath('{root}/update_json_only'.format(root=test_path))
    create_icons_from_scratch(test_config, path)
    old_time = os.path.getmtime(os.path.abspath('{0}/mapping.json'.format(path)))
    time.sleep(0.1)
    update_icon_content_by_layer_name(path, 'ch.bav.kataster-belasteter-standorte-oev.oereb')
    new_time = os.path.getmtime(os.path.abspath('{0}/mapping.json'.format(path)))
    assert datetime.datetime.fromtimestamp(old_time) < datetime.datetime.fromtimestamp(new_time)


def test_update_icon_content_json_only_incorrect_layer_name(test_path, test_config):
    path = os.path.abspath('{root}/update_json_only_incorrect_layer_name'.format(root=test_path))
    create_icons_from_scratch(test_config, path)
    old_time = os.path.getmtime(os.path.abspath('{0}/mapping.json'.format(path)))
    update_icon_content_by_layer_name(path, 'incorrect_layer_name')
    new_time = os.path.getmtime(os.path.abspath('{0}/mapping.json'.format(path)))
    assert datetime.datetime.fromtimestamp(old_time) == datetime.datetime.fromtimestamp(new_time)


def test_update_icon_content_json_and_images(test_path, test_config):
    path = os.path.abspath('{root}/update_json_and_images'.format(root=test_path))
    create_icons_from_scratch(test_config, path, images=True)
    old_time_json = os.path.getmtime(os.path.abspath('{0}/mapping.json'.format(path)))
    root_path = os.path.abspath('{0}/ch.bav.kataster-belasteter-standorte-oev.oereb'.format(path))
    files = [
        os.path.join(
            dp,
            f
        ) for dp, dn, filenames in os.walk(root_path) for f in filenames if os.path.splitext(f)[1] == '.txt']
    old_icon_times = []
    for file in files:
        old_icon_times.append(os.path.getmtime(file))
    time.sleep(0.1)
    update_icon_content_by_layer_name(path, 'ch.bav.kataster-belasteter-standorte-oev.oereb', images=True)
    new_time_json = os.path.getmtime(os.path.abspath('{0}/mapping.json'.format(path)))
    assert datetime.datetime.fromtimestamp(old_time_json) < datetime.datetime.fromtimestamp(new_time_json)
    files = [
        os.path.join(
            dp,
            f
        ) for dp, dn, filenames in os.walk(root_path) for f in filenames if os.path.splitext(f)[1] == '.txt']
    new_icon_times = []
    for file in files:
        new_icon_times.append(os.path.getmtime(file))
    for index, old_time in old_icon_times:
        assert datetime.datetime.fromtimestamp(old_time) < datetime.datetime.fromtimestamp(
            new_icon_times[index]
        )


def test_update_icon_content_json_and_images_and_svgs(test_path, test_config):
    path = os.path.abspath('{root}/update_json_and_images_and_svgs'.format(root=test_path))
    create_icons_from_scratch(test_config, path, images=True, svgs=True)
    old_time_json = os.path.getmtime(os.path.abspath('{0}/mapping.json'.format(path)))
    root_path = os.path.abspath('{0}/ch.bav.kataster-belasteter-standorte-oev.oereb'.format(path))
    files = [
        os.path.join(
            dp,
            f
        ) for dp, dn, filenames in os.walk(root_path) for f in filenames if os.path.splitext(f)[1] == '.txt']
    old_icon_times = []
    for file in files:
        old_icon_times.append(os.path.getmtime(file))
    time.sleep(0.1)
    update_icon_content_by_layer_name(path, 'ch.bav.kataster-belasteter-standorte-oev.oereb', images=True,
                                      svgs=True)
    new_time_json = os.path.getmtime(os.path.abspath('{0}/mapping.json'.format(path)))
    assert datetime.datetime.fromtimestamp(old_time_json) < datetime.datetime.fromtimestamp(new_time_json)
    files = [
        os.path.join(
            dp,
            f
        ) for dp, dn, filenames in os.walk(root_path) for f in filenames if os.path.splitext(f)[1] == '.txt']
    new_icon_times = []
    for file in files:
        new_icon_times.append(os.path.getmtime(file))
    for index, old_time in old_icon_times:
        assert datetime.datetime.fromtimestamp(old_time) < datetime.datetime.fromtimestamp(
            new_icon_times[index]
        )


def test_delete_from_structure_by_layer_name_json_only(test_path, test_config):
    path = os.path.abspath('{root}/delete_json_only'.format(root=test_path))
    create_icons_from_scratch(test_config, path)
    delete_from_structure_by_layer_name(path, 'ch.bav.kataster-belasteter-standorte-oev.oereb')
    config = read(os.path.abspath('{0}/mapping.json'.format(path)))
    assert len(config.layers) == 0


def test_delete_from_structure_by_incorrect_layer_name_json_only(test_path, test_config):
    path = os.path.abspath('{root}/delete_json_only_incorrect_layer_name'.format(root=test_path))
    create_icons_from_scratch(test_config, path)
    delete_from_structure_by_layer_name(path, 'incorrect_layer_name')
    config = read(os.path.abspath('{0}/mapping.json'.format(path)))
    assert len(config.layers) == 1


def test_delete_from_structure_by_layer_name_json_and_images(test_path, test_config):
    path = os.path.abspath('{root}/delete_json_and_images'.format(root=test_path))
    create_icons_from_scratch(test_config, path, images=True)
    delete_from_structure_by_layer_name(
        path, 'ch.bav.kataster-belasteter-standorte-oev.oereb', images=True
    )
    config = read(os.path.abspath('{0}/mapping.json'.format(path)))
    assert len(config.layers) == 0
    assert not os.path.isdir(
        os.path.abspath('{0}/ch.bav.kataster-belasteter-standorte-oev.oereb'.format(path))
    )


def test_delete_from_structure_by_incorrect_layer_name_json_and_images(test_path, test_config):
    path = os.path.abspath('{root}/delete_json_and_images_incorrect_layer_name'.format(root=test_path))
    create_icons_from_scratch(test_config, path, images=True)
    delete_from_structure_by_layer_name(
        path, 'incorrect_layer_name', images=True
    )
    config = read(os.path.abspath('{0}/mapping.json'.format(path)))
    assert len(config.layers) == 1
    assert os.path.isdir(
        os.path.abspath('{0}/ch.bav.kataster-belasteter-standorte-oev.oereb'.format(path))
    )


def test_get_icon(test_path, test_config):
    path = os.path.abspath('{root}/get_icon'.format(root=test_path))
    create_icons_from_scratch(test_config, path, images=True)
    icon_content = get_icon(
        path, 'ch.bav.kataster-belasteter-standorte-oev.oereb', 'Belastet, untersuchungsbedürftig'
    )
    assert filetype.guess(icon_content).extension == 'png'