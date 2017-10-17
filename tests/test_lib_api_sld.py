# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from pyconizer.lib.api.sld import FactoryFromString, extract_rules


def test_factory_from_string_wrong_sld_version():
    sld_content = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<StyledLayerDescriptor version=\"1.1.1\" " \
                  "xmlns=\"http://www.opengis.net/sld\" xmlns:gml=\"http://www.opengis.net/gml\" " \
                  "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" " \
                  "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                  "xsi:schemaLocation=\"http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/Sty" \
                  "ledLayerDescriptor.xsd\">\n<NamedLayer>\n<Name>ch.bav.kataster-belasteter-standorte-oev." \
                  "oereb_polygon</Name>\n<UserStyle>\n<FeatureTypeStyle>\n<Rule>\n<Name>Belastet, keine sch" \
                  "\u00e4dlichen oder l\u00e4stigen Einwirkungen zu erwarten</Name>\n<ogc:Filter><ogc:Prope" \
                  "rtyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal>class01</ogc:Li" \
                  "teral></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000000.000000</MaxS" \
                  "caleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter name=\"fill\">#ffff00</CssP" \
                  "arameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n<Name>Belastet, untersuchungs" \
                  "bed\u00fcrftig</Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</" \
                  "ogc:PropertyName><ogc:Literal>class02</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>" \
                  "\n<MaxScaleDenominator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fil" \
                  "l>\n<CssParameter name=\"fill\">#0066ff</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n<" \
                  "/Rule>\n<Rule>\n<Name>Belastet, weder \u00fcberwachungs- noch sanierungsbed\u00fcrftig</" \
                  "Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName" \
                  "><ogc:Literal>class03</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenom" \
                  "inator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParamete" \
                  "r name=\"fill\">#ffcc00</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n" \
                  "<Name>Belastet, \u00fcberwachungsbed\u00fcrftig</Name>\n<ogc:Filter><ogc:PropertyIsEqual" \
                  "To><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal>class04</ogc:Literal></og" \
                  "c:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000000.000000</MaxScaleDenomi" \
                  "nator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter name=\"fill\">#ff6605</CssParameter>" \
                  "\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n<Name>Belastet, sanierungsbed\u00fcrft" \
                  "ig</Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:Property" \
                  "Name><ogc:Literal>class05</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScale" \
                  "Denominator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssPar" \
                  "ameter name=\"fill\">#ff0000</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Ru" \
                  "le>\n<Name>Belastet, Untersuchungsbed\u00fcrftigkeit noch nicht definiert</Name>\n<ogc:F" \
                  "ilter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal" \
                  ">class06</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000" \
                  "000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter " \
                  "name=\"fill\">#5f5f5f</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n</FeatureT" \
                  "ypeStyle>\n</UserStyle>\n</NamedLayer>\n<NamedLayer>\n<Name>ch.bav.kataster-belasteter-s" \
                  "tandorte-oev.oereb_line</Name>\n<UserStyle>\n<FeatureTypeStyle>\n<Rule>\n<MaxScaleDenomi" \
                  "nator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Stroke>\n<CssParamet" \
                  "er name=\"stroke\">#000000</CssParameter>\n<CssParameter name=\"stroke-width\">1.00</Css" \
                  "Parameter>\n</Stroke>\n</PolygonSymbolizer>\n</Rule>\n</FeatureTypeStyle>\n</UserStyle>" \
                  "\n</NamedLayer>\n</StyledLayerDescriptor>\n\n".encode('utf-8')
    with pytest.raises(LookupError):
        FactoryFromString(sld_content)


def test_extract_rules_no_filter_but_name():
    sld_content = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<StyledLayerDescriptor version=\"1.0.0\" " \
                  "xmlns=\"http://www.opengis.net/sld\" xmlns:gml=\"http://www.opengis.net/gml\" " \
                  "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" " \
                  "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                  "xsi:schemaLocation=\"http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/Sty" \
                  "ledLayerDescriptor.xsd\">\n<NamedLayer>\n<Name>ch.bav.kataster-belasteter-standorte-oev." \
                  "oereb_polygon</Name>\n<UserStyle>\n<FeatureTypeStyle>\n<Rule>\n<Name>Belastet, keine sch" \
                  "\u00e4dlichen oder l\u00e4stigen Einwirkungen zu erwarten</Name>\n<MaxScaleDenominator>1" \
                  "00000000.000000</MaxS" \
                  "caleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter name=\"fill\">#ffff00</CssP" \
                  "arameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n<Name>Belastet, untersuchungs" \
                  "bed\u00fcrftig</Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</" \
                  "ogc:PropertyName><ogc:Literal>class02</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>" \
                  "\n<MaxScaleDenominator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fil" \
                  "l>\n<CssParameter name=\"fill\">#0066ff</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n<" \
                  "/Rule>\n<Rule>\n<Name>Belastet, weder \u00fcberwachungs- noch sanierungsbed\u00fcrftig</" \
                  "Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName" \
                  "><ogc:Literal>class03</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenom" \
                  "inator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParamete" \
                  "r name=\"fill\">#ffcc00</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n" \
                  "<Name>Belastet, \u00fcberwachungsbed\u00fcrftig</Name>\n<ogc:Filter><ogc:PropertyIsEqual" \
                  "To><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal>class04</ogc:Literal></og" \
                  "c:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000000.000000</MaxScaleDenomi" \
                  "nator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter name=\"fill\">#ff6605</CssParameter>" \
                  "\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n<Name>Belastet, sanierungsbed\u00fcrft" \
                  "ig</Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:Property" \
                  "Name><ogc:Literal>class05</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScale" \
                  "Denominator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssPar" \
                  "ameter name=\"fill\">#ff0000</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Ru" \
                  "le>\n<Name>Belastet, Untersuchungsbed\u00fcrftigkeit noch nicht definiert</Name>\n<ogc:F" \
                  "ilter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal" \
                  ">class06</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000" \
                  "000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter " \
                  "name=\"fill\">#5f5f5f</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n</FeatureT" \
                  "ypeStyle>\n</UserStyle>\n</NamedLayer>\n<NamedLayer>\n<Name>ch.bav.kataster-belasteter-s" \
                  "tandorte-oev.oereb_line</Name>\n<UserStyle>\n<FeatureTypeStyle>\n<Rule>\n<MaxScaleDenomi" \
                  "nator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Stroke>\n<CssParamet" \
                  "er name=\"stroke\">#000000</CssParameter>\n<CssParameter name=\"stroke-width\">1.00</Css" \
                  "Parameter>\n</Stroke>\n</PolygonSymbolizer>\n</Rule>\n</FeatureTypeStyle>\n</UserStyle>" \
                  "\n</NamedLayer>\n</StyledLayerDescriptor>\n\n".encode('utf-8')
    layers = extract_rules(sld_content)
    assert len(layers[0].rules) == 6


def test_extract_rules_no_name_but_filter():
    sld_content = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<StyledLayerDescriptor version=\"1.0.0\" " \
                  "xmlns=\"http://www.opengis.net/sld\" xmlns:gml=\"http://www.opengis.net/gml\" " \
                  "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" " \
                  "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                  "xsi:schemaLocation=\"http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/Sty" \
                  "ledLayerDescriptor.xsd\">\n<NamedLayer>\n<Name>ch.bav.kataster-belasteter-standorte-oev." \
                  "oereb_polygon</Name>\n<UserStyle>\n<FeatureTypeStyle>\n<Rule><ogc:Filter><ogc:Prope" \
                  "rtyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal>class01</ogc:Li" \
                  "teral></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000000.000000</MaxS" \
                  "caleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter name=\"fill\">#ffff00</CssP" \
                  "arameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n<Name>Belastet, untersuchungs" \
                  "bed\u00fcrftig</Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</" \
                  "ogc:PropertyName><ogc:Literal>class02</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>" \
                  "\n<MaxScaleDenominator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fil" \
                  "l>\n<CssParameter name=\"fill\">#0066ff</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n<" \
                  "/Rule>\n<Rule>\n<Name>Belastet, weder \u00fcberwachungs- noch sanierungsbed\u00fcrftig</" \
                  "Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName" \
                  "><ogc:Literal>class03</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenom" \
                  "inator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParamete" \
                  "r name=\"fill\">#ffcc00</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n" \
                  "<Name>Belastet, \u00fcberwachungsbed\u00fcrftig</Name>\n<ogc:Filter><ogc:PropertyIsEqual" \
                  "To><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal>class04</ogc:Literal></og" \
                  "c:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000000.000000</MaxScaleDenomi" \
                  "nator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter name=\"fill\">#ff6605</CssParameter>" \
                  "\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n<Name>Belastet, sanierungsbed\u00fcrft" \
                  "ig</Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:Property" \
                  "Name><ogc:Literal>class05</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScale" \
                  "Denominator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssPar" \
                  "ameter name=\"fill\">#ff0000</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Ru" \
                  "le>\n<Name>Belastet, Untersuchungsbed\u00fcrftigkeit noch nicht definiert</Name>\n<ogc:F" \
                  "ilter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal" \
                  ">class06</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000" \
                  "000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter " \
                  "name=\"fill\">#5f5f5f</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n</FeatureT" \
                  "ypeStyle>\n</UserStyle>\n</NamedLayer>\n<NamedLayer>\n<Name>ch.bav.kataster-belasteter-s" \
                  "tandorte-oev.oereb_line</Name>\n<UserStyle>\n<FeatureTypeStyle>\n<Rule>\n<MaxScaleDenomi" \
                  "nator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Stroke>\n<CssParamet" \
                  "er name=\"stroke\">#000000</CssParameter>\n<CssParameter name=\"stroke-width\">1.00</Css" \
                  "Parameter>\n</Stroke>\n</PolygonSymbolizer>\n</Rule>\n</FeatureTypeStyle>\n</UserStyle>" \
                  "\n</NamedLayer>\n</StyledLayerDescriptor>\n\n".encode('utf-8')
    layers = extract_rules(sld_content)
    assert len(layers[0].rules) == 6


def test_extract_rules_no_encoding():
    sld_content = "<?xml version=\"1.0\" ?>\n<StyledLayerDescriptor version=\"1.0.0\" " \
                  "xmlns=\"http://www.opengis.net/sld\" xmlns:gml=\"http://www.opengis.net/gml\" " \
                  "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" " \
                  "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                  "xsi:schemaLocation=\"http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/Sty" \
                  "ledLayerDescriptor.xsd\">\n<NamedLayer>\n<Name>ch.bav.kataster-belasteter-standorte-oev." \
                  "oereb_polygon</Name>\n<UserStyle>\n<FeatureTypeStyle>\n<Rule><ogc:Filter><ogc:Prope" \
                  "rtyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal>class01</ogc:Li" \
                  "teral></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000000.000000</MaxS" \
                  "caleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter name=\"fill\">#ffff00</CssP" \
                  "arameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n<Name>Belastet, untersuchungs" \
                  "bed\u00fcrftig</Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</" \
                  "ogc:PropertyName><ogc:Literal>class02</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>" \
                  "\n<MaxScaleDenominator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fil" \
                  "l>\n<CssParameter name=\"fill\">#0066ff</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n<" \
                  "/Rule>\n<Rule>\n<Name>Belastet, weder \u00fcberwachungs- noch sanierungsbed\u00fcrftig</" \
                  "Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName" \
                  "><ogc:Literal>class03</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenom" \
                  "inator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParamete" \
                  "r name=\"fill\">#ffcc00</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n" \
                  "<Name>Belastet, \u00fcberwachungsbed\u00fcrftig</Name>\n<ogc:Filter><ogc:PropertyIsEqual" \
                  "To><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal>class04</ogc:Literal></og" \
                  "c:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000000.000000</MaxScaleDenomi" \
                  "nator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter name=\"fill\">#ff6605</CssParameter>" \
                  "\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Rule>\n<Name>Belastet, sanierungsbed\u00fcrft" \
                  "ig</Name>\n<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:Property" \
                  "Name><ogc:Literal>class05</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScale" \
                  "Denominator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssPar" \
                  "ameter name=\"fill\">#ff0000</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n<Ru" \
                  "le>\n<Name>Belastet, Untersuchungsbed\u00fcrftigkeit noch nicht definiert</Name>\n<ogc:F" \
                  "ilter><ogc:PropertyIsEqualTo><ogc:PropertyName>bgdi_class</ogc:PropertyName><ogc:Literal" \
                  ">class06</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>\n<MaxScaleDenominator>100000" \
                  "000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Fill>\n<CssParameter " \
                  "name=\"fill\">#5f5f5f</CssParameter>\n</Fill>\n</PolygonSymbolizer>\n</Rule>\n</FeatureT" \
                  "ypeStyle>\n</UserStyle>\n</NamedLayer>\n<NamedLayer>\n<Name>ch.bav.kataster-belasteter-s" \
                  "tandorte-oev.oereb_line</Name>\n<UserStyle>\n<FeatureTypeStyle>\n<Rule>\n<MaxScaleDenomi" \
                  "nator>100000000.000000</MaxScaleDenominator>\n<PolygonSymbolizer>\n<Stroke>\n<CssParamet" \
                  "er name=\"stroke\">#000000</CssParameter>\n<CssParameter name=\"stroke-width\">1.00</Css" \
                  "Parameter>\n</Stroke>\n</PolygonSymbolizer>\n</Rule>\n</FeatureTypeStyle>\n</UserStyle>" \
                  "\n</NamedLayer>\n</StyledLayerDescriptor>\n\n".encode('utf-8')
    layers = extract_rules(sld_content, encoding='utf-8')
    assert len(layers[0].rules) == 6
