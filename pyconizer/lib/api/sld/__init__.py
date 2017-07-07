# -*- coding: utf-8 -*-
import xml.etree.ElementTree as etree
import StringIO


def FactoryFromString(sld_content):
    """

    Args:
        sld_content (str): The content of an SLD to check for version and parse with the found module.

    Returns:
        pyconizer.lib.api.sld.v1_0_0.classes.StyledLayerDescriptor: The complete objectified representation
            of the SLD.
    """
    parser = etree.XMLParser()
    tree = etree.fromstring(sld_content, parser)
    version = tree.attrib.get('version')
    if version == '1.0.0':
        from pyconizer.lib.api.sld.v1_0_0 import classes
        found_version = classes
    else:
        raise LookupError('Version is not supported. Version of SLD was: {0}'.format(version))
    output = StringIO.StringIO(sld_content)
    parsed_sld = found_version.parse(output, parser)
    return parsed_sld


def Factory(sld_file_path):
    """

    Args:
        sld_file_path (str): The SLD file to check for version and parse with the found module.

    Returns:
        pyconizer.lib.api.sld.v1_0_0.classes.StyledLayerDescriptor: The complete objectified representation
            of the SLD.
    """
    content = open(sld_file_path).read()
    return FactoryFromString(content)
