# -*- coding: utf-8 -*-
from mako.template import Template
from pyramid.path import AssetResolver

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


def create_svg_icon(symbolizers):
    """
    Creates a SVG symbol icon out of a SLD symbol definition.

    Args:
        symbolizers (dict): All symbolizers which are are included in the SLD.

    Returns:
        str: The generated XML/SVG.
    """
    svg_template = Template(
        filename=AssetResolver('pyconizer').resolve(
            'lib/api/svg/templates/svg_1_0.xml').abspath(),
        input_encoding='utf-8',
        output_encoding='utf-8'
    )
    icon_paths = []
    for symbolizer in symbolizers['polygon_symolizers']:
        styles = []
        styles.extend(process_stroke_styling(symbolizer))
        styles.extend(process_fill_styling(symbolizer))
        fill_found = False
        for style in styles:
            if 'fill=' in style:
                fill_found = True
        if not fill_found:
            print('no fill found, adding it as empty style')
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
        icon_paths.append(content)
    for symbolizer in symbolizers['line_symbolizers']:
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
        icon_paths.append(content)
    for symbolizer in symbolizers['line_symbolizers']:
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
                        icon_paths.append(content)

    # only add a svg path if it would have content
    if len(icon_paths) > 0:
        svg_content = svg_template.render(**{
            'geometry_tag': '\n'.join(str(v) for v in icon_paths)
        })
        return svg_content.decode()
