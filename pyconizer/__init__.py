# -*- coding: utf-8 -*-
import base64
import os
import shutil

from pyconizer.lib.api.image import download_legend_icon
from pyconizer.lib.api.sld import load_sld_content, extract_rules
from pyconizer.lib.api.structure import Configuration, write, read, persist_layer_path, write_rule, \
    persist_mapping

config = [
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
    }, {
        'url': 'http://geowms.bl.ch/?',
        'layer': 'liegenschaft',
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
    }, {
        'url': 'http://geowms.bl.ch/?',
        'layer': 'np_nur_grundnutzung_group',
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
    }, {
        'url': 'http://geowms.bl.ch/?',
        'layer': 'grundkarte_farbig_group',
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

path = '/tmp/iconizer/icons/'


def create_icons_from_scratch(configuration, path, json_only=True):
    """
    This is probably the starting point. If you use this package for the first time you might want use this.

    Args:
        configuration (list of dict): The minimal configuration to construct all images from scratch
        path (str): The root path where all the stuff will be created in.
        json_only (bool): Switch to create only a JSON file. This might be useful for test use. This is
            constructing the JSON from the passed configuration but do not downloads the image content.
    """

    configuration = Configuration.from_dict(configuration)
    for layer in configuration.layers:

        # download the sld content and store it to the config object
        sld_content = load_sld_content(layer.get_styles_url)
        layer.get_styles.set_content(sld_content)

        # add the empty structure of rules extracted from the SLD
        named_layers = extract_rules(sld_content)
        layer.get_legend.add_named_layers(named_layers)
        layer.get_legend.create_rule_urls(layer.url)
    write(path, configuration, json_only=json_only)


def update_icon_content(path, layer_name, mapping_file_name='mapping.json', json_only=True):
    """
    This function updates all icon contents in an existing structure. The update is filtered by the
    layer_name to update only the wanted layer.

    Args:
        path (str): The root path which all the files will be created in.
        layer_name (str): This must be the layer name fitting one of the names in the JSON configuration. It
            must not be the name of some named layer.
        mapping_file_name (str): The name of the mapping file which is expected to be existing inside of the
            path.
        json_only (bool): Switch to create only a JSON file. This might be useful for test use. This is
            constructing the JSON from the passed configuration but do not downloads the image content.
    """

    configuration = read(os.path.abspath('{path}/{mapping}'.format(path=path, mapping=mapping_file_name)))
    for layer in configuration.layers:
        if layer.name == layer_name:
            print 'found the layer to update:', layer.name
            for named_layer in layer.get_legend.named_layers:
                for rule in named_layer.rules:
                    download_legend_icon(rule)
                    if not json_only:
                        combined_path = persist_layer_path(path, layer.name, named_layer.name)
                        write_rule(combined_path, rule)
            persist_mapping(path, configuration)
            return
    print 'No layer with name "{0}" was found'.format(layer_name)


def delete(path, layer_name, mapping_file_name='mapping.json', json_only=True):
    """
    Deletes a layer from the structure. If the json_only parameter is set to False, it is done also in the
    structures file system representation.

    Args:
        path (str): The root path which all the files will be created in.
        layer_name (str): This must be the layer name fitting one of the names in the JSON configuration. It
            must not be the name of some named layer.
        mapping_file_name (str): The name of the mapping file which is expected to be existing inside of the
            path.
        json_only (bool): Switch to create only a JSON file. This might be useful for test use. This is
            constructing the JSON from the passed configuration but do not downloads the image content.
    """

    configuration = read(os.path.abspath('{path}/{mapping}'.format(path=path, mapping=mapping_file_name)))
    found_layer_index = None
    for index, layer in enumerate(configuration.layers):
        if layer.name == layer_name:
            found_layer_index = index
    if found_layer_index is not None:
        configuration.layers.pop(found_layer_index)
        if not json_only:
            shutil.rmtree(os.path.abspath('{path}/{layer}'.format(path=path, layer=layer_name)))
        persist_mapping(path, configuration)
    else:
        print 'No layer with name "{0}" was found'.format(layer_name)


def get_icon(path, layer_name, class_name, mapping_file_name='mapping.json'):
    """

    Args:
        path (str): The root path which all the files will be created in.
        layer_name (str): This must be the layer name fitting one of the names in the JSON configuration. It
            must not be the name of some named layer.
        class_name (str): The class name which is used to extract the icon.
        mapping_file_name (str): The name of the mapping file which is expected to be existing inside of the
            path.

    Returns:
        str: The content of the icon. It is encoded as base code 64.
    """
    configuration = read(os.path.abspath('{path}/{mapping}'.format(path=path, mapping=mapping_file_name)))
    for layer in configuration.layers:
        if layer.name == layer_name:
            print 'found the layer you where looking for:', layer.name
            for named_layer in layer.get_legend.named_layers:
                for rule in named_layer.rules:
                    if rule.class_name == class_name:
                        print 'found the rule you where looking for:', class_name
                        return base64.b64encode(rule.content)
