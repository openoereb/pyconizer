# -*- coding: utf-8 -*-
import logging
import re

from lxml import etree, objectify

from pyconizer.lib.api.structure import Rule, NamedLayer
from pyconizer.lib.api.svg import create_svg_icon

from pyconizer.lib.api.sld.v1_0_0 import SLDSchema100
from pyconizer.lib.api.sld.v1_1_0 import SLDSchema110

# python 3 compatibility
from future.moves.urllib.request import urlopen

try:
    from StringIO import StringIO
    python_3 = False
except ImportError:
    from io import StringIO
    python_3 = True

log = logging.getLogger('pyconizer')


class SLDSchemaBase(object):

    def __init__(self, sld_schema_definition):
        self.sld_schema_definition = sld_schema_definition
        self.schema = etree.XMLSchema(etree.parse(sld_schema_definition))

    def validate(self, sld):
        """

        Args:
            sld (lxml.etree._ElementTree): The etree element to validate.
        Returns:
            boolean: Whether the sld was valid or not.
        """
        return self.schema.validate(sld)


def FactoryFromString(sld_content):
    """

    Args:
        sld_content (str): The content of an SLD to check for version and parse with the found module.

    Returns:
        lxml.objectify.ObjectifiedElement: The complete objectified representation of the SLD.
    """

    sld_document = etree.parse(StringIO(sld_content))
    sld_schema_100 = SLDSchema100()
    sld_schema_110 = SLDSchema110()

    if sld_schema_100.validate(sld_document):
        parser = objectify.makeparser(schema=sld_schema_100)
    elif sld_schema_110.validate(sld_document):
        parser = objectify.makeparser(schema=sld_schema_100)
    else:
        raise LookupError('Version is not supported. Version of SLD was: {0}'.format(
            sld_document.getroot().attrib['version']))
    return objectify.fromstring(sld_document, parser)


def load_sld_content(url):
    """
    Load the SLD from the passed url.

    Args:
        url (str): The URL which should return a SLD generated from WMS.

    Returns:
        str: The SLD as XML in a simple string.

    """
    response = urlopen(url)
    content = response.read()
    if python_3:
        return content.decode(response.headers.get_content_charset())
    else:
        return content


def extract_rules(sld_content):
    """
    Extract all Rules with its name and classes.

    Args:
        sld_content (str): The SLD you want to split up in all its svg symbol definitions.

    Returns:
        list of pyconizer.lib.api.structure.NamedLayer: A list of named layers and their image
            configs all wrapped in application structure.
    """
    objectified_sld = FactoryFromString(sld_content)
    ns_map = objectified_sld.nsmap
    layers = []
    named_layers = objectified_sld.findall('NamedLayer')
    log.debug('Start processing of SLD')
    log.debug('Found {} named layers.'.format(len(named_layers)))
    for named_layer in named_layers:
        named_layer_name = named_layer.find('se:Name', namespaces=ns_map)
        log.debug('  Start processing of named layer "{}"'.format(
            named_layer_name
        ), )
        rules = []
        user_styles = named_layer.findall('UserStyle', namespaces=ns_map)
        # TODO: Implement multiple user styles per layer
        if len(user_styles) > 1:
            raise LookupError('Found more than one user style definition in SLD')
        for user_style in user_styles:
            feature_type_styles = user_style.findall(
                'se:FeatureTypeStyle',
                namespaces=ns_map
            )
            # TODO: Implement multiple user styles per layer, or find out if this is possible at least
            if len(feature_type_styles) > 1:
                raise LookupError('Found more than one feature type style definition in SLD')
            for feature_type_style in feature_type_styles:
                style_rules = feature_type_style.findall(
                    'se:Rule',
                    namespaces=ns_map
                )
                for rule in style_rules:
                    filters = rule.findall('ogc:Filter', namespaces=ns_map)
                    if len(filters) > 1:
                        raise LookupError('found an SLD with multiple filter definitions per rule.'
                                          'This is not supported.')
                    rule_name = rule.find('se:Name', namespaces=ns_map)
                    symbolizers = {
                        'point_symbolizers': rule.findall(
                            'se:PointSymbolizer',
                            namespaces=ns_map
                        ),
                        'line_symbolizers': rule.findall(
                            'se:LineSymbolizer',
                            namespaces=ns_map
                        ),
                        'polygon_symolizers': rule.findall(
                            'se:PolygonSymbolizer',
                            namespaces=ns_map
                        )
                    }

                    # only comparison ops are supported now, if rule has no filter => What is this????
                    if not filters and rule_name:
                        structure_rule = Rule(class_name=rule_name)
                        structure_rule.set_svg(create_svg_icon(symbolizers))
                        rules.append(structure_rule)
                    elif filters and not rule_name:
                        filter_class = filters[0].find('ogc:Literal', namespaces=ns_map)
                        structure_rule = Rule(
                            filter_class=filter_class
                        )
                        structure_rule.set_svg(create_svg_icon(symbolizers))
                        rules.append(structure_rule)
                    elif filters and rule_name:
                        filter_class = filters[0].find('ogc:Literal', namespaces=ns_map)
                        structure_rule = Rule(
                            class_name=rule.Name,
                            filter_class=filter_class
                        )
                        structure_rule.set_svg(create_svg_icon(symbolizers))
                        rules.append(structure_rule)
        layers.append(NamedLayer(name=named_layer_name, rules=rules))
    return layers
