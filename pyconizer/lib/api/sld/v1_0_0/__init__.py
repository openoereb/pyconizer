# -*- coding: utf-8 -*-
from pyconizer.lib.api.sld import SLDSchemaBase


class SLDSchema100(SLDSchemaBase):

    def __init__(self):
        super(SLDSchema100, self).__init__("StyledLayerDescriptor.xsd")
