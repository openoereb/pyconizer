# -*- coding: utf-8 -*-
from urllib2 import urlopen


def download_legend_icon(rule):
    """

    Args:
        rule (pyconizer.lib.api.structure.Rule): The rule which icon should be downloaded.

    """
    if rule.rule_url:
        print('process rule:', rule.class_name)
        response = urlopen(rule.rule_url)
        rule.set_content(response.read())
    else:
        print('no url was found on rule with class name:', rule.dict)


def download_all_legend_icons(configuration):
    """
    Load images via configured get styles request and prepared and parsed sld content
    Args:
        configuration (pyconizer.lib.api.structure.Configuration): The configuration which holds all
            information to download the icons.

    Returns:
        list of dict: The Updated config dictionary containing now the obtained images.
    """
    for layer in configuration.layers:
        print('process layer:', layer.name)
        for named_layer in layer.get_legend.named_layers:
            print('process named layer:', named_layer.name)
            for rule in named_layer.rules:
                download_legend_icon(rule)
