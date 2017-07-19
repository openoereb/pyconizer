# -*- coding: utf-8 -*-
from mako.template import Template
from pyramid.path import AssetResolver

from pyconizer.lib.api.sld import FactoryFromString

square_points = "28,28 28,32 32,32 32,28 28,28"
polygon_points = "10,10 10,54 54,54 54,10 10,10"
line_points = "54,54 10,10"


def process_fill_styling(symbolizer):
    styles = []
    if symbolizer.Fill:
        for css_parameter in symbolizer.Fill.CssParameter:
            styles.append('{name}="{value}"'.format(
                name=css_parameter.get_name(),
                value=css_parameter.get_valueOf_()
            ))
    return styles


def process_stroke_styling(symbolizer):
    styles = []
    if symbolizer.Stroke:
        for css_parameter in symbolizer.Stroke.CssParameter:
            styles.append('{name}="{value}"'.format(
                name=css_parameter.get_name(),
                value=css_parameter.get_valueOf_()
            ))
    return styles


def sld_to_svg(sld_content):
    """

    Args:
        sld_content (str): The SLD you want to split up in all its svg symbol definitions.

    Returns:
        dict: The generated SVGS wrapped in a dictionary sorted after layer name and sub sorted after class
    """
    svg_template = Template(
        filename=AssetResolver('pyconizer').resolve(
            'lib/api/svg/templates/svg_1_0.xml').abspath(),
        input_encoding='utf-8',
        output_encoding='utf-8'
    )
    sld_content = FactoryFromString(sld_content)
    svg_construct = {}
    for named_layer in sld_content.NamedLayer:
        named_layer_name = named_layer.Name
        svg_construct.update({named_layer_name: {}})
        for user_style in named_layer.UserStyle:
            for feature_type_style in user_style.FeatureTypeStyle:
                i = 1
                for rule in feature_type_style.Rule:
                    # only comparison ops are supported now, if rule has no filter => What is this????
                    if not rule.Filter and rule.Name:
                        class_name = rule.Name
                        filter_class = 'unfiltered_{0}'.format(str(i))
                        i += 1
                    if rule.Filter and not rule.Name:
                        class_name = rule.Filter.comparisonOps.expression[1].get_valueOf_()
                        filter_class = rule.Filter.comparisonOps.expression[1].get_valueOf_()
                    if rule.Filter and rule.Name:
                        class_name = rule.Name
                        filter_class = rule.Filter.comparisonOps.expression[1].get_valueOf_()
                    print class_name
                    print filter_class
                    class_svg_paths = []
                    for symbolizer in rule.Symbolizer:
                        if 'PolygonSymbolizer' in symbolizer.original_tagname_:
                            styles = []
                            styles.extend(process_stroke_styling(symbolizer))
                            styles.extend(process_fill_styling(symbolizer))
                            fill_found = False
                            for style in styles:
                                if 'fill=' in style:
                                    fill_found = True
                            if not fill_found:
                                print 'no fill found, adding it as empty style'
                                styles.append('fill="none"')
                            polygon_template = Template(
                                filename=AssetResolver('pyconizer').resolve(
                                    'lib/api/svg/templates/polygon.xml').abspath(),
                                input_encoding='utf-8',
                                output_encoding='utf-8'
                            )
                            template_params = {
                                'points': polygon_points,
                                'styles': ' '.join(styles)
                            }
                            content = polygon_template.render(**template_params)
                            class_svg_paths.append(content)

                        elif 'LineSymbolizer' in symbolizer.original_tagname_:
                            styles = []
                            styles.extend(process_stroke_styling(symbolizer))
                            # TODO: Add support for geometry Handling
                            line_template = Template(
                                filename=AssetResolver('pyconizer').resolve(
                                    'lib/api/svg/templates/line.xml').abspath(),
                                input_encoding='utf-8',
                                output_encoding='utf-8'
                            )
                            template_params = {
                                'points': line_points,
                                'styles': ' '.join(styles)
                            }
                            content = line_template.render(**template_params)
                            class_svg_paths.append(content)
                        elif 'PointSymbolizer' in symbolizer.original_tagname_:
                            # TODO: Check how to handle a Point
                            if symbolizer.Graphic:
                                if symbolizer.Graphic.Mark:
                                    styles = []
                                    for mark in symbolizer.Graphic.Mark:
                                        styles.extend(process_fill_styling(mark))
                                        if mark.WellKnownName == 'square':
                                            polygon_template = Template(
                                                filename=AssetResolver('pyconizer').resolve(
                                                    'lib/api/svg/templates/polygon.xml').abspath(),
                                                input_encoding='utf-8',
                                                output_encoding='utf-8'
                                            )
                                            template_params = {
                                                'points': square_points,
                                                'styles': ' '.join(styles)
                                            }
                                            content = polygon_template.render(**template_params)
                                            class_svg_paths.append(content)
                            elif symbolizer.Geometry:
                                # TODO: implement geometry symbolizer
                                print 'point symbolizer does not support geometry for now'
                            # else:
                            #     styles = [
                            #         'stroke="black"',
                            #         'stroke-width="1"',
                            #         'fill="red"'
                            #     ]
                            #     polygon_template = Template(
                            #         filename=AssetResolver('pyconizer').resolve(
                            #             'lib/api/svg/templates/circle.xml').abspath(),
                            #         input_encoding='utf-8',
                            #         output_encoding='utf-8'
                            #     )
                            #     template_params = {
                            #         'x': '2',
                            #         'y': '2',
                            #         'radius': '1',
                            #         'styles': ' '.join(styles)
                            #     }
                            #     content = polygon_template.render(**template_params)
                            #     class_svg_paths.append(content)

                    # only add a svg path if it would have content
                    if len(class_svg_paths) > 0:
                        svg_content = svg_template.render(**{
                            'filter_class': filter_class,
                            'name': class_name,
                            'geometry_tag': '\n'.join(class_svg_paths)
                        })
                        svg_construct[named_layer_name].update({
                            filter_class: svg_content
                        })
    return svg_construct
