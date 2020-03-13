# -*- coding: utf-8 -*-

from pyconizer.lib.api.sld import SLDSchemaBase


class SLDSchema110(SLDSchemaBase):

    def __init__(self):
        super(SLDSchema110, self).__init__("sldAll.xsd")
