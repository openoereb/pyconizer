#!/usr/bin/env python

#
# Generated Wed Jul 10 14:54:36 2019 by generateDS.py version 2.28.1.
# Python 2.7.15+ (default, Nov 27 2018, 23:36:35)  [GCC 7.3.0]
#
# Command line options:
#   ('-f', '')
#   ('-o', 'classes.py')
#   ('-s', 'sub_classes.py')
#   ('--external-encoding', 'utf-8')
#
# Command line arguments:
#   StyledLayerDescriptor.xsd
#
# Command line:
#   .venv/bin/generateDS -f -o "classes.py" -s "sub_classes.py" --external-encoding="utf-8" StyledLayerDescriptor.xsd
#
# Current working directory (os.getcwd()):
#   sld-1-1-0
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class DescribeLayerResponseTypeSub(supermod.DescribeLayerResponseType):
    def __init__(self, Version=None, LayerDescription=None):
        super(DescribeLayerResponseTypeSub, self).__init__(Version, LayerDescription, )
supermod.DescribeLayerResponseType.subclass = DescribeLayerResponseTypeSub
# end class DescribeLayerResponseTypeSub


class LayerDescriptionTypeSub(supermod.LayerDescriptionType):
    def __init__(self, owsType=None, OnlineResource=None, TypeName=None):
        super(LayerDescriptionTypeSub, self).__init__(owsType, OnlineResource, TypeName, )
supermod.LayerDescriptionType.subclass = LayerDescriptionTypeSub
# end class LayerDescriptionTypeSub


class TypeNameTypeSub(supermod.TypeNameType):
    def __init__(self, FeatureTypeName=None, CoverageName=None):
        super(TypeNameTypeSub, self).__init__(FeatureTypeName, CoverageName, )
supermod.TypeNameType.subclass = TypeNameTypeSub
# end class TypeNameTypeSub


class StyledLayerDescriptorSub(supermod.StyledLayerDescriptor):
    def __init__(self, version=None, Name=None, Description=None, UseSLDLibrary=None, NamedLayer=None, UserLayer=None):
        super(StyledLayerDescriptorSub, self).__init__(version, Name, Description, UseSLDLibrary, NamedLayer, UserLayer, )
supermod.StyledLayerDescriptor.subclass = StyledLayerDescriptorSub
# end class StyledLayerDescriptorSub


class UseSLDLibrarySub(supermod.UseSLDLibrary):
    def __init__(self, OnlineResource=None):
        super(UseSLDLibrarySub, self).__init__(OnlineResource, )
supermod.UseSLDLibrary.subclass = UseSLDLibrarySub
# end class UseSLDLibrarySub


class NamedLayerSub(supermod.NamedLayer):
    def __init__(self, Name=None, Description=None, LayerFeatureConstraints=None, NamedStyle=None, UserStyle=None):
        super(NamedLayerSub, self).__init__(Name, Description, LayerFeatureConstraints, NamedStyle, UserStyle, )
supermod.NamedLayer.subclass = NamedLayerSub
# end class NamedLayerSub


class NamedStyleSub(supermod.NamedStyle):
    def __init__(self, Name=None, Description=None):
        super(NamedStyleSub, self).__init__(Name, Description, )
supermod.NamedStyle.subclass = NamedStyleSub
# end class NamedStyleSub


class UserLayerSub(supermod.UserLayer):
    def __init__(self, Name=None, Description=None, RemoteOWS=None, InlineFeature=None, LayerFeatureConstraints=None, LayerCoverageConstraints=None, UserStyle=None):
        super(UserLayerSub, self).__init__(Name, Description, RemoteOWS, InlineFeature, LayerFeatureConstraints, LayerCoverageConstraints, UserStyle, )
supermod.UserLayer.subclass = UserLayerSub
# end class UserLayerSub


class RemoteOWSSub(supermod.RemoteOWS):
    def __init__(self, Service=None, OnlineResource=None):
        super(RemoteOWSSub, self).__init__(Service, OnlineResource, )
supermod.RemoteOWS.subclass = RemoteOWSSub
# end class RemoteOWSSub


class InlineFeatureSub(supermod.InlineFeature):
    def __init__(self, FeatureCollection=None):
        super(InlineFeatureSub, self).__init__(FeatureCollection, )
supermod.InlineFeature.subclass = InlineFeatureSub
# end class InlineFeatureSub


class LayerFeatureConstraintsSub(supermod.LayerFeatureConstraints):
    def __init__(self, FeatureTypeConstraint=None):
        super(LayerFeatureConstraintsSub, self).__init__(FeatureTypeConstraint, )
supermod.LayerFeatureConstraints.subclass = LayerFeatureConstraintsSub
# end class LayerFeatureConstraintsSub


class FeatureTypeConstraintSub(supermod.FeatureTypeConstraint):
    def __init__(self, FeatureTypeName=None, Filter=None, Extent=None):
        super(FeatureTypeConstraintSub, self).__init__(FeatureTypeName, Filter, Extent, )
supermod.FeatureTypeConstraint.subclass = FeatureTypeConstraintSub
# end class FeatureTypeConstraintSub


class LayerCoverageConstraintsSub(supermod.LayerCoverageConstraints):
    def __init__(self, CoverageConstraint=None):
        super(LayerCoverageConstraintsSub, self).__init__(CoverageConstraint, )
supermod.LayerCoverageConstraints.subclass = LayerCoverageConstraintsSub
# end class LayerCoverageConstraintsSub


class CoverageConstraintSub(supermod.CoverageConstraint):
    def __init__(self, CoverageName=None, CoverageExtent=None):
        super(CoverageConstraintSub, self).__init__(CoverageName, CoverageExtent, )
supermod.CoverageConstraint.subclass = CoverageConstraintSub
# end class CoverageConstraintSub


class CoverageExtentSub(supermod.CoverageExtent):
    def __init__(self, RangeAxis=None, TimePeriod=None):
        super(CoverageExtentSub, self).__init__(RangeAxis, TimePeriod, )
supermod.CoverageExtent.subclass = CoverageExtentSub
# end class CoverageExtentSub


class RangeAxisSub(supermod.RangeAxis):
    def __init__(self, Name=None, Value=None):
        super(RangeAxisSub, self).__init__(Name, Value, )
supermod.RangeAxis.subclass = RangeAxisSub
# end class RangeAxisSub


class ExtentSub(supermod.Extent):
    def __init__(self, Name=None, Value=None):
        super(ExtentSub, self).__init__(Name, Value, )
supermod.Extent.subclass = ExtentSub
# end class ExtentSub


class UserStyleSub(supermod.UserStyle):
    def __init__(self, Name=None, Description=None, IsDefault=None, FeatureTypeStyle=None, CoverageStyle=None, OnlineResource=None):
        super(UserStyleSub, self).__init__(Name, Description, IsDefault, FeatureTypeStyle, CoverageStyle, OnlineResource, )
supermod.UserStyle.subclass = UserStyleSub
# end class UserStyleSub


class BoundingShapeTypeSub(supermod.BoundingShapeType):
    def __init__(self, Envelope=None, Null=None):
        super(BoundingShapeTypeSub, self).__init__(Envelope, Null, )
supermod.BoundingShapeType.subclass = BoundingShapeTypeSub
# end class BoundingShapeTypeSub


class FeaturePropertyTypeSub(supermod.FeaturePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Feature=None):
        super(FeaturePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Feature, )
supermod.FeaturePropertyType.subclass = FeaturePropertyTypeSub
# end class FeaturePropertyTypeSub


class FeatureArrayPropertyTypeSub(supermod.FeatureArrayPropertyType):
    def __init__(self, _Feature=None):
        super(FeatureArrayPropertyTypeSub, self).__init__(_Feature, )
supermod.FeatureArrayPropertyType.subclass = FeatureArrayPropertyTypeSub
# end class FeatureArrayPropertyTypeSub


class BoundedFeatureTypeSub(supermod.BoundedFeatureType):
    def __init__(self, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None):
        super(BoundedFeatureTypeSub, self).__init__(metaDataProperty, description, name, boundedBy, location, )
supermod.BoundedFeatureType.subclass = BoundedFeatureTypeSub
# end class BoundedFeatureTypeSub


class LocationPropertyTypeSub(supermod.LocationPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Geometry=None, LocationKeyWord=None, LocationString=None, Null=None, extensiontype_=None):
        super(LocationPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Geometry, LocationKeyWord, LocationString, Null, extensiontype_, )
supermod.LocationPropertyType.subclass = LocationPropertyTypeSub
# end class LocationPropertyTypeSub


class PriorityLocationPropertyTypeSub(supermod.PriorityLocationPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Geometry=None, LocationKeyWord=None, LocationString=None, Null=None, priority=None):
        super(PriorityLocationPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Geometry, LocationKeyWord, LocationString, Null, priority, )
supermod.PriorityLocationPropertyType.subclass = PriorityLocationPropertyTypeSub
# end class PriorityLocationPropertyTypeSub


class HistoryPropertyTypeSub(supermod.HistoryPropertyType):
    def __init__(self, _TimeSlice=None):
        super(HistoryPropertyTypeSub, self).__init__(_TimeSlice, )
supermod.HistoryPropertyType.subclass = HistoryPropertyTypeSub
# end class HistoryPropertyTypeSub


class TrackTypeSub(supermod.TrackType):
    def __init__(self, MovingObjectStatus=None):
        super(TrackTypeSub, self).__init__(MovingObjectStatus, )
supermod.TrackType.subclass = TrackTypeSub
# end class TrackTypeSub


class DirectionPropertyTypeSub(supermod.DirectionPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, DirectionVector=None, CompassPoint=None, DirectionKeyword=None, DirectionString=None):
        super(DirectionPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, DirectionVector, CompassPoint, DirectionKeyword, DirectionString, )
supermod.DirectionPropertyType.subclass = DirectionPropertyTypeSub
# end class DirectionPropertyTypeSub


class DirectionVectorTypeSub(supermod.DirectionVectorType):
    def __init__(self, vector=None, horizontalAngle=None, verticalAngle=None):
        super(DirectionVectorTypeSub, self).__init__(vector, horizontalAngle, verticalAngle, )
supermod.DirectionVectorType.subclass = DirectionVectorTypeSub
# end class DirectionVectorTypeSub


class GeometryPropertyTypeSub(supermod.GeometryPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Geometry=None):
        super(GeometryPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Geometry, )
supermod.GeometryPropertyType.subclass = GeometryPropertyTypeSub
# end class GeometryPropertyTypeSub


class GeometryArrayPropertyTypeSub(supermod.GeometryArrayPropertyType):
    def __init__(self, _Geometry=None):
        super(GeometryArrayPropertyTypeSub, self).__init__(_Geometry, )
supermod.GeometryArrayPropertyType.subclass = GeometryArrayPropertyTypeSub
# end class GeometryArrayPropertyTypeSub


class GeometricPrimitivePropertyTypeSub(supermod.GeometricPrimitivePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _GeometricPrimitive=None):
        super(GeometricPrimitivePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _GeometricPrimitive, )
supermod.GeometricPrimitivePropertyType.subclass = GeometricPrimitivePropertyTypeSub
# end class GeometricPrimitivePropertyTypeSub


class PointPropertyTypeSub(supermod.PointPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Point=None):
        super(PointPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Point, )
supermod.PointPropertyType.subclass = PointPropertyTypeSub
# end class PointPropertyTypeSub


class PointArrayPropertyTypeSub(supermod.PointArrayPropertyType):
    def __init__(self, Point=None):
        super(PointArrayPropertyTypeSub, self).__init__(Point, )
supermod.PointArrayPropertyType.subclass = PointArrayPropertyTypeSub
# end class PointArrayPropertyTypeSub


class CurvePropertyTypeSub(supermod.CurvePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Curve=None):
        super(CurvePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Curve, )
supermod.CurvePropertyType.subclass = CurvePropertyTypeSub
# end class CurvePropertyTypeSub


class CurveArrayPropertyTypeSub(supermod.CurveArrayPropertyType):
    def __init__(self, _Curve=None):
        super(CurveArrayPropertyTypeSub, self).__init__(_Curve, )
supermod.CurveArrayPropertyType.subclass = CurveArrayPropertyTypeSub
# end class CurveArrayPropertyTypeSub


class DirectPositionTypeSub(supermod.DirectPositionType):
    def __init__(self, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, valueOf_=None):
        super(DirectPositionTypeSub, self).__init__(srsName, srsDimension, axisLabels, uomLabels, valueOf_, )
supermod.DirectPositionType.subclass = DirectPositionTypeSub
# end class DirectPositionTypeSub


class DirectPositionListTypeSub(supermod.DirectPositionListType):
    def __init__(self, count=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, valueOf_=None):
        super(DirectPositionListTypeSub, self).__init__(count, srsName, srsDimension, axisLabels, uomLabels, valueOf_, )
supermod.DirectPositionListType.subclass = DirectPositionListTypeSub
# end class DirectPositionListTypeSub


class VectorTypeSub(supermod.VectorType):
    def __init__(self, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, valueOf_=None):
        super(VectorTypeSub, self).__init__(srsName, srsDimension, axisLabels, uomLabels, valueOf_, )
supermod.VectorType.subclass = VectorTypeSub
# end class VectorTypeSub


class EnvelopeTypeSub(supermod.EnvelopeType):
    def __init__(self, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, lowerCorner=None, upperCorner=None, coord=None, pos=None, coordinates=None, extensiontype_=None):
        super(EnvelopeTypeSub, self).__init__(srsName, srsDimension, axisLabels, uomLabels, lowerCorner, upperCorner, coord, pos, coordinates, extensiontype_, )
supermod.EnvelopeType.subclass = EnvelopeTypeSub
# end class EnvelopeTypeSub


class CoordTypeSub(supermod.CoordType):
    def __init__(self, X=None, Y=None, Z=None):
        super(CoordTypeSub, self).__init__(X, Y, Z, )
supermod.CoordType.subclass = CoordTypeSub
# end class CoordTypeSub


class LineStringPropertyTypeSub(supermod.LineStringPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, LineString=None):
        super(LineStringPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, LineString, )
supermod.LineStringPropertyType.subclass = LineStringPropertyTypeSub
# end class LineStringPropertyTypeSub


class AngleChoiceTypeSub(supermod.AngleChoiceType):
    def __init__(self, angle=None, dmsAngle=None):
        super(AngleChoiceTypeSub, self).__init__(angle, dmsAngle, )
supermod.AngleChoiceType.subclass = AngleChoiceTypeSub
# end class AngleChoiceTypeSub


class DMSAngleTypeSub(supermod.DMSAngleType):
    def __init__(self, degrees=None, decimalMinutes=None, minutes=None, seconds=None):
        super(DMSAngleTypeSub, self).__init__(degrees, decimalMinutes, minutes, seconds, )
supermod.DMSAngleType.subclass = DMSAngleTypeSub
# end class DMSAngleTypeSub


class DegreesTypeSub(supermod.DegreesType):
    def __init__(self, direction=None, valueOf_=None):
        super(DegreesTypeSub, self).__init__(direction, valueOf_, )
supermod.DegreesType.subclass = DegreesTypeSub
# end class DegreesTypeSub


class UnitOfMeasureTypeSub(supermod.UnitOfMeasureType):
    def __init__(self, uom=None, extensiontype_=None):
        super(UnitOfMeasureTypeSub, self).__init__(uom, extensiontype_, )
supermod.UnitOfMeasureType.subclass = UnitOfMeasureTypeSub
# end class UnitOfMeasureTypeSub


class DerivationUnitTermTypeSub(supermod.DerivationUnitTermType):
    def __init__(self, uom=None, exponent=None):
        super(DerivationUnitTermTypeSub, self).__init__(uom, exponent, )
supermod.DerivationUnitTermType.subclass = DerivationUnitTermTypeSub
# end class DerivationUnitTermTypeSub


class ConversionToPreferredUnitTypeSub(supermod.ConversionToPreferredUnitType):
    def __init__(self, uom=None, factor=None, formula=None):
        super(ConversionToPreferredUnitTypeSub, self).__init__(uom, factor, formula, )
supermod.ConversionToPreferredUnitType.subclass = ConversionToPreferredUnitTypeSub
# end class ConversionToPreferredUnitTypeSub


class FormulaTypeSub(supermod.FormulaType):
    def __init__(self, a=None, b=None, c=None, d=None):
        super(FormulaTypeSub, self).__init__(a, b, c, d, )
supermod.FormulaType.subclass = FormulaTypeSub
# end class FormulaTypeSub


class DefinitionTypeSub(supermod.DefinitionType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, extensiontype_=None):
        super(DefinitionTypeSub, self).__init__(id, metaDataProperty, description, name, extensiontype_, )
supermod.DefinitionType.subclass = DefinitionTypeSub
# end class DefinitionTypeSub


class DictionaryTypeSub(supermod.DictionaryType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, dictionaryEntry=None, indirectEntry=None):
        super(DictionaryTypeSub, self).__init__(id, metaDataProperty, description, name, dictionaryEntry, indirectEntry, )
supermod.DictionaryType.subclass = DictionaryTypeSub
# end class DictionaryTypeSub


class DictionaryEntryTypeSub(supermod.DictionaryEntryType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Definition=None):
        super(DictionaryEntryTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Definition, )
supermod.DictionaryEntryType.subclass = DictionaryEntryTypeSub
# end class DictionaryEntryTypeSub


class IndirectEntryTypeSub(supermod.IndirectEntryType):
    def __init__(self, DefinitionProxy=None):
        super(IndirectEntryTypeSub, self).__init__(DefinitionProxy, )
supermod.IndirectEntryType.subclass = IndirectEntryTypeSub
# end class IndirectEntryTypeSub


class DefinitionProxyTypeSub(supermod.DefinitionProxyType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, definitionRef=None):
        super(DefinitionProxyTypeSub, self).__init__(id, metaDataProperty, description, name, definitionRef, )
supermod.DefinitionProxyType.subclass = DefinitionProxyTypeSub
# end class DefinitionProxyTypeSub


class _ObjectSub(supermod._Object):
    def __init__(self):
        super(_ObjectSub, self).__init__()
supermod._Object.subclass = _ObjectSub
# end class _ObjectSub


class AbstractGMLTypeSub(supermod.AbstractGMLType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, extensiontype_=None):
        super(AbstractGMLTypeSub, self).__init__(id, metaDataProperty, description, name, extensiontype_, )
supermod.AbstractGMLType.subclass = AbstractGMLTypeSub
# end class AbstractGMLTypeSub


class BagTypeSub(supermod.BagType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, member=None, members=None):
        super(BagTypeSub, self).__init__(id, metaDataProperty, description, name, member, members, )
supermod.BagType.subclass = BagTypeSub
# end class BagTypeSub


class ArrayTypeSub(supermod.ArrayType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, members=None):
        super(ArrayTypeSub, self).__init__(id, metaDataProperty, description, name, members, )
supermod.ArrayType.subclass = ArrayTypeSub
# end class ArrayTypeSub


class AbstractMetaDataTypeSub(supermod.AbstractMetaDataType):
    def __init__(self, id=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None):
        super(AbstractMetaDataTypeSub, self).__init__(id, valueOf_, mixedclass_, content_, extensiontype_, )
supermod.AbstractMetaDataType.subclass = AbstractMetaDataTypeSub
# end class AbstractMetaDataTypeSub


class GenericMetaDataTypeSub(supermod.GenericMetaDataType):
    def __init__(self, id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(GenericMetaDataTypeSub, self).__init__(id, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.GenericMetaDataType.subclass = GenericMetaDataTypeSub
# end class GenericMetaDataTypeSub


class AssociationTypeSub(supermod.AssociationType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Object=None):
        super(AssociationTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Object, )
supermod.AssociationType.subclass = AssociationTypeSub
# end class AssociationTypeSub


class ReferenceTypeSub(supermod.ReferenceType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None):
        super(ReferenceTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, )
supermod.ReferenceType.subclass = ReferenceTypeSub
# end class ReferenceTypeSub


class ArrayAssociationTypeSub(supermod.ArrayAssociationType):
    def __init__(self, _Object=None):
        super(ArrayAssociationTypeSub, self).__init__(_Object, )
supermod.ArrayAssociationType.subclass = ArrayAssociationTypeSub
# end class ArrayAssociationTypeSub


class MetaDataPropertyTypeSub(supermod.MetaDataPropertyType):
    def __init__(self, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, anytypeobjs_=None):
        super(MetaDataPropertyTypeSub, self).__init__(about, type_, href, role, arcrole, title, show, actuate, remoteSchema, anytypeobjs_, )
supermod.MetaDataPropertyType.subclass = MetaDataPropertyTypeSub
# end class MetaDataPropertyTypeSub


class StringOrRefTypeSub(supermod.StringOrRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, valueOf_=None):
        super(StringOrRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, valueOf_, )
supermod.StringOrRefType.subclass = StringOrRefTypeSub
# end class StringOrRefTypeSub


class CodeTypeSub(supermod.CodeType):
    def __init__(self, codeSpace=None, valueOf_=None):
        super(CodeTypeSub, self).__init__(codeSpace, valueOf_, )
supermod.CodeType.subclass = CodeTypeSub
# end class CodeTypeSub


class CodeListTypeSub(supermod.CodeListType):
    def __init__(self, codeSpace=None, valueOf_=None):
        super(CodeListTypeSub, self).__init__(codeSpace, valueOf_, )
supermod.CodeListType.subclass = CodeListTypeSub
# end class CodeListTypeSub


class CodeOrNullListTypeSub(supermod.CodeOrNullListType):
    def __init__(self, codeSpace=None, valueOf_=None, extensiontype_=None):
        super(CodeOrNullListTypeSub, self).__init__(codeSpace, valueOf_, extensiontype_, )
supermod.CodeOrNullListType.subclass = CodeOrNullListTypeSub
# end class CodeOrNullListTypeSub


class MeasureTypeSub(supermod.MeasureType):
    def __init__(self, uom=None, valueOf_=None, extensiontype_=None):
        super(MeasureTypeSub, self).__init__(uom, valueOf_, extensiontype_, )
supermod.MeasureType.subclass = MeasureTypeSub
# end class MeasureTypeSub


class MeasureListTypeSub(supermod.MeasureListType):
    def __init__(self, uom=None, valueOf_=None):
        super(MeasureListTypeSub, self).__init__(uom, valueOf_, )
supermod.MeasureListType.subclass = MeasureListTypeSub
# end class MeasureListTypeSub


class MeasureOrNullListTypeSub(supermod.MeasureOrNullListType):
    def __init__(self, uom=None, valueOf_=None, extensiontype_=None):
        super(MeasureOrNullListTypeSub, self).__init__(uom, valueOf_, extensiontype_, )
supermod.MeasureOrNullListType.subclass = MeasureOrNullListTypeSub
# end class MeasureOrNullListTypeSub


class CoordinatesTypeSub(supermod.CoordinatesType):
    def __init__(self, decimal='.', cs=',', ts=' ', valueOf_=None):
        super(CoordinatesTypeSub, self).__init__(decimal, cs, ts, valueOf_, )
supermod.CoordinatesType.subclass = CoordinatesTypeSub
# end class CoordinatesTypeSub


class simpleSub(supermod.simple):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(simpleSub, self).__init__(type_, href, role, arcrole, title, show, actuate, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.simple.subclass = simpleSub
# end class simpleSub


class extendedSub(supermod.extended):
    def __init__(self, type_=None, role=None, title_attr=None, title=None, resource=None, locator=None, arc=None):
        super(extendedSub, self).__init__(type_, role, title_attr, title, resource, locator, arc, )
supermod.extended.subclass = extendedSub
# end class extendedSub


class titleEltTypeSub(supermod.titleEltType):
    def __init__(self, type_=None, lang=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(titleEltTypeSub, self).__init__(type_, lang, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.titleEltType.subclass = titleEltTypeSub
# end class titleEltTypeSub


class resourceTypeSub(supermod.resourceType):
    def __init__(self, type_=None, role=None, title=None, label=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(resourceTypeSub, self).__init__(type_, role, title, label, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.resourceType.subclass = resourceTypeSub
# end class resourceTypeSub


class locatorTypeSub(supermod.locatorType):
    def __init__(self, type_=None, href=None, role=None, title_attr=None, label=None, title=None):
        super(locatorTypeSub, self).__init__(type_, href, role, title_attr, label, title, )
supermod.locatorType.subclass = locatorTypeSub
# end class locatorTypeSub


class arcTypeSub(supermod.arcType):
    def __init__(self, type_=None, arcrole=None, title_attr=None, show=None, actuate=None, from_=None, to=None, title=None):
        super(arcTypeSub, self).__init__(type_, arcrole, title_attr, show, actuate, from_, to, title, )
supermod.arcType.subclass = arcTypeSub
# end class arcTypeSub


class AbstractTopologyTypeSub(supermod.AbstractTopologyType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, extensiontype_=None):
        super(AbstractTopologyTypeSub, self).__init__(id, metaDataProperty, description, name, extensiontype_, )
supermod.AbstractTopologyType.subclass = AbstractTopologyTypeSub
# end class AbstractTopologyTypeSub


class AbstractTopoPrimitiveTypeSub(supermod.AbstractTopoPrimitiveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, isolated=None, container=None, extensiontype_=None):
        super(AbstractTopoPrimitiveTypeSub, self).__init__(id, metaDataProperty, description, name, isolated, container, extensiontype_, )
supermod.AbstractTopoPrimitiveType.subclass = AbstractTopoPrimitiveTypeSub
# end class AbstractTopoPrimitiveTypeSub


class IsolatedPropertyTypeSub(supermod.IsolatedPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Node=None, Edge=None):
        super(IsolatedPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Node, Edge, )
supermod.IsolatedPropertyType.subclass = IsolatedPropertyTypeSub
# end class IsolatedPropertyTypeSub


class ContainerPropertyTypeSub(supermod.ContainerPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Face=None, TopoSolid=None):
        super(ContainerPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Face, TopoSolid, )
supermod.ContainerPropertyType.subclass = ContainerPropertyTypeSub
# end class ContainerPropertyTypeSub


class NodeTypeSub(supermod.NodeType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, isolated=None, container=None, directedEdge=None, pointProperty=None):
        super(NodeTypeSub, self).__init__(id, metaDataProperty, description, name, isolated, container, directedEdge, pointProperty, )
supermod.NodeType.subclass = NodeTypeSub
# end class NodeTypeSub


class DirectedNodePropertyTypeSub(supermod.DirectedNodePropertyType):
    def __init__(self, orientation='+', type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Node=None):
        super(DirectedNodePropertyTypeSub, self).__init__(orientation, type_, href, role, arcrole, title, show, actuate, remoteSchema, Node, )
supermod.DirectedNodePropertyType.subclass = DirectedNodePropertyTypeSub
# end class DirectedNodePropertyTypeSub


class EdgeTypeSub(supermod.EdgeType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, isolated=None, container=None, directedNode=None, directedFace=None, curveProperty=None):
        super(EdgeTypeSub, self).__init__(id, metaDataProperty, description, name, isolated, container, directedNode, directedFace, curveProperty, )
supermod.EdgeType.subclass = EdgeTypeSub
# end class EdgeTypeSub


class DirectedEdgePropertyTypeSub(supermod.DirectedEdgePropertyType):
    def __init__(self, orientation='+', type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Edge=None):
        super(DirectedEdgePropertyTypeSub, self).__init__(orientation, type_, href, role, arcrole, title, show, actuate, remoteSchema, Edge, )
supermod.DirectedEdgePropertyType.subclass = DirectedEdgePropertyTypeSub
# end class DirectedEdgePropertyTypeSub


class FaceTypeSub(supermod.FaceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, isolated=None, container=None, directedEdge=None, directedTopoSolid=None, surfaceProperty=None):
        super(FaceTypeSub, self).__init__(id, metaDataProperty, description, name, isolated, container, directedEdge, directedTopoSolid, surfaceProperty, )
supermod.FaceType.subclass = FaceTypeSub
# end class FaceTypeSub


class DirectedFacePropertyTypeSub(supermod.DirectedFacePropertyType):
    def __init__(self, orientation='+', type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Face=None):
        super(DirectedFacePropertyTypeSub, self).__init__(orientation, type_, href, role, arcrole, title, show, actuate, remoteSchema, Face, )
supermod.DirectedFacePropertyType.subclass = DirectedFacePropertyTypeSub
# end class DirectedFacePropertyTypeSub


class TopoSolidTypeSub(supermod.TopoSolidType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, isolated=None, container=None, directedFace=None):
        super(TopoSolidTypeSub, self).__init__(id, metaDataProperty, description, name, isolated, container, directedFace, )
supermod.TopoSolidType.subclass = TopoSolidTypeSub
# end class TopoSolidTypeSub


class DirectedTopoSolidPropertyTypeSub(supermod.DirectedTopoSolidPropertyType):
    def __init__(self, orientation='+', type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TopoSolid=None):
        super(DirectedTopoSolidPropertyTypeSub, self).__init__(orientation, type_, href, role, arcrole, title, show, actuate, remoteSchema, TopoSolid, )
supermod.DirectedTopoSolidPropertyType.subclass = DirectedTopoSolidPropertyTypeSub
# end class DirectedTopoSolidPropertyTypeSub


class TopoPointTypeSub(supermod.TopoPointType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, directedNode=None):
        super(TopoPointTypeSub, self).__init__(id, metaDataProperty, description, name, directedNode, )
supermod.TopoPointType.subclass = TopoPointTypeSub
# end class TopoPointTypeSub


class TopoPointPropertyTypeSub(supermod.TopoPointPropertyType):
    def __init__(self, TopoPoint=None):
        super(TopoPointPropertyTypeSub, self).__init__(TopoPoint, )
supermod.TopoPointPropertyType.subclass = TopoPointPropertyTypeSub
# end class TopoPointPropertyTypeSub


class TopoCurveTypeSub(supermod.TopoCurveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, directedEdge=None):
        super(TopoCurveTypeSub, self).__init__(id, metaDataProperty, description, name, directedEdge, )
supermod.TopoCurveType.subclass = TopoCurveTypeSub
# end class TopoCurveTypeSub


class TopoCurvePropertyTypeSub(supermod.TopoCurvePropertyType):
    def __init__(self, TopoCurve=None):
        super(TopoCurvePropertyTypeSub, self).__init__(TopoCurve, )
supermod.TopoCurvePropertyType.subclass = TopoCurvePropertyTypeSub
# end class TopoCurvePropertyTypeSub


class TopoSurfaceTypeSub(supermod.TopoSurfaceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, directedFace=None):
        super(TopoSurfaceTypeSub, self).__init__(id, metaDataProperty, description, name, directedFace, )
supermod.TopoSurfaceType.subclass = TopoSurfaceTypeSub
# end class TopoSurfaceTypeSub


class TopoSurfacePropertyTypeSub(supermod.TopoSurfacePropertyType):
    def __init__(self, TopoSurface=None):
        super(TopoSurfacePropertyTypeSub, self).__init__(TopoSurface, )
supermod.TopoSurfacePropertyType.subclass = TopoSurfacePropertyTypeSub
# end class TopoSurfacePropertyTypeSub


class TopoVolumeTypeSub(supermod.TopoVolumeType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, directedTopoSolid=None):
        super(TopoVolumeTypeSub, self).__init__(id, metaDataProperty, description, name, directedTopoSolid, )
supermod.TopoVolumeType.subclass = TopoVolumeTypeSub
# end class TopoVolumeTypeSub


class TopoVolumePropertyTypeSub(supermod.TopoVolumePropertyType):
    def __init__(self, TopoVolume=None):
        super(TopoVolumePropertyTypeSub, self).__init__(TopoVolume, )
supermod.TopoVolumePropertyType.subclass = TopoVolumePropertyTypeSub
# end class TopoVolumePropertyTypeSub


class TopoComplexTypeSub(supermod.TopoComplexType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, isMaximal='false', maximalComplex=None, superComplex=None, subComplex=None, topoPrimitiveMember=None, topoPrimitiveMembers=None):
        super(TopoComplexTypeSub, self).__init__(id, metaDataProperty, description, name, isMaximal, maximalComplex, superComplex, subComplex, topoPrimitiveMember, topoPrimitiveMembers, )
supermod.TopoComplexType.subclass = TopoComplexTypeSub
# end class TopoComplexTypeSub


class TopoComplexMemberTypeSub(supermod.TopoComplexMemberType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TopoComplex=None):
        super(TopoComplexMemberTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TopoComplex, )
supermod.TopoComplexMemberType.subclass = TopoComplexMemberTypeSub
# end class TopoComplexMemberTypeSub


class TopoPrimitiveMemberTypeSub(supermod.TopoPrimitiveMemberType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _TopoPrimitive=None):
        super(TopoPrimitiveMemberTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _TopoPrimitive, )
supermod.TopoPrimitiveMemberType.subclass = TopoPrimitiveMemberTypeSub
# end class TopoPrimitiveMemberTypeSub


class TopoPrimitiveArrayAssociationTypeSub(supermod.TopoPrimitiveArrayAssociationType):
    def __init__(self, _TopoPrimitive=None):
        super(TopoPrimitiveArrayAssociationTypeSub, self).__init__(_TopoPrimitive, )
supermod.TopoPrimitiveArrayAssociationType.subclass = TopoPrimitiveArrayAssociationTypeSub
# end class TopoPrimitiveArrayAssociationTypeSub


class CompositeCurvePropertyTypeSub(supermod.CompositeCurvePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, CompositeCurve=None):
        super(CompositeCurvePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, CompositeCurve, )
supermod.CompositeCurvePropertyType.subclass = CompositeCurvePropertyTypeSub
# end class CompositeCurvePropertyTypeSub


class CompositeSurfacePropertyTypeSub(supermod.CompositeSurfacePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, CompositeSurface=None):
        super(CompositeSurfacePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, CompositeSurface, )
supermod.CompositeSurfacePropertyType.subclass = CompositeSurfacePropertyTypeSub
# end class CompositeSurfacePropertyTypeSub


class CompositeSolidPropertyTypeSub(supermod.CompositeSolidPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, CompositeSolid=None):
        super(CompositeSolidPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, CompositeSolid, )
supermod.CompositeSolidPropertyType.subclass = CompositeSolidPropertyTypeSub
# end class CompositeSolidPropertyTypeSub


class GeometricComplexPropertyTypeSub(supermod.GeometricComplexPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, GeometricComplex=None, CompositeCurve=None, CompositeSurface=None, CompositeSolid=None):
        super(GeometricComplexPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, GeometricComplex, CompositeCurve, CompositeSurface, CompositeSolid, )
supermod.GeometricComplexPropertyType.subclass = GeometricComplexPropertyTypeSub
# end class GeometricComplexPropertyTypeSub


class MultiGeometryPropertyTypeSub(supermod.MultiGeometryPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _GeometricAggregate=None):
        super(MultiGeometryPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _GeometricAggregate, )
supermod.MultiGeometryPropertyType.subclass = MultiGeometryPropertyTypeSub
# end class MultiGeometryPropertyTypeSub


class MultiPointPropertyTypeSub(supermod.MultiPointPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiPoint=None):
        super(MultiPointPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiPoint, )
supermod.MultiPointPropertyType.subclass = MultiPointPropertyTypeSub
# end class MultiPointPropertyTypeSub


class MultiCurvePropertyTypeSub(supermod.MultiCurvePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiCurve=None):
        super(MultiCurvePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiCurve, )
supermod.MultiCurvePropertyType.subclass = MultiCurvePropertyTypeSub
# end class MultiCurvePropertyTypeSub


class MultiSurfacePropertyTypeSub(supermod.MultiSurfacePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiSurface=None):
        super(MultiSurfacePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiSurface, )
supermod.MultiSurfacePropertyType.subclass = MultiSurfacePropertyTypeSub
# end class MultiSurfacePropertyTypeSub


class MultiSolidPropertyTypeSub(supermod.MultiSolidPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiSolid=None):
        super(MultiSolidPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiSolid, )
supermod.MultiSolidPropertyType.subclass = MultiSolidPropertyTypeSub
# end class MultiSolidPropertyTypeSub


class MultiLineStringPropertyTypeSub(supermod.MultiLineStringPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiLineString=None):
        super(MultiLineStringPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiLineString, )
supermod.MultiLineStringPropertyType.subclass = MultiLineStringPropertyTypeSub
# end class MultiLineStringPropertyTypeSub


class MultiPolygonPropertyTypeSub(supermod.MultiPolygonPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiPolygon=None):
        super(MultiPolygonPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiPolygon, )
supermod.MultiPolygonPropertyType.subclass = MultiPolygonPropertyTypeSub
# end class MultiPolygonPropertyTypeSub


class AbstractCurveSegmentTypeSub(supermod.AbstractCurveSegmentType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', extensiontype_=None):
        super(AbstractCurveSegmentTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, extensiontype_, )
supermod.AbstractCurveSegmentType.subclass = AbstractCurveSegmentTypeSub
# end class AbstractCurveSegmentTypeSub


class CurveSegmentArrayPropertyTypeSub(supermod.CurveSegmentArrayPropertyType):
    def __init__(self, _CurveSegment=None):
        super(CurveSegmentArrayPropertyTypeSub, self).__init__(_CurveSegment, )
supermod.CurveSegmentArrayPropertyType.subclass = CurveSegmentArrayPropertyTypeSub
# end class CurveSegmentArrayPropertyTypeSub


class LineStringSegmentTypeSub(supermod.LineStringSegmentType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None):
        super(LineStringSegmentTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, pos, pointProperty, pointRep, posList, coordinates, )
supermod.LineStringSegmentType.subclass = LineStringSegmentTypeSub
# end class LineStringSegmentTypeSub


class ArcStringTypeSub(supermod.ArcStringType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation=None, numArc=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None):
        super(ArcStringTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, numArc, pos, pointProperty, pointRep, posList, coordinates, )
supermod.ArcStringType.subclass = ArcStringTypeSub
# end class ArcStringTypeSub


class ArcTypeSub(supermod.ArcType):
    def __init__(self, numArc=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, extensiontype_=None):
        super(ArcTypeSub, self).__init__(numArc, pos, pointProperty, pointRep, posList, coordinates, extensiontype_, )
supermod.ArcType.subclass = ArcTypeSub
# end class ArcTypeSub


class CircleTypeSub(supermod.CircleType):
    def __init__(self, numArc=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None):
        super(CircleTypeSub, self).__init__(numArc, pos, pointProperty, pointRep, posList, coordinates, )
supermod.CircleType.subclass = CircleTypeSub
# end class CircleTypeSub


class ArcStringByBulgeTypeSub(supermod.ArcStringByBulgeType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation=None, numArc=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, bulge=None, normal=None):
        super(ArcStringByBulgeTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, numArc, pos, pointProperty, pointRep, posList, coordinates, bulge, normal, )
supermod.ArcStringByBulgeType.subclass = ArcStringByBulgeTypeSub
# end class ArcStringByBulgeTypeSub


class ArcByBulgeTypeSub(supermod.ArcByBulgeType):
    def __init__(self, numArc=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, bulge=None, normal=None):
        super(ArcByBulgeTypeSub, self).__init__(numArc, pos, pointProperty, pointRep, posList, coordinates, bulge, normal, )
supermod.ArcByBulgeType.subclass = ArcByBulgeTypeSub
# end class ArcByBulgeTypeSub


class ArcByCenterPointTypeSub(supermod.ArcByCenterPointType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation=None, numArc=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, radius=None, startAngle=None, endAngle=None, extensiontype_=None):
        super(ArcByCenterPointTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, numArc, pos, pointProperty, pointRep, posList, coordinates, radius, startAngle, endAngle, extensiontype_, )
supermod.ArcByCenterPointType.subclass = ArcByCenterPointTypeSub
# end class ArcByCenterPointTypeSub


class CircleByCenterPointTypeSub(supermod.CircleByCenterPointType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation=None, numArc=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, radius=None, startAngle=None, endAngle=None):
        super(CircleByCenterPointTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, numArc, pos, pointProperty, pointRep, posList, coordinates, radius, startAngle, endAngle, )
supermod.CircleByCenterPointType.subclass = CircleByCenterPointTypeSub
# end class CircleByCenterPointTypeSub


class OffsetCurveTypeSub(supermod.OffsetCurveType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', offsetBase=None, distance=None, refDirection=None):
        super(OffsetCurveTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, offsetBase, distance, refDirection, )
supermod.OffsetCurveType.subclass = OffsetCurveTypeSub
# end class OffsetCurveTypeSub


class AffinePlacementTypeSub(supermod.AffinePlacementType):
    def __init__(self, location=None, refDirection=None, inDimension=None, outDimension=None):
        super(AffinePlacementTypeSub, self).__init__(location, refDirection, inDimension, outDimension, )
supermod.AffinePlacementType.subclass = AffinePlacementTypeSub
# end class AffinePlacementTypeSub


class ClothoidTypeSub(supermod.ClothoidType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', refLocation=None, scaleFactor=None, startParameter=None, endParameter=None):
        super(ClothoidTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, refLocation, scaleFactor, startParameter, endParameter, )
supermod.ClothoidType.subclass = ClothoidTypeSub
# end class ClothoidTypeSub


class GeodesicStringTypeSub(supermod.GeodesicStringType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation=None, posList=None, pos=None, pointProperty=None, extensiontype_=None):
        super(GeodesicStringTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, posList, pos, pointProperty, extensiontype_, )
supermod.GeodesicStringType.subclass = GeodesicStringTypeSub
# end class GeodesicStringTypeSub


class GeodesicTypeSub(supermod.GeodesicType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation=None, posList=None, pos=None, pointProperty=None):
        super(GeodesicTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, posList, pos, pointProperty, )
supermod.GeodesicType.subclass = GeodesicTypeSub
# end class GeodesicTypeSub


class CubicSplineTypeSub(supermod.CubicSplineType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation=None, degree=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, vectorAtStart=None, vectorAtEnd=None):
        super(CubicSplineTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, degree, pos, pointProperty, pointRep, posList, coordinates, vectorAtStart, vectorAtEnd, )
supermod.CubicSplineType.subclass = CubicSplineTypeSub
# end class CubicSplineTypeSub


class KnotTypeSub(supermod.KnotType):
    def __init__(self, value=None, multiplicity=None, weight=None):
        super(KnotTypeSub, self).__init__(value, multiplicity, weight, )
supermod.KnotType.subclass = KnotTypeSub
# end class KnotTypeSub


class KnotPropertyTypeSub(supermod.KnotPropertyType):
    def __init__(self, Knot=None):
        super(KnotPropertyTypeSub, self).__init__(Knot, )
supermod.KnotPropertyType.subclass = KnotPropertyTypeSub
# end class KnotPropertyTypeSub


class BSplineTypeSub(supermod.BSplineType):
    def __init__(self, numDerivativesAtStart='0', numDerivativesAtEnd='0', numDerivativeInterior='0', interpolation='polynomialSpline', isPolynomial=None, knotType=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, degree=None, knot=None):
        super(BSplineTypeSub, self).__init__(numDerivativesAtStart, numDerivativesAtEnd, numDerivativeInterior, interpolation, isPolynomial, knotType, pos, pointProperty, pointRep, posList, coordinates, degree, knot, )
supermod.BSplineType.subclass = BSplineTypeSub
# end class BSplineTypeSub


class BezierTypeSub(supermod.BezierType):
    def __init__(self, interpolation=None, isPolynomial=None, knotType=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, degree=None, knot=None):
        super(BezierTypeSub, self).__init__(interpolation, isPolynomial, knotType, pos, pointProperty, pointRep, posList, coordinates, degree, knot, )
supermod.BezierType.subclass = BezierTypeSub
# end class BezierTypeSub


class AbstractSurfacePatchTypeSub(supermod.AbstractSurfacePatchType):
    def __init__(self, extensiontype_=None):
        super(AbstractSurfacePatchTypeSub, self).__init__(extensiontype_, )
supermod.AbstractSurfacePatchType.subclass = AbstractSurfacePatchTypeSub
# end class AbstractSurfacePatchTypeSub


class SurfacePatchArrayPropertyTypeSub(supermod.SurfacePatchArrayPropertyType):
    def __init__(self, _SurfacePatch=None):
        super(SurfacePatchArrayPropertyTypeSub, self).__init__(_SurfacePatch, )
supermod.SurfacePatchArrayPropertyType.subclass = SurfacePatchArrayPropertyTypeSub
# end class SurfacePatchArrayPropertyTypeSub


class PolygonPatchTypeSub(supermod.PolygonPatchType):
    def __init__(self, interpolation=None, exterior=None, interior=None):
        super(PolygonPatchTypeSub, self).__init__(interpolation, exterior, interior, )
supermod.PolygonPatchType.subclass = PolygonPatchTypeSub
# end class PolygonPatchTypeSub


class TriangleTypeSub(supermod.TriangleType):
    def __init__(self, interpolation=None, exterior=None):
        super(TriangleTypeSub, self).__init__(interpolation, exterior, )
supermod.TriangleType.subclass = TriangleTypeSub
# end class TriangleTypeSub


class RectangleTypeSub(supermod.RectangleType):
    def __init__(self, interpolation=None, exterior=None):
        super(RectangleTypeSub, self).__init__(interpolation, exterior, )
supermod.RectangleType.subclass = RectangleTypeSub
# end class RectangleTypeSub


class RingPropertyTypeSub(supermod.RingPropertyType):
    def __init__(self, Ring=None):
        super(RingPropertyTypeSub, self).__init__(Ring, )
supermod.RingPropertyType.subclass = RingPropertyTypeSub
# end class RingPropertyTypeSub


class AbstractParametricCurveSurfaceTypeSub(supermod.AbstractParametricCurveSurfaceType):
    def __init__(self, extensiontype_=None):
        super(AbstractParametricCurveSurfaceTypeSub, self).__init__(extensiontype_, )
supermod.AbstractParametricCurveSurfaceType.subclass = AbstractParametricCurveSurfaceTypeSub
# end class AbstractParametricCurveSurfaceTypeSub


class AbstractGriddedSurfaceTypeSub(supermod.AbstractGriddedSurfaceType):
    def __init__(self, row=None, rows=None, columns=None, extensiontype_=None):
        super(AbstractGriddedSurfaceTypeSub, self).__init__(row, rows, columns, extensiontype_, )
supermod.AbstractGriddedSurfaceType.subclass = AbstractGriddedSurfaceTypeSub
# end class AbstractGriddedSurfaceTypeSub


class ConeTypeSub(supermod.ConeType):
    def __init__(self, row=None, rows=None, columns=None, horizontalCurveType=None, verticalCurveType=None):
        super(ConeTypeSub, self).__init__(row, rows, columns, horizontalCurveType, verticalCurveType, )
supermod.ConeType.subclass = ConeTypeSub
# end class ConeTypeSub


class CylinderTypeSub(supermod.CylinderType):
    def __init__(self, row=None, rows=None, columns=None, horizontalCurveType=None, verticalCurveType=None):
        super(CylinderTypeSub, self).__init__(row, rows, columns, horizontalCurveType, verticalCurveType, )
supermod.CylinderType.subclass = CylinderTypeSub
# end class CylinderTypeSub


class SphereTypeSub(supermod.SphereType):
    def __init__(self, row=None, rows=None, columns=None, horizontalCurveType=None, verticalCurveType=None):
        super(SphereTypeSub, self).__init__(row, rows, columns, horizontalCurveType, verticalCurveType, )
supermod.SphereType.subclass = SphereTypeSub
# end class SphereTypeSub


class PolyhedralSurfaceTypeSub(supermod.PolyhedralSurfaceType):
    def __init__(self, metaDataProperty=None, description=None, name=None, polygonPatches=None):
        super(PolyhedralSurfaceTypeSub, self).__init__(metaDataProperty, description, name, polygonPatches, )
supermod.PolyhedralSurfaceType.subclass = PolyhedralSurfaceTypeSub
# end class PolyhedralSurfaceTypeSub


class PolygonPatchArrayPropertyTypeSub(supermod.PolygonPatchArrayPropertyType):
    def __init__(self, PolygonPatch=None):
        super(PolygonPatchArrayPropertyTypeSub, self).__init__(PolygonPatch, )
supermod.PolygonPatchArrayPropertyType.subclass = PolygonPatchArrayPropertyTypeSub
# end class PolygonPatchArrayPropertyTypeSub


class TrianglePatchArrayPropertyTypeSub(supermod.TrianglePatchArrayPropertyType):
    def __init__(self, Triangle=None):
        super(TrianglePatchArrayPropertyTypeSub, self).__init__(Triangle, )
supermod.TrianglePatchArrayPropertyType.subclass = TrianglePatchArrayPropertyTypeSub
# end class TrianglePatchArrayPropertyTypeSub


class TriangulatedSurfaceTypeSub(supermod.TriangulatedSurfaceType):
    def __init__(self, metaDataProperty=None, description=None, name=None, trianglePatches=None, extensiontype_=None):
        super(TriangulatedSurfaceTypeSub, self).__init__(metaDataProperty, description, name, trianglePatches, extensiontype_, )
supermod.TriangulatedSurfaceType.subclass = TriangulatedSurfaceTypeSub
# end class TriangulatedSurfaceTypeSub


class TinTypeSub(supermod.TinType):
    def __init__(self, metaDataProperty=None, description=None, name=None, trianglePatches=None, stopLines=None, breakLines=None, maxLength=None, controlPoint=None):
        super(TinTypeSub, self).__init__(metaDataProperty, description, name, trianglePatches, stopLines, breakLines, maxLength, controlPoint, )
supermod.TinType.subclass = TinTypeSub
# end class TinTypeSub


class LineStringSegmentArrayPropertyTypeSub(supermod.LineStringSegmentArrayPropertyType):
    def __init__(self, LineStringSegment=None):
        super(LineStringSegmentArrayPropertyTypeSub, self).__init__(LineStringSegment, )
supermod.LineStringSegmentArrayPropertyType.subclass = LineStringSegmentArrayPropertyTypeSub
# end class LineStringSegmentArrayPropertyTypeSub


class SolidPropertyTypeSub(supermod.SolidPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Solid=None):
        super(SolidPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Solid, )
supermod.SolidPropertyType.subclass = SolidPropertyTypeSub
# end class SolidPropertyTypeSub


class SolidArrayPropertyTypeSub(supermod.SolidArrayPropertyType):
    def __init__(self, _Solid=None):
        super(SolidArrayPropertyTypeSub, self).__init__(_Solid, )
supermod.SolidArrayPropertyType.subclass = SolidArrayPropertyTypeSub
# end class SolidArrayPropertyTypeSub


class SurfacePropertyTypeSub(supermod.SurfacePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Surface=None):
        super(SurfacePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Surface, )
supermod.SurfacePropertyType.subclass = SurfacePropertyTypeSub
# end class SurfacePropertyTypeSub


class SurfaceArrayPropertyTypeSub(supermod.SurfaceArrayPropertyType):
    def __init__(self, _Surface=None):
        super(SurfaceArrayPropertyTypeSub, self).__init__(_Surface, )
supermod.SurfaceArrayPropertyType.subclass = SurfaceArrayPropertyTypeSub
# end class SurfaceArrayPropertyTypeSub


class AbstractRingPropertyTypeSub(supermod.AbstractRingPropertyType):
    def __init__(self, _Ring=None):
        super(AbstractRingPropertyTypeSub, self).__init__(_Ring, )
supermod.AbstractRingPropertyType.subclass = AbstractRingPropertyTypeSub
# end class AbstractRingPropertyTypeSub


class LinearRingPropertyTypeSub(supermod.LinearRingPropertyType):
    def __init__(self, LinearRing=None):
        super(LinearRingPropertyTypeSub, self).__init__(LinearRing, )
supermod.LinearRingPropertyType.subclass = LinearRingPropertyTypeSub
# end class LinearRingPropertyTypeSub


class PolygonPropertyTypeSub(supermod.PolygonPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Polygon=None):
        super(PolygonPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Polygon, )
supermod.PolygonPropertyType.subclass = PolygonPropertyTypeSub
# end class PolygonPropertyTypeSub


class DomainSetTypeSub(supermod.DomainSetType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Geometry=None, _TimeObject=None):
        super(DomainSetTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Geometry, _TimeObject, )
supermod.DomainSetType.subclass = DomainSetTypeSub
# end class DomainSetTypeSub


class RangeSetTypeSub(supermod.RangeSetType):
    def __init__(self, ValueArray=None, BooleanList=None, CategoryList=None, QuantityList=None, CountList=None, DataBlock=None, File=None):
        super(RangeSetTypeSub, self).__init__(ValueArray, BooleanList, CategoryList, QuantityList, CountList, DataBlock, File, )
supermod.RangeSetType.subclass = RangeSetTypeSub
# end class RangeSetTypeSub


class CoverageFunctionTypeSub(supermod.CoverageFunctionType):
    def __init__(self, MappingRule=None, GridFunction=None):
        super(CoverageFunctionTypeSub, self).__init__(MappingRule, GridFunction, )
supermod.CoverageFunctionType.subclass = CoverageFunctionTypeSub
# end class CoverageFunctionTypeSub


class DataBlockTypeSub(supermod.DataBlockType):
    def __init__(self, rangeParameters=None, tupleList=None, doubleOrNullTupleList=None):
        super(DataBlockTypeSub, self).__init__(rangeParameters, tupleList, doubleOrNullTupleList, )
supermod.DataBlockType.subclass = DataBlockTypeSub
# end class DataBlockTypeSub


class FileTypeSub(supermod.FileType):
    def __init__(self, rangeParameters=None, fileName=None, fileStructure=None, mimeType=None, compression=None):
        super(FileTypeSub, self).__init__(rangeParameters, fileName, fileStructure, mimeType, compression, )
supermod.FileType.subclass = FileTypeSub
# end class FileTypeSub


class RangeParametersTypeSub(supermod.RangeParametersType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Boolean=None, Category=None, Quantity=None, Count=None, BooleanList=None, CategoryList=None, QuantityList=None, CountList=None, CategoryExtent=None, QuantityExtent=None, CountExtent=None, CompositeValue=None):
        super(RangeParametersTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Boolean, Category, Quantity, Count, BooleanList, CategoryList, QuantityList, CountList, CategoryExtent, QuantityExtent, CountExtent, CompositeValue, )
supermod.RangeParametersType.subclass = RangeParametersTypeSub
# end class RangeParametersTypeSub


class GridFunctionTypeSub(supermod.GridFunctionType):
    def __init__(self, sequenceRule=None, startPoint=None, extensiontype_=None):
        super(GridFunctionTypeSub, self).__init__(sequenceRule, startPoint, extensiontype_, )
supermod.GridFunctionType.subclass = GridFunctionTypeSub
# end class GridFunctionTypeSub


class IndexMapTypeSub(supermod.IndexMapType):
    def __init__(self, sequenceRule=None, startPoint=None, lookUpTable=None):
        super(IndexMapTypeSub, self).__init__(sequenceRule, startPoint, lookUpTable, )
supermod.IndexMapType.subclass = IndexMapTypeSub
# end class IndexMapTypeSub


class SequenceRuleTypeSub(supermod.SequenceRuleType):
    def __init__(self, order=None, valueOf_=None):
        super(SequenceRuleTypeSub, self).__init__(order, valueOf_, )
supermod.SequenceRuleType.subclass = SequenceRuleTypeSub
# end class SequenceRuleTypeSub


class MultiPointCoverageTypeSub(supermod.MultiPointCoverageType):
    def __init__(self, metaDataProperty=None, description=None, name=None, boundedBy=None, multiPointDomain=None, rangeSet=None, coverageFunction=None):
        super(MultiPointCoverageTypeSub, self).__init__(metaDataProperty, description, name, boundedBy, multiPointDomain, rangeSet, coverageFunction, )
supermod.MultiPointCoverageType.subclass = MultiPointCoverageTypeSub
# end class MultiPointCoverageTypeSub


class MultiPointDomainTypeSub(supermod.MultiPointDomainType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiPoint=None):
        super(MultiPointDomainTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiPoint, )
supermod.MultiPointDomainType.subclass = MultiPointDomainTypeSub
# end class MultiPointDomainTypeSub


class MultiCurveCoverageTypeSub(supermod.MultiCurveCoverageType):
    def __init__(self, metaDataProperty=None, description=None, name=None, boundedBy=None, multiCurveDomain=None, rangeSet=None, coverageFunction=None):
        super(MultiCurveCoverageTypeSub, self).__init__(metaDataProperty, description, name, boundedBy, multiCurveDomain, rangeSet, coverageFunction, )
supermod.MultiCurveCoverageType.subclass = MultiCurveCoverageTypeSub
# end class MultiCurveCoverageTypeSub


class MultiCurveDomainTypeSub(supermod.MultiCurveDomainType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiCurve=None):
        super(MultiCurveDomainTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiCurve, )
supermod.MultiCurveDomainType.subclass = MultiCurveDomainTypeSub
# end class MultiCurveDomainTypeSub


class MultiSurfaceCoverageTypeSub(supermod.MultiSurfaceCoverageType):
    def __init__(self, metaDataProperty=None, description=None, name=None, boundedBy=None, multiSurfaceDomain=None, rangeSet=None, coverageFunction=None):
        super(MultiSurfaceCoverageTypeSub, self).__init__(metaDataProperty, description, name, boundedBy, multiSurfaceDomain, rangeSet, coverageFunction, )
supermod.MultiSurfaceCoverageType.subclass = MultiSurfaceCoverageTypeSub
# end class MultiSurfaceCoverageTypeSub


class MultiSurfaceDomainTypeSub(supermod.MultiSurfaceDomainType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiSurface=None):
        super(MultiSurfaceDomainTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiSurface, )
supermod.MultiSurfaceDomainType.subclass = MultiSurfaceDomainTypeSub
# end class MultiSurfaceDomainTypeSub


class MultiSolidCoverageTypeSub(supermod.MultiSolidCoverageType):
    def __init__(self, metaDataProperty=None, description=None, name=None, boundedBy=None, multiSolidDomain=None, rangeSet=None, coverageFunction=None):
        super(MultiSolidCoverageTypeSub, self).__init__(metaDataProperty, description, name, boundedBy, multiSolidDomain, rangeSet, coverageFunction, )
supermod.MultiSolidCoverageType.subclass = MultiSolidCoverageTypeSub
# end class MultiSolidCoverageTypeSub


class MultiSolidDomainTypeSub(supermod.MultiSolidDomainType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, MultiSolid=None):
        super(MultiSolidDomainTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, MultiSolid, )
supermod.MultiSolidDomainType.subclass = MultiSolidDomainTypeSub
# end class MultiSolidDomainTypeSub


class GridCoverageTypeSub(supermod.GridCoverageType):
    def __init__(self, metaDataProperty=None, description=None, name=None, boundedBy=None, gridDomain=None, rangeSet=None, coverageFunction=None):
        super(GridCoverageTypeSub, self).__init__(metaDataProperty, description, name, boundedBy, gridDomain, rangeSet, coverageFunction, )
supermod.GridCoverageType.subclass = GridCoverageTypeSub
# end class GridCoverageTypeSub


class GridDomainTypeSub(supermod.GridDomainType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Grid=None):
        super(GridDomainTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Grid, )
supermod.GridDomainType.subclass = GridDomainTypeSub
# end class GridDomainTypeSub


class RectifiedGridCoverageTypeSub(supermod.RectifiedGridCoverageType):
    def __init__(self, metaDataProperty=None, description=None, name=None, boundedBy=None, rectifiedGridDomain=None, rangeSet=None, coverageFunction=None):
        super(RectifiedGridCoverageTypeSub, self).__init__(metaDataProperty, description, name, boundedBy, rectifiedGridDomain, rangeSet, coverageFunction, )
supermod.RectifiedGridCoverageType.subclass = RectifiedGridCoverageTypeSub
# end class RectifiedGridCoverageTypeSub


class RectifiedGridDomainTypeSub(supermod.RectifiedGridDomainType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, RectifiedGrid=None):
        super(RectifiedGridDomainTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, RectifiedGrid, )
supermod.RectifiedGridDomainType.subclass = RectifiedGridDomainTypeSub
# end class RectifiedGridDomainTypeSub


class CompositeValueTypeSub(supermod.CompositeValueType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, valueComponent=None, valueComponents=None, extensiontype_=None):
        super(CompositeValueTypeSub, self).__init__(id, metaDataProperty, description, name, valueComponent, valueComponents, extensiontype_, )
supermod.CompositeValueType.subclass = CompositeValueTypeSub
# end class CompositeValueTypeSub


class ValueArrayTypeSub(supermod.ValueArrayType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, valueComponent=None, valueComponents=None, codeSpace=None, uom=None):
        super(ValueArrayTypeSub, self).__init__(id, metaDataProperty, description, name, valueComponent, valueComponents, codeSpace, uom, )
supermod.ValueArrayType.subclass = ValueArrayTypeSub
# end class ValueArrayTypeSub


class QuantityExtentTypeSub(supermod.QuantityExtentType):
    def __init__(self, uom=None, valueOf_=None):
        super(QuantityExtentTypeSub, self).__init__(uom, valueOf_, )
supermod.QuantityExtentType.subclass = QuantityExtentTypeSub
# end class QuantityExtentTypeSub


class CategoryExtentTypeSub(supermod.CategoryExtentType):
    def __init__(self, codeSpace=None, valueOf_=None):
        super(CategoryExtentTypeSub, self).__init__(codeSpace, valueOf_, )
supermod.CategoryExtentType.subclass = CategoryExtentTypeSub
# end class CategoryExtentTypeSub


class ValuePropertyTypeSub(supermod.ValuePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Boolean=None, Category=None, Quantity=None, Count=None, BooleanList=None, CategoryList=None, QuantityList=None, CountList=None, CategoryExtent=None, QuantityExtent=None, CountExtent=None, CompositeValue=None, _Object=None, Null=None):
        super(ValuePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Boolean, Category, Quantity, Count, BooleanList, CategoryList, QuantityList, CountList, CategoryExtent, QuantityExtent, CountExtent, CompositeValue, _Object, Null, )
supermod.ValuePropertyType.subclass = ValuePropertyTypeSub
# end class ValuePropertyTypeSub


class ValueArrayPropertyTypeSub(supermod.ValueArrayPropertyType):
    def __init__(self, Boolean=None, Category=None, Quantity=None, Count=None, BooleanList=None, CategoryList=None, QuantityList=None, CountList=None, CategoryExtent=None, QuantityExtent=None, CountExtent=None, CompositeValue=None, _Object=None, Null=None):
        super(ValueArrayPropertyTypeSub, self).__init__(Boolean, Category, Quantity, Count, BooleanList, CategoryList, QuantityList, CountList, CategoryExtent, QuantityExtent, CountExtent, CompositeValue, _Object, Null, )
supermod.ValueArrayPropertyType.subclass = ValueArrayPropertyTypeSub
# end class ValueArrayPropertyTypeSub


class ScalarValuePropertyTypeSub(supermod.ScalarValuePropertyType):
    def __init__(self, Boolean=None, Category=None, Quantity=None, Count=None):
        super(ScalarValuePropertyTypeSub, self).__init__(Boolean, Category, Quantity, Count, )
supermod.ScalarValuePropertyType.subclass = ScalarValuePropertyTypeSub
# end class ScalarValuePropertyTypeSub


class BooleanPropertyTypeSub(supermod.BooleanPropertyType):
    def __init__(self, Boolean=None):
        super(BooleanPropertyTypeSub, self).__init__(Boolean, )
supermod.BooleanPropertyType.subclass = BooleanPropertyTypeSub
# end class BooleanPropertyTypeSub


class CategoryPropertyTypeSub(supermod.CategoryPropertyType):
    def __init__(self, Category=None):
        super(CategoryPropertyTypeSub, self).__init__(Category, )
supermod.CategoryPropertyType.subclass = CategoryPropertyTypeSub
# end class CategoryPropertyTypeSub


class QuantityPropertyTypeSub(supermod.QuantityPropertyType):
    def __init__(self, Quantity=None):
        super(QuantityPropertyTypeSub, self).__init__(Quantity, )
supermod.QuantityPropertyType.subclass = QuantityPropertyTypeSub
# end class QuantityPropertyTypeSub


class CountPropertyTypeSub(supermod.CountPropertyType):
    def __init__(self, Count=None):
        super(CountPropertyTypeSub, self).__init__(Count, )
supermod.CountPropertyType.subclass = CountPropertyTypeSub
# end class CountPropertyTypeSub


class AbstractTimeObjectTypeSub(supermod.AbstractTimeObjectType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, extensiontype_=None):
        super(AbstractTimeObjectTypeSub, self).__init__(id, metaDataProperty, description, name, extensiontype_, )
supermod.AbstractTimeObjectType.subclass = AbstractTimeObjectTypeSub
# end class AbstractTimeObjectTypeSub


class AbstractTimePrimitiveTypeSub(supermod.AbstractTimePrimitiveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, relatedTime=None, extensiontype_=None):
        super(AbstractTimePrimitiveTypeSub, self).__init__(id, metaDataProperty, description, name, relatedTime, extensiontype_, )
supermod.AbstractTimePrimitiveType.subclass = AbstractTimePrimitiveTypeSub
# end class AbstractTimePrimitiveTypeSub


class TimePrimitivePropertyTypeSub(supermod.TimePrimitivePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _TimePrimitive=None, extensiontype_=None):
        super(TimePrimitivePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _TimePrimitive, extensiontype_, )
supermod.TimePrimitivePropertyType.subclass = TimePrimitivePropertyTypeSub
# end class TimePrimitivePropertyTypeSub


class RelatedTimeTypeSub(supermod.RelatedTimeType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _TimePrimitive=None, relativePosition=None):
        super(RelatedTimeTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _TimePrimitive, relativePosition, )
supermod.RelatedTimeType.subclass = RelatedTimeTypeSub
# end class RelatedTimeTypeSub


class AbstractTimeComplexTypeSub(supermod.AbstractTimeComplexType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, extensiontype_=None):
        super(AbstractTimeComplexTypeSub, self).__init__(id, metaDataProperty, description, name, extensiontype_, )
supermod.AbstractTimeComplexType.subclass = AbstractTimeComplexTypeSub
# end class AbstractTimeComplexTypeSub


class AbstractTimeGeometricPrimitiveTypeSub(supermod.AbstractTimeGeometricPrimitiveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, relatedTime=None, frame='#ISO-8601', extensiontype_=None):
        super(AbstractTimeGeometricPrimitiveTypeSub, self).__init__(id, metaDataProperty, description, name, relatedTime, frame, extensiontype_, )
supermod.AbstractTimeGeometricPrimitiveType.subclass = AbstractTimeGeometricPrimitiveTypeSub
# end class AbstractTimeGeometricPrimitiveTypeSub


class TimeGeometricPrimitivePropertyTypeSub(supermod.TimeGeometricPrimitivePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _TimeGeometricPrimitive=None):
        super(TimeGeometricPrimitivePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _TimeGeometricPrimitive, )
supermod.TimeGeometricPrimitivePropertyType.subclass = TimeGeometricPrimitivePropertyTypeSub
# end class TimeGeometricPrimitivePropertyTypeSub


class TimeInstantTypeSub(supermod.TimeInstantType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, relatedTime=None, frame='#ISO-8601', timePosition=None):
        super(TimeInstantTypeSub, self).__init__(id, metaDataProperty, description, name, relatedTime, frame, timePosition, )
supermod.TimeInstantType.subclass = TimeInstantTypeSub
# end class TimeInstantTypeSub


class TimeInstantPropertyTypeSub(supermod.TimeInstantPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimeInstant=None):
        super(TimeInstantPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimeInstant, )
supermod.TimeInstantPropertyType.subclass = TimeInstantPropertyTypeSub
# end class TimeInstantPropertyTypeSub


class TimePeriodTypeSub(supermod.TimePeriodType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, relatedTime=None, frame='#ISO-8601', beginPosition=None, begin=None, endPosition=None, end=None, duration=None, timeInterval=None):
        super(TimePeriodTypeSub, self).__init__(id, metaDataProperty, description, name, relatedTime, frame, beginPosition, begin, endPosition, end, duration, timeInterval, )
supermod.TimePeriodType.subclass = TimePeriodTypeSub
# end class TimePeriodTypeSub


class TimePeriodPropertyTypeSub(supermod.TimePeriodPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimePeriod=None):
        super(TimePeriodPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimePeriod, )
supermod.TimePeriodPropertyType.subclass = TimePeriodPropertyTypeSub
# end class TimePeriodPropertyTypeSub


class TimeIntervalLengthTypeSub(supermod.TimeIntervalLengthType):
    def __init__(self, unit=None, radix=None, factor=None, valueOf_=None):
        super(TimeIntervalLengthTypeSub, self).__init__(unit, radix, factor, valueOf_, )
supermod.TimeIntervalLengthType.subclass = TimeIntervalLengthTypeSub
# end class TimeIntervalLengthTypeSub


class TimePositionTypeSub(supermod.TimePositionType):
    def __init__(self, frame='#ISO-8601', calendarEraName=None, indeterminatePosition=None, valueOf_=None):
        super(TimePositionTypeSub, self).__init__(frame, calendarEraName, indeterminatePosition, valueOf_, )
supermod.TimePositionType.subclass = TimePositionTypeSub
# end class TimePositionTypeSub


class GridLimitsTypeSub(supermod.GridLimitsType):
    def __init__(self, GridEnvelope=None):
        super(GridLimitsTypeSub, self).__init__(GridEnvelope, )
supermod.GridLimitsType.subclass = GridLimitsTypeSub
# end class GridLimitsTypeSub


class GridEnvelopeTypeSub(supermod.GridEnvelopeType):
    def __init__(self, low=None, high=None):
        super(GridEnvelopeTypeSub, self).__init__(low, high, )
supermod.GridEnvelopeType.subclass = GridEnvelopeTypeSub
# end class GridEnvelopeTypeSub


class CoordinateReferenceSystemRefTypeSub(supermod.CoordinateReferenceSystemRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _CoordinateReferenceSystem=None):
        super(CoordinateReferenceSystemRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _CoordinateReferenceSystem, )
supermod.CoordinateReferenceSystemRefType.subclass = CoordinateReferenceSystemRefTypeSub
# end class CoordinateReferenceSystemRefTypeSub


class CompoundCRSRefTypeSub(supermod.CompoundCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, CompoundCRS=None):
        super(CompoundCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, CompoundCRS, )
supermod.CompoundCRSRefType.subclass = CompoundCRSRefTypeSub
# end class CompoundCRSRefTypeSub


class GeographicCRSRefTypeSub(supermod.GeographicCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, GeographicCRS=None):
        super(GeographicCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, GeographicCRS, )
supermod.GeographicCRSRefType.subclass = GeographicCRSRefTypeSub
# end class GeographicCRSRefTypeSub


class VerticalCRSRefTypeSub(supermod.VerticalCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, VerticalCRS=None):
        super(VerticalCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, VerticalCRS, )
supermod.VerticalCRSRefType.subclass = VerticalCRSRefTypeSub
# end class VerticalCRSRefTypeSub


class GeocentricCRSRefTypeSub(supermod.GeocentricCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, GeocentricCRS=None):
        super(GeocentricCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, GeocentricCRS, )
supermod.GeocentricCRSRefType.subclass = GeocentricCRSRefTypeSub
# end class GeocentricCRSRefTypeSub


class ProjectedCRSRefTypeSub(supermod.ProjectedCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, ProjectedCRS=None):
        super(ProjectedCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, ProjectedCRS, )
supermod.ProjectedCRSRefType.subclass = ProjectedCRSRefTypeSub
# end class ProjectedCRSRefTypeSub


class DerivedCRSTypeTypeSub(supermod.DerivedCRSTypeType):
    def __init__(self, codeSpace=None, valueOf_=None):
        super(DerivedCRSTypeTypeSub, self).__init__(codeSpace, valueOf_, )
supermod.DerivedCRSTypeType.subclass = DerivedCRSTypeTypeSub
# end class DerivedCRSTypeTypeSub


class DerivedCRSRefTypeSub(supermod.DerivedCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, DerivedCRS=None):
        super(DerivedCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, DerivedCRS, )
supermod.DerivedCRSRefType.subclass = DerivedCRSRefTypeSub
# end class DerivedCRSRefTypeSub


class EngineeringCRSRefTypeSub(supermod.EngineeringCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, EngineeringCRS=None):
        super(EngineeringCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, EngineeringCRS, )
supermod.EngineeringCRSRefType.subclass = EngineeringCRSRefTypeSub
# end class EngineeringCRSRefTypeSub


class ImageCRSRefTypeSub(supermod.ImageCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, ImageCRS=None):
        super(ImageCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, ImageCRS, )
supermod.ImageCRSRefType.subclass = ImageCRSRefTypeSub
# end class ImageCRSRefTypeSub


class TemporalCRSRefTypeSub(supermod.TemporalCRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TemporalCRS=None):
        super(TemporalCRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TemporalCRS, )
supermod.TemporalCRSRefType.subclass = TemporalCRSRefTypeSub
# end class TemporalCRSRefTypeSub


class CoordinateSystemAxisBaseTypeSub(supermod.CoordinateSystemAxisBaseType):
    def __init__(self, id=None, metaDataProperty=None, name=None, extensiontype_=None):
        super(CoordinateSystemAxisBaseTypeSub, self).__init__(id, metaDataProperty, name, extensiontype_, )
supermod.CoordinateSystemAxisBaseType.subclass = CoordinateSystemAxisBaseTypeSub
# end class CoordinateSystemAxisBaseTypeSub


class CoordinateSystemAxisTypeSub(supermod.CoordinateSystemAxisType):
    def __init__(self, id=None, metaDataProperty=None, name=None, uom=None, axisID=None, remarks=None, axisAbbrev=None, axisDirection=None):
        super(CoordinateSystemAxisTypeSub, self).__init__(id, metaDataProperty, name, uom, axisID, remarks, axisAbbrev, axisDirection, )
supermod.CoordinateSystemAxisType.subclass = CoordinateSystemAxisTypeSub
# end class CoordinateSystemAxisTypeSub


class CoordinateSystemAxisRefTypeSub(supermod.CoordinateSystemAxisRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, CoordinateSystemAxis=None):
        super(CoordinateSystemAxisRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, CoordinateSystemAxis, )
supermod.CoordinateSystemAxisRefType.subclass = CoordinateSystemAxisRefTypeSub
# end class CoordinateSystemAxisRefTypeSub


class AbstractCoordinateSystemBaseTypeSub(supermod.AbstractCoordinateSystemBaseType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, extensiontype_=None):
        super(AbstractCoordinateSystemBaseTypeSub, self).__init__(id, metaDataProperty, csName, extensiontype_, )
supermod.AbstractCoordinateSystemBaseType.subclass = AbstractCoordinateSystemBaseTypeSub
# end class AbstractCoordinateSystemBaseTypeSub


class AbstractCoordinateSystemTypeSub(supermod.AbstractCoordinateSystemType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None, extensiontype_=None):
        super(AbstractCoordinateSystemTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, extensiontype_, )
supermod.AbstractCoordinateSystemType.subclass = AbstractCoordinateSystemTypeSub
# end class AbstractCoordinateSystemTypeSub


class CoordinateSystemRefTypeSub(supermod.CoordinateSystemRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _CoordinateSystem=None):
        super(CoordinateSystemRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _CoordinateSystem, )
supermod.CoordinateSystemRefType.subclass = CoordinateSystemRefTypeSub
# end class CoordinateSystemRefTypeSub


class EllipsoidalCSTypeSub(supermod.EllipsoidalCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(EllipsoidalCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.EllipsoidalCSType.subclass = EllipsoidalCSTypeSub
# end class EllipsoidalCSTypeSub


class EllipsoidalCSRefTypeSub(supermod.EllipsoidalCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, EllipsoidalCS=None):
        super(EllipsoidalCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, EllipsoidalCS, )
supermod.EllipsoidalCSRefType.subclass = EllipsoidalCSRefTypeSub
# end class EllipsoidalCSRefTypeSub


class CartesianCSTypeSub(supermod.CartesianCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(CartesianCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.CartesianCSType.subclass = CartesianCSTypeSub
# end class CartesianCSTypeSub


class CartesianCSRefTypeSub(supermod.CartesianCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, CartesianCS=None):
        super(CartesianCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, CartesianCS, )
supermod.CartesianCSRefType.subclass = CartesianCSRefTypeSub
# end class CartesianCSRefTypeSub


class VerticalCSTypeSub(supermod.VerticalCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(VerticalCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.VerticalCSType.subclass = VerticalCSTypeSub
# end class VerticalCSTypeSub


class VerticalCSRefTypeSub(supermod.VerticalCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, VerticalCS=None):
        super(VerticalCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, VerticalCS, )
supermod.VerticalCSRefType.subclass = VerticalCSRefTypeSub
# end class VerticalCSRefTypeSub


class TemporalCSTypeSub(supermod.TemporalCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(TemporalCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.TemporalCSType.subclass = TemporalCSTypeSub
# end class TemporalCSTypeSub


class TemporalCSRefTypeSub(supermod.TemporalCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TemporalCS=None):
        super(TemporalCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TemporalCS, )
supermod.TemporalCSRefType.subclass = TemporalCSRefTypeSub
# end class TemporalCSRefTypeSub


class LinearCSTypeSub(supermod.LinearCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(LinearCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.LinearCSType.subclass = LinearCSTypeSub
# end class LinearCSTypeSub


class LinearCSRefTypeSub(supermod.LinearCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, LinearCS=None):
        super(LinearCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, LinearCS, )
supermod.LinearCSRefType.subclass = LinearCSRefTypeSub
# end class LinearCSRefTypeSub


class UserDefinedCSTypeSub(supermod.UserDefinedCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(UserDefinedCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.UserDefinedCSType.subclass = UserDefinedCSTypeSub
# end class UserDefinedCSTypeSub


class UserDefinedCSRefTypeSub(supermod.UserDefinedCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, UserDefinedCS=None):
        super(UserDefinedCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, UserDefinedCS, )
supermod.UserDefinedCSRefType.subclass = UserDefinedCSRefTypeSub
# end class UserDefinedCSRefTypeSub


class SphericalCSTypeSub(supermod.SphericalCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(SphericalCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.SphericalCSType.subclass = SphericalCSTypeSub
# end class SphericalCSTypeSub


class SphericalCSRefTypeSub(supermod.SphericalCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, SphericalCS=None):
        super(SphericalCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, SphericalCS, )
supermod.SphericalCSRefType.subclass = SphericalCSRefTypeSub
# end class SphericalCSRefTypeSub


class PolarCSTypeSub(supermod.PolarCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(PolarCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.PolarCSType.subclass = PolarCSTypeSub
# end class PolarCSTypeSub


class PolarCSRefTypeSub(supermod.PolarCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, PolarCS=None):
        super(PolarCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, PolarCS, )
supermod.PolarCSRefType.subclass = PolarCSRefTypeSub
# end class PolarCSRefTypeSub


class CylindricalCSTypeSub(supermod.CylindricalCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(CylindricalCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.CylindricalCSType.subclass = CylindricalCSTypeSub
# end class CylindricalCSTypeSub


class CylindricalCSRefTypeSub(supermod.CylindricalCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, CylindricalCS=None):
        super(CylindricalCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, CylindricalCS, )
supermod.CylindricalCSRefType.subclass = CylindricalCSRefTypeSub
# end class CylindricalCSRefTypeSub


class ObliqueCartesianCSTypeSub(supermod.ObliqueCartesianCSType):
    def __init__(self, id=None, metaDataProperty=None, csName=None, csID=None, remarks=None, usesAxis=None):
        super(ObliqueCartesianCSTypeSub, self).__init__(id, metaDataProperty, csName, csID, remarks, usesAxis, )
supermod.ObliqueCartesianCSType.subclass = ObliqueCartesianCSTypeSub
# end class ObliqueCartesianCSTypeSub


class ObliqueCartesianCSRefTypeSub(supermod.ObliqueCartesianCSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, ObliqueCartesianCS=None):
        super(ObliqueCartesianCSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, ObliqueCartesianCS, )
supermod.ObliqueCartesianCSRefType.subclass = ObliqueCartesianCSRefTypeSub
# end class ObliqueCartesianCSRefTypeSub


class AbstractReferenceSystemBaseTypeSub(supermod.AbstractReferenceSystemBaseType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, extensiontype_=None):
        super(AbstractReferenceSystemBaseTypeSub, self).__init__(id, metaDataProperty, srsName, extensiontype_, )
supermod.AbstractReferenceSystemBaseType.subclass = AbstractReferenceSystemBaseTypeSub
# end class AbstractReferenceSystemBaseTypeSub


class AbstractReferenceSystemTypeSub(supermod.AbstractReferenceSystemType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, extensiontype_=None):
        super(AbstractReferenceSystemTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, extensiontype_, )
supermod.AbstractReferenceSystemType.subclass = AbstractReferenceSystemTypeSub
# end class AbstractReferenceSystemTypeSub


class ReferenceSystemRefTypeSub(supermod.ReferenceSystemRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _ReferenceSystem=None):
        super(ReferenceSystemRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _ReferenceSystem, )
supermod.ReferenceSystemRefType.subclass = ReferenceSystemRefTypeSub
# end class ReferenceSystemRefTypeSub


class CRSRefTypeSub(supermod.CRSRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _CRS=None):
        super(CRSRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _CRS, )
supermod.CRSRefType.subclass = CRSRefTypeSub
# end class CRSRefTypeSub


class IdentifierTypeSub(supermod.IdentifierType):
    def __init__(self, name=None, version=None, remarks=None):
        super(IdentifierTypeSub, self).__init__(name, version, remarks, )
supermod.IdentifierType.subclass = IdentifierTypeSub
# end class IdentifierTypeSub


class ExtentTypeSub(supermod.ExtentType):
    def __init__(self, description=None, boundingBox=None, boundingPolygon=None, verticalExtent=None, temporalExtent=None):
        super(ExtentTypeSub, self).__init__(description, boundingBox, boundingPolygon, verticalExtent, temporalExtent, )
supermod.ExtentType.subclass = ExtentTypeSub
# end class ExtentTypeSub


class AbstractDatumBaseTypeSub(supermod.AbstractDatumBaseType):
    def __init__(self, id=None, metaDataProperty=None, datumName=None, extensiontype_=None):
        super(AbstractDatumBaseTypeSub, self).__init__(id, metaDataProperty, datumName, extensiontype_, )
supermod.AbstractDatumBaseType.subclass = AbstractDatumBaseTypeSub
# end class AbstractDatumBaseTypeSub


class AbstractDatumTypeSub(supermod.AbstractDatumType):
    def __init__(self, id=None, metaDataProperty=None, datumName=None, datumID=None, remarks=None, anchorPoint=None, realizationEpoch=None, validArea=None, scope=None, extensiontype_=None):
        super(AbstractDatumTypeSub, self).__init__(id, metaDataProperty, datumName, datumID, remarks, anchorPoint, realizationEpoch, validArea, scope, extensiontype_, )
supermod.AbstractDatumType.subclass = AbstractDatumTypeSub
# end class AbstractDatumTypeSub


class DatumRefTypeSub(supermod.DatumRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Datum=None):
        super(DatumRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Datum, )
supermod.DatumRefType.subclass = DatumRefTypeSub
# end class DatumRefTypeSub


class EngineeringDatumTypeSub(supermod.EngineeringDatumType):
    def __init__(self, id=None, metaDataProperty=None, datumName=None, datumID=None, remarks=None, anchorPoint=None, realizationEpoch=None, validArea=None, scope=None):
        super(EngineeringDatumTypeSub, self).__init__(id, metaDataProperty, datumName, datumID, remarks, anchorPoint, realizationEpoch, validArea, scope, )
supermod.EngineeringDatumType.subclass = EngineeringDatumTypeSub
# end class EngineeringDatumTypeSub


class EngineeringDatumRefTypeSub(supermod.EngineeringDatumRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, EngineeringDatum=None):
        super(EngineeringDatumRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, EngineeringDatum, )
supermod.EngineeringDatumRefType.subclass = EngineeringDatumRefTypeSub
# end class EngineeringDatumRefTypeSub


class ImageDatumTypeSub(supermod.ImageDatumType):
    def __init__(self, id=None, metaDataProperty=None, datumName=None, datumID=None, remarks=None, anchorPoint=None, realizationEpoch=None, validArea=None, scope=None, pixelInCell=None):
        super(ImageDatumTypeSub, self).__init__(id, metaDataProperty, datumName, datumID, remarks, anchorPoint, realizationEpoch, validArea, scope, pixelInCell, )
supermod.ImageDatumType.subclass = ImageDatumTypeSub
# end class ImageDatumTypeSub


class PixelInCellTypeSub(supermod.PixelInCellType):
    def __init__(self, codeSpace=None, valueOf_=None):
        super(PixelInCellTypeSub, self).__init__(codeSpace, valueOf_, )
supermod.PixelInCellType.subclass = PixelInCellTypeSub
# end class PixelInCellTypeSub


class ImageDatumRefTypeSub(supermod.ImageDatumRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, ImageDatum=None):
        super(ImageDatumRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, ImageDatum, )
supermod.ImageDatumRefType.subclass = ImageDatumRefTypeSub
# end class ImageDatumRefTypeSub


class VerticalDatumTypeSub(supermod.VerticalDatumType):
    def __init__(self, id=None, metaDataProperty=None, datumName=None, datumID=None, remarks=None, anchorPoint=None, realizationEpoch=None, validArea=None, scope=None, verticalDatumType=None):
        super(VerticalDatumTypeSub, self).__init__(id, metaDataProperty, datumName, datumID, remarks, anchorPoint, realizationEpoch, validArea, scope, verticalDatumType, )
supermod.VerticalDatumType.subclass = VerticalDatumTypeSub
# end class VerticalDatumTypeSub


class VerticalDatumTypeTypeSub(supermod.VerticalDatumTypeType):
    def __init__(self, codeSpace=None, valueOf_=None):
        super(VerticalDatumTypeTypeSub, self).__init__(codeSpace, valueOf_, )
supermod.VerticalDatumTypeType.subclass = VerticalDatumTypeTypeSub
# end class VerticalDatumTypeTypeSub


class VerticalDatumRefTypeSub(supermod.VerticalDatumRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, VerticalDatum=None):
        super(VerticalDatumRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, VerticalDatum, )
supermod.VerticalDatumRefType.subclass = VerticalDatumRefTypeSub
# end class VerticalDatumRefTypeSub


class TemporalDatumBaseTypeSub(supermod.TemporalDatumBaseType):
    def __init__(self, id=None, metaDataProperty=None, datumName=None, datumID=None, validArea=None, scope=None, extensiontype_=None):
        super(TemporalDatumBaseTypeSub, self).__init__(id, metaDataProperty, datumName, datumID, validArea, scope, extensiontype_, )
supermod.TemporalDatumBaseType.subclass = TemporalDatumBaseTypeSub
# end class TemporalDatumBaseTypeSub


class TemporalDatumTypeSub(supermod.TemporalDatumType):
    def __init__(self, id=None, metaDataProperty=None, datumName=None, datumID=None, validArea=None, scope=None, origin=None):
        super(TemporalDatumTypeSub, self).__init__(id, metaDataProperty, datumName, datumID, validArea, scope, origin, )
supermod.TemporalDatumType.subclass = TemporalDatumTypeSub
# end class TemporalDatumTypeSub


class TemporalDatumRefTypeSub(supermod.TemporalDatumRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TemporalDatum=None):
        super(TemporalDatumRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TemporalDatum, )
supermod.TemporalDatumRefType.subclass = TemporalDatumRefTypeSub
# end class TemporalDatumRefTypeSub


class GeodeticDatumTypeSub(supermod.GeodeticDatumType):
    def __init__(self, id=None, metaDataProperty=None, datumName=None, datumID=None, remarks=None, anchorPoint=None, realizationEpoch=None, validArea=None, scope=None, usesPrimeMeridian=None, usesEllipsoid=None):
        super(GeodeticDatumTypeSub, self).__init__(id, metaDataProperty, datumName, datumID, remarks, anchorPoint, realizationEpoch, validArea, scope, usesPrimeMeridian, usesEllipsoid, )
supermod.GeodeticDatumType.subclass = GeodeticDatumTypeSub
# end class GeodeticDatumTypeSub


class GeodeticDatumRefTypeSub(supermod.GeodeticDatumRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, GeodeticDatum=None):
        super(GeodeticDatumRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, GeodeticDatum, )
supermod.GeodeticDatumRefType.subclass = GeodeticDatumRefTypeSub
# end class GeodeticDatumRefTypeSub


class PrimeMeridianBaseTypeSub(supermod.PrimeMeridianBaseType):
    def __init__(self, id=None, metaDataProperty=None, meridianName=None, extensiontype_=None):
        super(PrimeMeridianBaseTypeSub, self).__init__(id, metaDataProperty, meridianName, extensiontype_, )
supermod.PrimeMeridianBaseType.subclass = PrimeMeridianBaseTypeSub
# end class PrimeMeridianBaseTypeSub


class PrimeMeridianTypeSub(supermod.PrimeMeridianType):
    def __init__(self, id=None, metaDataProperty=None, meridianName=None, meridianID=None, remarks=None, greenwichLongitude=None):
        super(PrimeMeridianTypeSub, self).__init__(id, metaDataProperty, meridianName, meridianID, remarks, greenwichLongitude, )
supermod.PrimeMeridianType.subclass = PrimeMeridianTypeSub
# end class PrimeMeridianTypeSub


class PrimeMeridianRefTypeSub(supermod.PrimeMeridianRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, PrimeMeridian=None):
        super(PrimeMeridianRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, PrimeMeridian, )
supermod.PrimeMeridianRefType.subclass = PrimeMeridianRefTypeSub
# end class PrimeMeridianRefTypeSub


class EllipsoidBaseTypeSub(supermod.EllipsoidBaseType):
    def __init__(self, id=None, metaDataProperty=None, ellipsoidName=None, extensiontype_=None):
        super(EllipsoidBaseTypeSub, self).__init__(id, metaDataProperty, ellipsoidName, extensiontype_, )
supermod.EllipsoidBaseType.subclass = EllipsoidBaseTypeSub
# end class EllipsoidBaseTypeSub


class EllipsoidTypeSub(supermod.EllipsoidType):
    def __init__(self, id=None, metaDataProperty=None, ellipsoidName=None, ellipsoidID=None, remarks=None, semiMajorAxis=None, secondDefiningParameter=None):
        super(EllipsoidTypeSub, self).__init__(id, metaDataProperty, ellipsoidName, ellipsoidID, remarks, semiMajorAxis, secondDefiningParameter, )
supermod.EllipsoidType.subclass = EllipsoidTypeSub
# end class EllipsoidTypeSub


class EllipsoidRefTypeSub(supermod.EllipsoidRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Ellipsoid=None):
        super(EllipsoidRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Ellipsoid, )
supermod.EllipsoidRefType.subclass = EllipsoidRefTypeSub
# end class EllipsoidRefTypeSub


class SecondDefiningParameterTypeSub(supermod.SecondDefiningParameterType):
    def __init__(self, inverseFlattening=None, semiMinorAxis=None, isSphere=None):
        super(SecondDefiningParameterTypeSub, self).__init__(inverseFlattening, semiMinorAxis, isSphere, )
supermod.SecondDefiningParameterType.subclass = SecondDefiningParameterTypeSub
# end class SecondDefiningParameterTypeSub


class isSphereSub(supermod.isSphere):
    def __init__(self, valueOf_=None):
        super(isSphereSub, self).__init__()
supermod.isSphere.subclass = isSphereSub
# end class isSphereSub


class AbstractCoordinateOperationBaseTypeSub(supermod.AbstractCoordinateOperationBaseType):
    def __init__(self, id=None, metaDataProperty=None, coordinateOperationName=None, extensiontype_=None):
        super(AbstractCoordinateOperationBaseTypeSub, self).__init__(id, metaDataProperty, coordinateOperationName, extensiontype_, )
supermod.AbstractCoordinateOperationBaseType.subclass = AbstractCoordinateOperationBaseTypeSub
# end class AbstractCoordinateOperationBaseTypeSub


class AbstractCoordinateOperationTypeSub(supermod.AbstractCoordinateOperationType):
    def __init__(self, id=None, metaDataProperty=None, coordinateOperationName=None, coordinateOperationID=None, remarks=None, operationVersion=None, validArea=None, scope=None, _positionalAccuracy=None, sourceCRS=None, targetCRS=None, extensiontype_=None):
        super(AbstractCoordinateOperationTypeSub, self).__init__(id, metaDataProperty, coordinateOperationName, coordinateOperationID, remarks, operationVersion, validArea, scope, _positionalAccuracy, sourceCRS, targetCRS, extensiontype_, )
supermod.AbstractCoordinateOperationType.subclass = AbstractCoordinateOperationTypeSub
# end class AbstractCoordinateOperationTypeSub


class CoordinateOperationRefTypeSub(supermod.CoordinateOperationRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _CoordinateOperation=None):
        super(CoordinateOperationRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _CoordinateOperation, )
supermod.CoordinateOperationRefType.subclass = CoordinateOperationRefTypeSub
# end class CoordinateOperationRefTypeSub


class ConcatenatedOperationTypeSub(supermod.ConcatenatedOperationType):
    def __init__(self, id=None, metaDataProperty=None, coordinateOperationName=None, coordinateOperationID=None, remarks=None, operationVersion=None, validArea=None, scope=None, _positionalAccuracy=None, sourceCRS=None, targetCRS=None, usesSingleOperation=None):
        super(ConcatenatedOperationTypeSub, self).__init__(id, metaDataProperty, coordinateOperationName, coordinateOperationID, remarks, operationVersion, validArea, scope, _positionalAccuracy, sourceCRS, targetCRS, usesSingleOperation, )
supermod.ConcatenatedOperationType.subclass = ConcatenatedOperationTypeSub
# end class ConcatenatedOperationTypeSub


class ConcatenatedOperationRefTypeSub(supermod.ConcatenatedOperationRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, ConcatenatedOperation=None):
        super(ConcatenatedOperationRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, ConcatenatedOperation, )
supermod.ConcatenatedOperationRefType.subclass = ConcatenatedOperationRefTypeSub
# end class ConcatenatedOperationRefTypeSub


class SingleOperationRefTypeSub(supermod.SingleOperationRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _SingleOperation=None):
        super(SingleOperationRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _SingleOperation, )
supermod.SingleOperationRefType.subclass = SingleOperationRefTypeSub
# end class SingleOperationRefTypeSub


class PassThroughOperationTypeSub(supermod.PassThroughOperationType):
    def __init__(self, id=None, metaDataProperty=None, coordinateOperationName=None, coordinateOperationID=None, remarks=None, operationVersion=None, validArea=None, scope=None, _positionalAccuracy=None, sourceCRS=None, targetCRS=None, modifiedCoordinate=None, usesOperation=None):
        super(PassThroughOperationTypeSub, self).__init__(id, metaDataProperty, coordinateOperationName, coordinateOperationID, remarks, operationVersion, validArea, scope, _positionalAccuracy, sourceCRS, targetCRS, modifiedCoordinate, usesOperation, )
supermod.PassThroughOperationType.subclass = PassThroughOperationTypeSub
# end class PassThroughOperationTypeSub


class PassThroughOperationRefTypeSub(supermod.PassThroughOperationRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, PassThroughOperation=None):
        super(PassThroughOperationRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, PassThroughOperation, )
supermod.PassThroughOperationRefType.subclass = PassThroughOperationRefTypeSub
# end class PassThroughOperationRefTypeSub


class OperationRefTypeSub(supermod.OperationRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Operation=None):
        super(OperationRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Operation, )
supermod.OperationRefType.subclass = OperationRefTypeSub
# end class OperationRefTypeSub


class AbstractGeneralConversionTypeSub(supermod.AbstractGeneralConversionType):
    def __init__(self, id=None, metaDataProperty=None, coordinateOperationName=None, coordinateOperationID=None, remarks=None, validArea=None, scope=None, _positionalAccuracy=None, extensiontype_=None):
        super(AbstractGeneralConversionTypeSub, self).__init__(id, metaDataProperty, coordinateOperationName, coordinateOperationID, remarks, validArea, scope, _positionalAccuracy, extensiontype_, )
supermod.AbstractGeneralConversionType.subclass = AbstractGeneralConversionTypeSub
# end class AbstractGeneralConversionTypeSub


class GeneralConversionRefTypeSub(supermod.GeneralConversionRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _GeneralConversion=None):
        super(GeneralConversionRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _GeneralConversion, )
supermod.GeneralConversionRefType.subclass = GeneralConversionRefTypeSub
# end class GeneralConversionRefTypeSub


class ConversionTypeSub(supermod.ConversionType):
    def __init__(self, id=None, metaDataProperty=None, coordinateOperationName=None, coordinateOperationID=None, remarks=None, validArea=None, scope=None, _positionalAccuracy=None, usesMethod=None, usesValue=None):
        super(ConversionTypeSub, self).__init__(id, metaDataProperty, coordinateOperationName, coordinateOperationID, remarks, validArea, scope, _positionalAccuracy, usesMethod, usesValue, )
supermod.ConversionType.subclass = ConversionTypeSub
# end class ConversionTypeSub


class ConversionRefTypeSub(supermod.ConversionRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Conversion=None):
        super(ConversionRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Conversion, )
supermod.ConversionRefType.subclass = ConversionRefTypeSub
# end class ConversionRefTypeSub


class AbstractGeneralTransformationTypeSub(supermod.AbstractGeneralTransformationType):
    def __init__(self, id=None, metaDataProperty=None, coordinateOperationName=None, coordinateOperationID=None, remarks=None, operationVersion=None, validArea=None, scope=None, _positionalAccuracy=None, sourceCRS=None, targetCRS=None, extensiontype_=None):
        super(AbstractGeneralTransformationTypeSub, self).__init__(id, metaDataProperty, coordinateOperationName, coordinateOperationID, remarks, operationVersion, validArea, scope, _positionalAccuracy, sourceCRS, targetCRS, extensiontype_, )
supermod.AbstractGeneralTransformationType.subclass = AbstractGeneralTransformationTypeSub
# end class AbstractGeneralTransformationTypeSub


class GeneralTransformationRefTypeSub(supermod.GeneralTransformationRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _GeneralTransformation=None):
        super(GeneralTransformationRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _GeneralTransformation, )
supermod.GeneralTransformationRefType.subclass = GeneralTransformationRefTypeSub
# end class GeneralTransformationRefTypeSub


class TransformationTypeSub(supermod.TransformationType):
    def __init__(self, id=None, metaDataProperty=None, coordinateOperationName=None, coordinateOperationID=None, remarks=None, operationVersion=None, validArea=None, scope=None, _positionalAccuracy=None, sourceCRS=None, targetCRS=None, usesMethod=None, usesValue=None):
        super(TransformationTypeSub, self).__init__(id, metaDataProperty, coordinateOperationName, coordinateOperationID, remarks, operationVersion, validArea, scope, _positionalAccuracy, sourceCRS, targetCRS, usesMethod, usesValue, )
supermod.TransformationType.subclass = TransformationTypeSub
# end class TransformationTypeSub


class TransformationRefTypeSub(supermod.TransformationRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Transformation=None):
        super(TransformationRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Transformation, )
supermod.TransformationRefType.subclass = TransformationRefTypeSub
# end class TransformationRefTypeSub


class AbstractGeneralParameterValueTypeSub(supermod.AbstractGeneralParameterValueType):
    def __init__(self, extensiontype_=None):
        super(AbstractGeneralParameterValueTypeSub, self).__init__(extensiontype_, )
supermod.AbstractGeneralParameterValueType.subclass = AbstractGeneralParameterValueTypeSub
# end class AbstractGeneralParameterValueTypeSub


class ParameterValueTypeSub(supermod.ParameterValueType):
    def __init__(self, value=None, dmsAngleValue=None, stringValue=None, integerValue=None, booleanValue=None, valueList=None, integerValueList=None, valueFile=None, valueOfParameter=None):
        super(ParameterValueTypeSub, self).__init__(value, dmsAngleValue, stringValue, integerValue, booleanValue, valueList, integerValueList, valueFile, valueOfParameter, )
supermod.ParameterValueType.subclass = ParameterValueTypeSub
# end class ParameterValueTypeSub


class ParameterValueGroupTypeSub(supermod.ParameterValueGroupType):
    def __init__(self, includesValue=None, valuesOfGroup=None):
        super(ParameterValueGroupTypeSub, self).__init__(includesValue, valuesOfGroup, )
supermod.ParameterValueGroupType.subclass = ParameterValueGroupTypeSub
# end class ParameterValueGroupTypeSub


class OperationMethodBaseTypeSub(supermod.OperationMethodBaseType):
    def __init__(self, id=None, metaDataProperty=None, methodName=None, extensiontype_=None):
        super(OperationMethodBaseTypeSub, self).__init__(id, metaDataProperty, methodName, extensiontype_, )
supermod.OperationMethodBaseType.subclass = OperationMethodBaseTypeSub
# end class OperationMethodBaseTypeSub


class OperationMethodTypeSub(supermod.OperationMethodType):
    def __init__(self, id=None, metaDataProperty=None, methodName=None, methodID=None, remarks=None, methodFormula=None, sourceDimensions=None, targetDimensions=None, usesParameter=None):
        super(OperationMethodTypeSub, self).__init__(id, metaDataProperty, methodName, methodID, remarks, methodFormula, sourceDimensions, targetDimensions, usesParameter, )
supermod.OperationMethodType.subclass = OperationMethodTypeSub
# end class OperationMethodTypeSub


class OperationMethodRefTypeSub(supermod.OperationMethodRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, OperationMethod=None):
        super(OperationMethodRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, OperationMethod, )
supermod.OperationMethodRefType.subclass = OperationMethodRefTypeSub
# end class OperationMethodRefTypeSub


class AbstractGeneralOperationParameterTypeSub(supermod.AbstractGeneralOperationParameterType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, minimumOccurs=None):
        super(AbstractGeneralOperationParameterTypeSub, self).__init__(id, metaDataProperty, description, name, minimumOccurs, )
supermod.AbstractGeneralOperationParameterType.subclass = AbstractGeneralOperationParameterTypeSub
# end class AbstractGeneralOperationParameterTypeSub


class AbstractGeneralOperationParameterRefTypeSub(supermod.AbstractGeneralOperationParameterRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _GeneralOperationParameter=None):
        super(AbstractGeneralOperationParameterRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _GeneralOperationParameter, )
supermod.AbstractGeneralOperationParameterRefType.subclass = AbstractGeneralOperationParameterRefTypeSub
# end class AbstractGeneralOperationParameterRefTypeSub


class OperationParameterBaseTypeSub(supermod.OperationParameterBaseType):
    def __init__(self, id=None, metaDataProperty=None, parameterName=None, minimumOccurs=None, extensiontype_=None):
        super(OperationParameterBaseTypeSub, self).__init__(id, metaDataProperty, parameterName, minimumOccurs, extensiontype_, )
supermod.OperationParameterBaseType.subclass = OperationParameterBaseTypeSub
# end class OperationParameterBaseTypeSub


class OperationParameterTypeSub(supermod.OperationParameterType):
    def __init__(self, id=None, metaDataProperty=None, parameterName=None, minimumOccurs=None, parameterID=None, remarks=None):
        super(OperationParameterTypeSub, self).__init__(id, metaDataProperty, parameterName, minimumOccurs, parameterID, remarks, )
supermod.OperationParameterType.subclass = OperationParameterTypeSub
# end class OperationParameterTypeSub


class OperationParameterRefTypeSub(supermod.OperationParameterRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, OperationParameter=None):
        super(OperationParameterRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, OperationParameter, )
supermod.OperationParameterRefType.subclass = OperationParameterRefTypeSub
# end class OperationParameterRefTypeSub


class OperationParameterGroupBaseTypeSub(supermod.OperationParameterGroupBaseType):
    def __init__(self, id=None, metaDataProperty=None, groupName=None, minimumOccurs=None, extensiontype_=None):
        super(OperationParameterGroupBaseTypeSub, self).__init__(id, metaDataProperty, groupName, minimumOccurs, extensiontype_, )
supermod.OperationParameterGroupBaseType.subclass = OperationParameterGroupBaseTypeSub
# end class OperationParameterGroupBaseTypeSub


class OperationParameterGroupTypeSub(supermod.OperationParameterGroupType):
    def __init__(self, id=None, metaDataProperty=None, groupName=None, minimumOccurs=None, groupID=None, remarks=None, maximumOccurs=None, includesParameter=None):
        super(OperationParameterGroupTypeSub, self).__init__(id, metaDataProperty, groupName, minimumOccurs, groupID, remarks, maximumOccurs, includesParameter, )
supermod.OperationParameterGroupType.subclass = OperationParameterGroupTypeSub
# end class OperationParameterGroupTypeSub


class OperationParameterGroupRefTypeSub(supermod.OperationParameterGroupRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, OperationParameterGroup=None):
        super(OperationParameterGroupRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, OperationParameterGroup, )
supermod.OperationParameterGroupRefType.subclass = OperationParameterGroupRefTypeSub
# end class OperationParameterGroupRefTypeSub


class AbstractPositionalAccuracyTypeSub(supermod.AbstractPositionalAccuracyType):
    def __init__(self, measureDescription=None, extensiontype_=None):
        super(AbstractPositionalAccuracyTypeSub, self).__init__(measureDescription, extensiontype_, )
supermod.AbstractPositionalAccuracyType.subclass = AbstractPositionalAccuracyTypeSub
# end class AbstractPositionalAccuracyTypeSub


class AbsoluteExternalPositionalAccuracyTypeSub(supermod.AbsoluteExternalPositionalAccuracyType):
    def __init__(self, measureDescription=None, result=None):
        super(AbsoluteExternalPositionalAccuracyTypeSub, self).__init__(measureDescription, result, )
supermod.AbsoluteExternalPositionalAccuracyType.subclass = AbsoluteExternalPositionalAccuracyTypeSub
# end class AbsoluteExternalPositionalAccuracyTypeSub


class RelativeInternalPositionalAccuracyTypeSub(supermod.RelativeInternalPositionalAccuracyType):
    def __init__(self, measureDescription=None, result=None):
        super(RelativeInternalPositionalAccuracyTypeSub, self).__init__(measureDescription, result, )
supermod.RelativeInternalPositionalAccuracyType.subclass = RelativeInternalPositionalAccuracyTypeSub
# end class RelativeInternalPositionalAccuracyTypeSub


class CovarianceMatrixTypeSub(supermod.CovarianceMatrixType):
    def __init__(self, measureDescription=None, unitOfMeasure=None, includesElement=None):
        super(CovarianceMatrixTypeSub, self).__init__(measureDescription, unitOfMeasure, includesElement, )
supermod.CovarianceMatrixType.subclass = CovarianceMatrixTypeSub
# end class CovarianceMatrixTypeSub


class CovarianceElementTypeSub(supermod.CovarianceElementType):
    def __init__(self, rowIndex=None, columnIndex=None, covariance=None):
        super(CovarianceElementTypeSub, self).__init__(rowIndex, columnIndex, covariance, )
supermod.CovarianceElementType.subclass = CovarianceElementTypeSub
# end class CovarianceElementTypeSub


class TargetPropertyTypeSub(supermod.TargetPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Feature=None, _Geometry=None):
        super(TargetPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _Feature, _Geometry, )
supermod.TargetPropertyType.subclass = TargetPropertyTypeSub
# end class TargetPropertyTypeSub


class DefaultStylePropertyTypeSub(supermod.DefaultStylePropertyType):
    def __init__(self, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _Style=None):
        super(DefaultStylePropertyTypeSub, self).__init__(about, type_, href, role, arcrole, title, show, actuate, remoteSchema, _Style, )
supermod.DefaultStylePropertyType.subclass = DefaultStylePropertyTypeSub
# end class DefaultStylePropertyTypeSub


class AbstractStyleTypeSub(supermod.AbstractStyleType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, extensiontype_=None):
        super(AbstractStyleTypeSub, self).__init__(id, metaDataProperty, description, name, extensiontype_, )
supermod.AbstractStyleType.subclass = AbstractStyleTypeSub
# end class AbstractStyleTypeSub


class StyleTypeSub(supermod.StyleType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, featureStyle=None, graphStyle=None):
        super(StyleTypeSub, self).__init__(id, metaDataProperty, description, name, featureStyle, graphStyle, )
supermod.StyleType.subclass = StyleTypeSub
# end class StyleTypeSub


class FeatureStylePropertyTypeSub(supermod.FeatureStylePropertyType):
    def __init__(self, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, FeatureStyle=None):
        super(FeatureStylePropertyTypeSub, self).__init__(about, type_, href, role, arcrole, title, show, actuate, remoteSchema, FeatureStyle, )
supermod.FeatureStylePropertyType.subclass = FeatureStylePropertyTypeSub
# end class FeatureStylePropertyTypeSub


class FeatureStyleTypeSub(supermod.FeatureStyleType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, featureType=None, baseType=None, queryGrammar=None, featureConstraint=None, geometryStyle=None, topologyStyle=None, labelStyle=None):
        super(FeatureStyleTypeSub, self).__init__(id, metaDataProperty, description, name, featureType, baseType, queryGrammar, featureConstraint, geometryStyle, topologyStyle, labelStyle, )
supermod.FeatureStyleType.subclass = FeatureStyleTypeSub
# end class FeatureStyleTypeSub


class BaseStyleDescriptorTypeSub(supermod.BaseStyleDescriptorType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, spatialResolution=None, styleVariation=None, animate=None, animateMotion=None, animateColor=None, set=None, extensiontype_=None):
        super(BaseStyleDescriptorTypeSub, self).__init__(id, metaDataProperty, description, name, spatialResolution, styleVariation, animate, animateMotion, animateColor, set, extensiontype_, )
supermod.BaseStyleDescriptorType.subclass = BaseStyleDescriptorTypeSub
# end class BaseStyleDescriptorTypeSub


class GeometryStylePropertyTypeSub(supermod.GeometryStylePropertyType):
    def __init__(self, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, GeometryStyle=None):
        super(GeometryStylePropertyTypeSub, self).__init__(about, type_, href, role, arcrole, title, show, actuate, remoteSchema, GeometryStyle, )
supermod.GeometryStylePropertyType.subclass = GeometryStylePropertyTypeSub
# end class GeometryStylePropertyTypeSub


class GeometryStyleTypeSub(supermod.GeometryStyleType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, spatialResolution=None, styleVariation=None, animate=None, animateMotion=None, animateColor=None, set=None, geometryProperty=None, geometryType=None, symbol=None, style=None, labelStyle=None):
        super(GeometryStyleTypeSub, self).__init__(id, metaDataProperty, description, name, spatialResolution, styleVariation, animate, animateMotion, animateColor, set, geometryProperty, geometryType, symbol, style, labelStyle, )
supermod.GeometryStyleType.subclass = GeometryStyleTypeSub
# end class GeometryStyleTypeSub


class TopologyStylePropertyTypeSub(supermod.TopologyStylePropertyType):
    def __init__(self, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TopologyStyle=None):
        super(TopologyStylePropertyTypeSub, self).__init__(about, type_, href, role, arcrole, title, show, actuate, remoteSchema, TopologyStyle, )
supermod.TopologyStylePropertyType.subclass = TopologyStylePropertyTypeSub
# end class TopologyStylePropertyTypeSub


class TopologyStyleTypeSub(supermod.TopologyStyleType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, spatialResolution=None, styleVariation=None, animate=None, animateMotion=None, animateColor=None, set=None, topologyProperty=None, topologyType=None, symbol=None, style=None, labelStyle=None):
        super(TopologyStyleTypeSub, self).__init__(id, metaDataProperty, description, name, spatialResolution, styleVariation, animate, animateMotion, animateColor, set, topologyProperty, topologyType, symbol, style, labelStyle, )
supermod.TopologyStyleType.subclass = TopologyStyleTypeSub
# end class TopologyStyleTypeSub


class LabelStylePropertyTypeSub(supermod.LabelStylePropertyType):
    def __init__(self, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, LabelStyle=None):
        super(LabelStylePropertyTypeSub, self).__init__(about, type_, href, role, arcrole, title, show, actuate, remoteSchema, LabelStyle, )
supermod.LabelStylePropertyType.subclass = LabelStylePropertyTypeSub
# end class LabelStylePropertyTypeSub


class LabelStyleTypeSub(supermod.LabelStyleType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, spatialResolution=None, styleVariation=None, animate=None, animateMotion=None, animateColor=None, set=None, style=None, label=None):
        super(LabelStyleTypeSub, self).__init__(id, metaDataProperty, description, name, spatialResolution, styleVariation, animate, animateMotion, animateColor, set, style, label, )
supermod.LabelStyleType.subclass = LabelStyleTypeSub
# end class LabelStyleTypeSub


class GraphStylePropertyTypeSub(supermod.GraphStylePropertyType):
    def __init__(self, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, GraphStyle=None):
        super(GraphStylePropertyTypeSub, self).__init__(about, type_, href, role, arcrole, title, show, actuate, remoteSchema, GraphStyle, )
supermod.GraphStylePropertyType.subclass = GraphStylePropertyTypeSub
# end class GraphStylePropertyTypeSub


class GraphStyleTypeSub(supermod.GraphStyleType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, spatialResolution=None, styleVariation=None, animate=None, animateMotion=None, animateColor=None, set=None, planar=None, directed=None, grid=None, minDistance=None, minAngle=None, graphType=None, drawingType=None, lineType=None, aestheticCriteria=None):
        super(GraphStyleTypeSub, self).__init__(id, metaDataProperty, description, name, spatialResolution, styleVariation, animate, animateMotion, animateColor, set, planar, directed, grid, minDistance, minAngle, graphType, drawingType, lineType, aestheticCriteria, )
supermod.GraphStyleType.subclass = GraphStyleTypeSub
# end class GraphStyleTypeSub


class SymbolTypeSub(supermod.SymbolType):
    def __init__(self, symbolType=None, transform=None, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, anytypeobjs_=None):
        super(SymbolTypeSub, self).__init__(symbolType, transform, about, type_, href, role, arcrole, title, show, actuate, remoteSchema, anytypeobjs_, )
supermod.SymbolType.subclass = SymbolTypeSub
# end class SymbolTypeSub


class LabelTypeSub(supermod.LabelType):
    def __init__(self, transform=None, LabelExpression=None, valueOf_=None, mixedclass_=None, content_=None):
        super(LabelTypeSub, self).__init__(transform, LabelExpression, valueOf_, mixedclass_, content_, )
supermod.LabelType.subclass = LabelTypeSub
# end class LabelTypeSub


class StyleVariationTypeSub(supermod.StyleVariationType):
    def __init__(self, styleProperty=None, featurePropertyRange=None, valueOf_=None):
        super(StyleVariationTypeSub, self).__init__(styleProperty, featurePropertyRange, valueOf_, )
supermod.StyleVariationType.subclass = StyleVariationTypeSub
# end class StyleVariationTypeSub


class animatePrototypeSub(supermod.animatePrototype):
    def __init__(self, attributeName=None, attributeType='auto', additive='replace', accumulate='none', to=None, from_=None, by=None, values=None, extensiontype_=None):
        super(animatePrototypeSub, self).__init__(attributeName, attributeType, additive, accumulate, to, from_, by, values, extensiontype_, )
supermod.animatePrototype.subclass = animatePrototypeSub
# end class animatePrototypeSub


class animateMotionPrototypeSub(supermod.animateMotionPrototype):
    def __init__(self, origin=None, additive='replace', accumulate='none', to=None, from_=None, by=None, values=None, extensiontype_=None):
        super(animateMotionPrototypeSub, self).__init__(origin, additive, accumulate, to, from_, by, values, extensiontype_, )
supermod.animateMotionPrototype.subclass = animateMotionPrototypeSub
# end class animateMotionPrototypeSub


class animateColorPrototypeSub(supermod.animateColorPrototype):
    def __init__(self, attributeName=None, attributeType='auto', additive='replace', accumulate='none', to=None, from_=None, by=None, values=None, extensiontype_=None):
        super(animateColorPrototypeSub, self).__init__(attributeName, attributeType, additive, accumulate, to, from_, by, values, extensiontype_, )
supermod.animateColorPrototype.subclass = animateColorPrototypeSub
# end class animateColorPrototypeSub


class setPrototypeSub(supermod.setPrototype):
    def __init__(self, attributeName=None, attributeType='auto', to=None, extensiontype_=None):
        super(setPrototypeSub, self).__init__(attributeName, attributeType, to, extensiontype_, )
supermod.setPrototype.subclass = setPrototypeSub
# end class setPrototypeSub


class animateTypeSub(supermod.animateType):
    def __init__(self, attributeName=None, attributeType='auto', additive='replace', accumulate='none', to=None, from_=None, by=None, values=None, id=None, class_=None, lang=None, alt=None, longdesc=None, begin=None, end=None, dur=None, repeatDur=None, repeatCount=None, repeat=None, min=None, max=None, syncBehavior='default', syncTolerance=None, syncBehaviorDefault='inherit', syncToleranceDefault='inherit', restart='default', restartDefault='inherit', fill='default', fillDefault='inherit', targetElement=None, calcMode='linear', skip_content='true', anytypeobjs_=None):
        super(animateTypeSub, self).__init__(attributeName, attributeType, additive, accumulate, to, from_, by, values, id, class_, lang, alt, longdesc, begin, end, dur, repeatDur, repeatCount, repeat, min, max, syncBehavior, syncTolerance, syncBehaviorDefault, syncToleranceDefault, restart, restartDefault, fill, fillDefault, targetElement, calcMode, skip_content, anytypeobjs_, )
supermod.animateType.subclass = animateTypeSub
# end class animateTypeSub


class animateMotionTypeSub(supermod.animateMotionType):
    def __init__(self, origin=None, additive='replace', accumulate='none', to=None, from_=None, by=None, values=None, id=None, class_=None, lang=None, alt=None, longdesc=None, begin=None, end=None, dur=None, repeatDur=None, repeatCount=None, repeat=None, min=None, max=None, syncBehavior='default', syncTolerance=None, syncBehaviorDefault='inherit', syncToleranceDefault='inherit', restart='default', restartDefault='inherit', fill='default', fillDefault='inherit', targetElement=None, calcMode='linear', skip_content='true', anytypeobjs_=None):
        super(animateMotionTypeSub, self).__init__(origin, additive, accumulate, to, from_, by, values, id, class_, lang, alt, longdesc, begin, end, dur, repeatDur, repeatCount, repeat, min, max, syncBehavior, syncTolerance, syncBehaviorDefault, syncToleranceDefault, restart, restartDefault, fill, fillDefault, targetElement, calcMode, skip_content, anytypeobjs_, )
supermod.animateMotionType.subclass = animateMotionTypeSub
# end class animateMotionTypeSub


class animateColorTypeSub(supermod.animateColorType):
    def __init__(self, attributeName=None, attributeType='auto', additive='replace', accumulate='none', to=None, from_=None, by=None, values=None, id=None, class_=None, lang=None, alt=None, longdesc=None, begin=None, end=None, dur=None, repeatDur=None, repeatCount=None, repeat=None, min=None, max=None, syncBehavior='default', syncTolerance=None, syncBehaviorDefault='inherit', syncToleranceDefault='inherit', restart='default', restartDefault='inherit', fill='default', fillDefault='inherit', targetElement=None, calcMode='linear', skip_content='true', anytypeobjs_=None):
        super(animateColorTypeSub, self).__init__(attributeName, attributeType, additive, accumulate, to, from_, by, values, id, class_, lang, alt, longdesc, begin, end, dur, repeatDur, repeatCount, repeat, min, max, syncBehavior, syncTolerance, syncBehaviorDefault, syncToleranceDefault, restart, restartDefault, fill, fillDefault, targetElement, calcMode, skip_content, anytypeobjs_, )
supermod.animateColorType.subclass = animateColorTypeSub
# end class animateColorTypeSub


class setTypeSub(supermod.setType):
    def __init__(self, attributeName=None, attributeType='auto', to=None, id=None, class_=None, lang=None, alt=None, longdesc=None, begin=None, end=None, dur=None, repeatDur=None, repeatCount=None, repeat=None, min=None, max=None, syncBehavior='default', syncTolerance=None, syncBehaviorDefault='inherit', syncToleranceDefault='inherit', restart='default', restartDefault='inherit', fill='default', fillDefault='inherit', targetElement=None, skip_content='true', anytypeobjs_=None):
        super(setTypeSub, self).__init__(attributeName, attributeType, to, id, class_, lang, alt, longdesc, begin, end, dur, repeatDur, repeatCount, repeat, min, max, syncBehavior, syncTolerance, syncBehaviorDefault, syncToleranceDefault, restart, restartDefault, fill, fillDefault, targetElement, skip_content, anytypeobjs_, )
supermod.setType.subclass = setTypeSub
# end class setTypeSub


class AbstractTimeReferenceSystemTypeSub(supermod.AbstractTimeReferenceSystemType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, domainOfValidity=None, extensiontype_=None):
        super(AbstractTimeReferenceSystemTypeSub, self).__init__(id, metaDataProperty, description, name, domainOfValidity, extensiontype_, )
supermod.AbstractTimeReferenceSystemType.subclass = AbstractTimeReferenceSystemTypeSub
# end class AbstractTimeReferenceSystemTypeSub


class TimeCoordinateSystemTypeSub(supermod.TimeCoordinateSystemType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, domainOfValidity=None, originPosition=None, origin=None, interval=None):
        super(TimeCoordinateSystemTypeSub, self).__init__(id, metaDataProperty, description, name, domainOfValidity, originPosition, origin, interval, )
supermod.TimeCoordinateSystemType.subclass = TimeCoordinateSystemTypeSub
# end class TimeCoordinateSystemTypeSub


class TimeOrdinalReferenceSystemTypeSub(supermod.TimeOrdinalReferenceSystemType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, domainOfValidity=None, component=None):
        super(TimeOrdinalReferenceSystemTypeSub, self).__init__(id, metaDataProperty, description, name, domainOfValidity, component, )
supermod.TimeOrdinalReferenceSystemType.subclass = TimeOrdinalReferenceSystemTypeSub
# end class TimeOrdinalReferenceSystemTypeSub


class TimeOrdinalEraTypeSub(supermod.TimeOrdinalEraType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, relatedTime=None, start=None, end=None, extent=None, member=None, group=None):
        super(TimeOrdinalEraTypeSub, self).__init__(id, metaDataProperty, description, name, relatedTime, start, end, extent, member, group, )
supermod.TimeOrdinalEraType.subclass = TimeOrdinalEraTypeSub
# end class TimeOrdinalEraTypeSub


class TimeOrdinalEraPropertyTypeSub(supermod.TimeOrdinalEraPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimeOrdinalEra=None):
        super(TimeOrdinalEraPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimeOrdinalEra, )
supermod.TimeOrdinalEraPropertyType.subclass = TimeOrdinalEraPropertyTypeSub
# end class TimeOrdinalEraPropertyTypeSub


class TimeCalendarTypeSub(supermod.TimeCalendarType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, domainOfValidity=None, referenceFrame=None):
        super(TimeCalendarTypeSub, self).__init__(id, metaDataProperty, description, name, domainOfValidity, referenceFrame, )
supermod.TimeCalendarType.subclass = TimeCalendarTypeSub
# end class TimeCalendarTypeSub


class TimeCalendarPropertyTypeSub(supermod.TimeCalendarPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimeCalendar=None):
        super(TimeCalendarPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimeCalendar, )
supermod.TimeCalendarPropertyType.subclass = TimeCalendarPropertyTypeSub
# end class TimeCalendarPropertyTypeSub


class TimeCalendarEraTypeSub(supermod.TimeCalendarEraType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, referenceEvent=None, referenceDate='0001-01-01', julianReference=None, epochOfUse=None):
        super(TimeCalendarEraTypeSub, self).__init__(id, metaDataProperty, description, name, referenceEvent, referenceDate, julianReference, epochOfUse, )
supermod.TimeCalendarEraType.subclass = TimeCalendarEraTypeSub
# end class TimeCalendarEraTypeSub


class TimeCalendarEraPropertyTypeSub(supermod.TimeCalendarEraPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimeCalendarEra=None):
        super(TimeCalendarEraPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimeCalendarEra, )
supermod.TimeCalendarEraPropertyType.subclass = TimeCalendarEraPropertyTypeSub
# end class TimeCalendarEraPropertyTypeSub


class TimeClockTypeSub(supermod.TimeClockType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, domainOfValidity=None, referenceEvent=None, referenceTime=None, utcReference=None, dateBasis=None):
        super(TimeClockTypeSub, self).__init__(id, metaDataProperty, description, name, domainOfValidity, referenceEvent, referenceTime, utcReference, dateBasis, )
supermod.TimeClockType.subclass = TimeClockTypeSub
# end class TimeClockTypeSub


class TimeClockPropertyTypeSub(supermod.TimeClockPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimeClock=None):
        super(TimeClockPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimeClock, )
supermod.TimeClockPropertyType.subclass = TimeClockPropertyTypeSub
# end class TimeClockPropertyTypeSub


class TimeTopologyComplexTypeSub(supermod.TimeTopologyComplexType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, primitive=None):
        super(TimeTopologyComplexTypeSub, self).__init__(id, metaDataProperty, description, name, primitive, )
supermod.TimeTopologyComplexType.subclass = TimeTopologyComplexTypeSub
# end class TimeTopologyComplexTypeSub


class TimeTopologyComplexPropertyTypeSub(supermod.TimeTopologyComplexPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimeTopologyComplex=None):
        super(TimeTopologyComplexPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimeTopologyComplex, )
supermod.TimeTopologyComplexPropertyType.subclass = TimeTopologyComplexPropertyTypeSub
# end class TimeTopologyComplexPropertyTypeSub


class AbstractTimeTopologyPrimitiveTypeSub(supermod.AbstractTimeTopologyPrimitiveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, relatedTime=None, complex=None, extensiontype_=None):
        super(AbstractTimeTopologyPrimitiveTypeSub, self).__init__(id, metaDataProperty, description, name, relatedTime, complex, extensiontype_, )
supermod.AbstractTimeTopologyPrimitiveType.subclass = AbstractTimeTopologyPrimitiveTypeSub
# end class AbstractTimeTopologyPrimitiveTypeSub


class TimeTopologyPrimitivePropertyTypeSub(supermod.TimeTopologyPrimitivePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, _TimeTopologyPrimitive=None):
        super(TimeTopologyPrimitivePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, _TimeTopologyPrimitive, )
supermod.TimeTopologyPrimitivePropertyType.subclass = TimeTopologyPrimitivePropertyTypeSub
# end class TimeTopologyPrimitivePropertyTypeSub


class TimeNodeTypeSub(supermod.TimeNodeType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, relatedTime=None, complex=None, previousEdge=None, nextEdge=None, position=None):
        super(TimeNodeTypeSub, self).__init__(id, metaDataProperty, description, name, relatedTime, complex, previousEdge, nextEdge, position, )
supermod.TimeNodeType.subclass = TimeNodeTypeSub
# end class TimeNodeTypeSub


class TimeNodePropertyTypeSub(supermod.TimeNodePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimeNode=None):
        super(TimeNodePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimeNode, )
supermod.TimeNodePropertyType.subclass = TimeNodePropertyTypeSub
# end class TimeNodePropertyTypeSub


class TimeEdgeTypeSub(supermod.TimeEdgeType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, relatedTime=None, complex=None, start=None, end=None, extent=None):
        super(TimeEdgeTypeSub, self).__init__(id, metaDataProperty, description, name, relatedTime, complex, start, end, extent, )
supermod.TimeEdgeType.subclass = TimeEdgeTypeSub
# end class TimeEdgeTypeSub


class TimeEdgePropertyTypeSub(supermod.TimeEdgePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, TimeEdge=None):
        super(TimeEdgePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, TimeEdge, )
supermod.TimeEdgePropertyType.subclass = TimeEdgePropertyTypeSub
# end class TimeEdgePropertyTypeSub


class FilterTypeSub(supermod.FilterType):
    def __init__(self, spatialOps=None, comparisonOps=None, logicOps=None, _Id=None):
        super(FilterTypeSub, self).__init__(spatialOps, comparisonOps, logicOps, _Id, )
supermod.FilterType.subclass = FilterTypeSub
# end class FilterTypeSub


class ComparisonOpsTypeSub(supermod.ComparisonOpsType):
    def __init__(self, extensiontype_=None):
        super(ComparisonOpsTypeSub, self).__init__(extensiontype_, )
supermod.ComparisonOpsType.subclass = ComparisonOpsTypeSub
# end class ComparisonOpsTypeSub


class SpatialOpsTypeSub(supermod.SpatialOpsType):
    def __init__(self, extensiontype_=None):
        super(SpatialOpsTypeSub, self).__init__(extensiontype_, )
supermod.SpatialOpsType.subclass = SpatialOpsTypeSub
# end class SpatialOpsTypeSub


class LogicOpsTypeSub(supermod.LogicOpsType):
    def __init__(self, extensiontype_=None):
        super(LogicOpsTypeSub, self).__init__(extensiontype_, )
supermod.LogicOpsType.subclass = LogicOpsTypeSub
# end class LogicOpsTypeSub


class AbstractIdTypeSub(supermod.AbstractIdType):
    def __init__(self, extensiontype_=None):
        super(AbstractIdTypeSub, self).__init__(extensiontype_, )
supermod.AbstractIdType.subclass = AbstractIdTypeSub
# end class AbstractIdTypeSub


class FeatureIdTypeSub(supermod.FeatureIdType):
    def __init__(self, fid=None):
        super(FeatureIdTypeSub, self).__init__(fid, )
supermod.FeatureIdType.subclass = FeatureIdTypeSub
# end class FeatureIdTypeSub


class GmlObjectIdTypeSub(supermod.GmlObjectIdType):
    def __init__(self, id=None):
        super(GmlObjectIdTypeSub, self).__init__(id, )
supermod.GmlObjectIdType.subclass = GmlObjectIdTypeSub
# end class GmlObjectIdTypeSub


class BinaryComparisonOpTypeSub(supermod.BinaryComparisonOpType):
    def __init__(self, matchCase=True, expression=None):
        super(BinaryComparisonOpTypeSub, self).__init__(matchCase, expression, )
supermod.BinaryComparisonOpType.subclass = BinaryComparisonOpTypeSub
# end class BinaryComparisonOpTypeSub


class PropertyIsLikeTypeSub(supermod.PropertyIsLikeType):
    def __init__(self, wildCard=None, singleChar=None, escapeChar=None, matchCase=True, PropertyName=None, Literal=None):
        super(PropertyIsLikeTypeSub, self).__init__(wildCard, singleChar, escapeChar, matchCase, PropertyName, Literal, )
supermod.PropertyIsLikeType.subclass = PropertyIsLikeTypeSub
# end class PropertyIsLikeTypeSub


class PropertyIsNullTypeSub(supermod.PropertyIsNullType):
    def __init__(self, PropertyName=None):
        super(PropertyIsNullTypeSub, self).__init__(PropertyName, )
supermod.PropertyIsNullType.subclass = PropertyIsNullTypeSub
# end class PropertyIsNullTypeSub


class PropertyIsBetweenTypeSub(supermod.PropertyIsBetweenType):
    def __init__(self, expression=None, LowerBoundary=None, UpperBoundary=None):
        super(PropertyIsBetweenTypeSub, self).__init__(expression, LowerBoundary, UpperBoundary, )
supermod.PropertyIsBetweenType.subclass = PropertyIsBetweenTypeSub
# end class PropertyIsBetweenTypeSub


class LowerBoundaryTypeSub(supermod.LowerBoundaryType):
    def __init__(self, expression=None):
        super(LowerBoundaryTypeSub, self).__init__(expression, )
supermod.LowerBoundaryType.subclass = LowerBoundaryTypeSub
# end class LowerBoundaryTypeSub


class UpperBoundaryTypeSub(supermod.UpperBoundaryType):
    def __init__(self, expression=None):
        super(UpperBoundaryTypeSub, self).__init__(expression, )
supermod.UpperBoundaryType.subclass = UpperBoundaryTypeSub
# end class UpperBoundaryTypeSub


class BinarySpatialOpTypeSub(supermod.BinarySpatialOpType):
    def __init__(self, PropertyName=None, _Geometry=None, Envelope=None):
        super(BinarySpatialOpTypeSub, self).__init__(PropertyName, _Geometry, Envelope, )
supermod.BinarySpatialOpType.subclass = BinarySpatialOpTypeSub
# end class BinarySpatialOpTypeSub


class BBOXTypeSub(supermod.BBOXType):
    def __init__(self, PropertyName=None, Envelope=None):
        super(BBOXTypeSub, self).__init__(PropertyName, Envelope, )
supermod.BBOXType.subclass = BBOXTypeSub
# end class BBOXTypeSub


class DistanceBufferTypeSub(supermod.DistanceBufferType):
    def __init__(self, PropertyName=None, _Geometry=None, Distance=None):
        super(DistanceBufferTypeSub, self).__init__(PropertyName, _Geometry, Distance, )
supermod.DistanceBufferType.subclass = DistanceBufferTypeSub
# end class DistanceBufferTypeSub


class DistanceTypeSub(supermod.DistanceType):
    def __init__(self, units=None, valueOf_=None):
        super(DistanceTypeSub, self).__init__(units, valueOf_, )
supermod.DistanceType.subclass = DistanceTypeSub
# end class DistanceTypeSub


class BinaryLogicOpTypeSub(supermod.BinaryLogicOpType):
    def __init__(self, comparisonOps=None, spatialOps=None, logicOps=None, Function=None):
        super(BinaryLogicOpTypeSub, self).__init__(comparisonOps, spatialOps, logicOps, Function, )
supermod.BinaryLogicOpType.subclass = BinaryLogicOpTypeSub
# end class BinaryLogicOpTypeSub


class UnaryLogicOpTypeSub(supermod.UnaryLogicOpType):
    def __init__(self, comparisonOps=None, spatialOps=None, logicOps=None, Function=None):
        super(UnaryLogicOpTypeSub, self).__init__(comparisonOps, spatialOps, logicOps, Function, )
supermod.UnaryLogicOpType.subclass = UnaryLogicOpTypeSub
# end class UnaryLogicOpTypeSub


class ExpressionTypeSub(supermod.ExpressionType):
    def __init__(self, extensiontype_=None):
        super(ExpressionTypeSub, self).__init__(extensiontype_, )
supermod.ExpressionType.subclass = ExpressionTypeSub
# end class ExpressionTypeSub


class BinaryOperatorTypeSub(supermod.BinaryOperatorType):
    def __init__(self, expression=None):
        super(BinaryOperatorTypeSub, self).__init__(expression, )
supermod.BinaryOperatorType.subclass = BinaryOperatorTypeSub
# end class BinaryOperatorTypeSub


class FunctionTypeSub(supermod.FunctionType):
    def __init__(self, name=None, expression=None):
        super(FunctionTypeSub, self).__init__(name, expression, )
supermod.FunctionType.subclass = FunctionTypeSub
# end class FunctionTypeSub


class LiteralTypeSub(supermod.LiteralType):
    def __init__(self, anytypeobjs_=None):
        super(LiteralTypeSub, self).__init__(anytypeobjs_, )
supermod.LiteralType.subclass = LiteralTypeSub
# end class LiteralTypeSub


class PropertyNameTypeSub(supermod.PropertyNameType):
    def __init__(self):
        super(PropertyNameTypeSub, self).__init__()
supermod.PropertyNameType.subclass = PropertyNameTypeSub
# end class PropertyNameTypeSub


class SortByTypeSub(supermod.SortByType):
    def __init__(self, SortProperty=None):
        super(SortByTypeSub, self).__init__(SortProperty, )
supermod.SortByType.subclass = SortByTypeSub
# end class SortByTypeSub


class SortPropertyTypeSub(supermod.SortPropertyType):
    def __init__(self, PropertyName=None, SortOrder=None):
        super(SortPropertyTypeSub, self).__init__(PropertyName, SortOrder, )
supermod.SortPropertyType.subclass = SortPropertyTypeSub
# end class SortPropertyTypeSub


class Filter_CapabilitiesSub(supermod.Filter_Capabilities):
    def __init__(self, Spatial_Capabilities=None, Scalar_Capabilities=None, Id_Capabilities=None):
        super(Filter_CapabilitiesSub, self).__init__(Spatial_Capabilities, Scalar_Capabilities, Id_Capabilities, )
supermod.Filter_Capabilities.subclass = Filter_CapabilitiesSub
# end class Filter_CapabilitiesSub


class Spatial_CapabilitiesTypeSub(supermod.Spatial_CapabilitiesType):
    def __init__(self, GeometryOperands=None, SpatialOperators=None):
        super(Spatial_CapabilitiesTypeSub, self).__init__(GeometryOperands, SpatialOperators, )
supermod.Spatial_CapabilitiesType.subclass = Spatial_CapabilitiesTypeSub
# end class Spatial_CapabilitiesTypeSub


class GeometryOperandsTypeSub(supermod.GeometryOperandsType):
    def __init__(self, GeometryOperand=None):
        super(GeometryOperandsTypeSub, self).__init__(GeometryOperand, )
supermod.GeometryOperandsType.subclass = GeometryOperandsTypeSub
# end class GeometryOperandsTypeSub


class SpatialOperatorsTypeSub(supermod.SpatialOperatorsType):
    def __init__(self, SpatialOperator=None):
        super(SpatialOperatorsTypeSub, self).__init__(SpatialOperator, )
supermod.SpatialOperatorsType.subclass = SpatialOperatorsTypeSub
# end class SpatialOperatorsTypeSub


class SpatialOperatorTypeSub(supermod.SpatialOperatorType):
    def __init__(self, name=None, GeometryOperands=None):
        super(SpatialOperatorTypeSub, self).__init__(name, GeometryOperands, )
supermod.SpatialOperatorType.subclass = SpatialOperatorTypeSub
# end class SpatialOperatorTypeSub


class Scalar_CapabilitiesTypeSub(supermod.Scalar_CapabilitiesType):
    def __init__(self, LogicalOperators=None, ComparisonOperators=None, ArithmeticOperators=None):
        super(Scalar_CapabilitiesTypeSub, self).__init__(LogicalOperators, ComparisonOperators, ArithmeticOperators, )
supermod.Scalar_CapabilitiesType.subclass = Scalar_CapabilitiesTypeSub
# end class Scalar_CapabilitiesTypeSub


class LogicalOperatorsSub(supermod.LogicalOperators):
    def __init__(self):
        super(LogicalOperatorsSub, self).__init__()
supermod.LogicalOperators.subclass = LogicalOperatorsSub
# end class LogicalOperatorsSub


class ComparisonOperatorsTypeSub(supermod.ComparisonOperatorsType):
    def __init__(self, ComparisonOperator=None):
        super(ComparisonOperatorsTypeSub, self).__init__(ComparisonOperator, )
supermod.ComparisonOperatorsType.subclass = ComparisonOperatorsTypeSub
# end class ComparisonOperatorsTypeSub


class ArithmeticOperatorsTypeSub(supermod.ArithmeticOperatorsType):
    def __init__(self, SimpleArithmetic=None, Functions=None):
        super(ArithmeticOperatorsTypeSub, self).__init__(SimpleArithmetic, Functions, )
supermod.ArithmeticOperatorsType.subclass = ArithmeticOperatorsTypeSub
# end class ArithmeticOperatorsTypeSub


class SimpleArithmeticSub(supermod.SimpleArithmetic):
    def __init__(self):
        super(SimpleArithmeticSub, self).__init__()
supermod.SimpleArithmetic.subclass = SimpleArithmeticSub
# end class SimpleArithmeticSub


class FunctionsTypeSub(supermod.FunctionsType):
    def __init__(self, FunctionNames=None):
        super(FunctionsTypeSub, self).__init__(FunctionNames, )
supermod.FunctionsType.subclass = FunctionsTypeSub
# end class FunctionsTypeSub


class FunctionNamesTypeSub(supermod.FunctionNamesType):
    def __init__(self, FunctionName=None):
        super(FunctionNamesTypeSub, self).__init__(FunctionName, )
supermod.FunctionNamesType.subclass = FunctionNamesTypeSub
# end class FunctionNamesTypeSub


class FunctionNameTypeSub(supermod.FunctionNameType):
    def __init__(self, nArgs=None, valueOf_=None):
        super(FunctionNameTypeSub, self).__init__(nArgs, valueOf_, )
supermod.FunctionNameType.subclass = FunctionNameTypeSub
# end class FunctionNameTypeSub


class Id_CapabilitiesTypeSub(supermod.Id_CapabilitiesType):
    def __init__(self, EID=None, FID=None):
        super(Id_CapabilitiesTypeSub, self).__init__(EID, FID, )
supermod.Id_CapabilitiesType.subclass = Id_CapabilitiesTypeSub
# end class Id_CapabilitiesTypeSub


class EIDSub(supermod.EID):
    def __init__(self):
        super(EIDSub, self).__init__()
supermod.EID.subclass = EIDSub
# end class EIDSub


class FIDSub(supermod.FID):
    def __init__(self):
        super(FIDSub, self).__init__()
supermod.FID.subclass = FIDSub
# end class FIDSub


class FeatureTypeStyleTypeSub(supermod.FeatureTypeStyleType):
    def __init__(self, version=None, Name=None, Description=None, FeatureTypeName=None, SemanticTypeIdentifier=None, Rule=None, OnlineResource=None):
        super(FeatureTypeStyleTypeSub, self).__init__(version, Name, Description, FeatureTypeName, SemanticTypeIdentifier, Rule, OnlineResource, )
supermod.FeatureTypeStyleType.subclass = FeatureTypeStyleTypeSub
# end class FeatureTypeStyleTypeSub


class CoverageStyleTypeSub(supermod.CoverageStyleType):
    def __init__(self, version=None, Name=None, Description=None, CoverageName=None, SemanticTypeIdentifier=None, Rule=None, OnlineResource=None):
        super(CoverageStyleTypeSub, self).__init__(version, Name, Description, CoverageName, SemanticTypeIdentifier, Rule, OnlineResource, )
supermod.CoverageStyleType.subclass = CoverageStyleTypeSub
# end class CoverageStyleTypeSub


class RuleTypeSub(supermod.RuleType):
    def __init__(self, Name=None, Description=None, LegendGraphic=None, Filter=None, ElseFilter=None, MinScaleDenominator=None, MaxScaleDenominator=None, Symbolizer=None):
        super(RuleTypeSub, self).__init__(Name, Description, LegendGraphic, Filter, ElseFilter, MinScaleDenominator, MaxScaleDenominator, Symbolizer, )
supermod.RuleType.subclass = RuleTypeSub
# end class RuleTypeSub


class LegendGraphicTypeSub(supermod.LegendGraphicType):
    def __init__(self, Graphic=None):
        super(LegendGraphicTypeSub, self).__init__(Graphic, )
supermod.LegendGraphicType.subclass = LegendGraphicTypeSub
# end class LegendGraphicTypeSub


class ElseFilterTypeSub(supermod.ElseFilterType):
    def __init__(self):
        super(ElseFilterTypeSub, self).__init__()
supermod.ElseFilterType.subclass = ElseFilterTypeSub
# end class ElseFilterTypeSub


class SymbolizerTypeSub(supermod.SymbolizerType):
    def __init__(self, version=None, uom=None, Name=None, Description=None, BaseSymbolizer=None, extensiontype_=None):
        super(SymbolizerTypeSub, self).__init__(version, uom, Name, Description, BaseSymbolizer, extensiontype_, )
supermod.SymbolizerType.subclass = SymbolizerTypeSub
# end class SymbolizerTypeSub


class BaseSymbolizerTypeSub(supermod.BaseSymbolizerType):
    def __init__(self, OnlineResource=None):
        super(BaseSymbolizerTypeSub, self).__init__(OnlineResource, )
supermod.BaseSymbolizerType.subclass = BaseSymbolizerTypeSub
# end class BaseSymbolizerTypeSub


class LineSymbolizerTypeSub(supermod.LineSymbolizerType):
    def __init__(self, version=None, uom=None, Name=None, Description=None, BaseSymbolizer=None, Geometry=None, Stroke=None, PerpendicularOffset=None):
        super(LineSymbolizerTypeSub, self).__init__(version, uom, Name, Description, BaseSymbolizer, Geometry, Stroke, PerpendicularOffset, )
supermod.LineSymbolizerType.subclass = LineSymbolizerTypeSub
# end class LineSymbolizerTypeSub


class GeometryTypeSub(supermod.GeometryType):
    def __init__(self, PropertyName=None):
        super(GeometryTypeSub, self).__init__(PropertyName, )
supermod.GeometryType.subclass = GeometryTypeSub
# end class GeometryTypeSub


class StrokeTypeSub(supermod.StrokeType):
    def __init__(self, GraphicFill=None, GraphicStroke=None, SvgParameter=None):
        super(StrokeTypeSub, self).__init__(GraphicFill, GraphicStroke, SvgParameter, )
supermod.StrokeType.subclass = StrokeTypeSub
# end class StrokeTypeSub


class SvgParameterTypeSub(supermod.SvgParameterType):
    def __init__(self, expression=None, name=None, valueOf_=None, mixedclass_=None, content_=None):
        super(SvgParameterTypeSub, self).__init__(expression, name, valueOf_, mixedclass_, content_, )
supermod.SvgParameterType.subclass = SvgParameterTypeSub
# end class SvgParameterTypeSub


class GraphicFillTypeSub(supermod.GraphicFillType):
    def __init__(self, Graphic=None):
        super(GraphicFillTypeSub, self).__init__(Graphic, )
supermod.GraphicFillType.subclass = GraphicFillTypeSub
# end class GraphicFillTypeSub


class GraphicStrokeTypeSub(supermod.GraphicStrokeType):
    def __init__(self, Graphic=None, InitialGap=None, Gap=None):
        super(GraphicStrokeTypeSub, self).__init__(Graphic, InitialGap, Gap, )
supermod.GraphicStrokeType.subclass = GraphicStrokeTypeSub
# end class GraphicStrokeTypeSub


class PolygonSymbolizerTypeSub(supermod.PolygonSymbolizerType):
    def __init__(self, version=None, uom=None, Name=None, Description=None, BaseSymbolizer=None, Geometry=None, Fill=None, Stroke=None, Displacement=None, PerpendicularOffset=None):
        super(PolygonSymbolizerTypeSub, self).__init__(version, uom, Name, Description, BaseSymbolizer, Geometry, Fill, Stroke, Displacement, PerpendicularOffset, )
supermod.PolygonSymbolizerType.subclass = PolygonSymbolizerTypeSub
# end class PolygonSymbolizerTypeSub


class FillTypeSub(supermod.FillType):
    def __init__(self, GraphicFill=None, SvgParameter=None):
        super(FillTypeSub, self).__init__(GraphicFill, SvgParameter, )
supermod.FillType.subclass = FillTypeSub
# end class FillTypeSub


class PointSymbolizerTypeSub(supermod.PointSymbolizerType):
    def __init__(self, version=None, uom=None, Name=None, Description=None, BaseSymbolizer=None, Geometry=None, Graphic=None):
        super(PointSymbolizerTypeSub, self).__init__(version, uom, Name, Description, BaseSymbolizer, Geometry, Graphic, )
supermod.PointSymbolizerType.subclass = PointSymbolizerTypeSub
# end class PointSymbolizerTypeSub


class GraphicTypeSub(supermod.GraphicType):
    def __init__(self, ExternalGraphic=None, Mark=None, Opacity=None, Size=None, Rotation=None, AnchorPoint=None, Displacement=None):
        super(GraphicTypeSub, self).__init__(ExternalGraphic, Mark, Opacity, Size, Rotation, AnchorPoint, Displacement, )
supermod.GraphicType.subclass = GraphicTypeSub
# end class GraphicTypeSub


class ExternalGraphicTypeSub(supermod.ExternalGraphicType):
    def __init__(self, OnlineResource=None, InlineContent=None, Format=None, ColorReplacement=None):
        super(ExternalGraphicTypeSub, self).__init__(OnlineResource, InlineContent, Format, ColorReplacement, )
supermod.ExternalGraphicType.subclass = ExternalGraphicTypeSub
# end class ExternalGraphicTypeSub


class ColorReplacementTypeSub(supermod.ColorReplacementType):
    def __init__(self, Recode=None):
        super(ColorReplacementTypeSub, self).__init__(Recode, )
supermod.ColorReplacementType.subclass = ColorReplacementTypeSub
# end class ColorReplacementTypeSub


class MarkTypeSub(supermod.MarkType):
    def __init__(self, WellKnownName=None, OnlineResource=None, InlineContent=None, Format=None, MarkIndex=None, Fill=None, Stroke=None):
        super(MarkTypeSub, self).__init__(WellKnownName, OnlineResource, InlineContent, Format, MarkIndex, Fill, Stroke, )
supermod.MarkType.subclass = MarkTypeSub
# end class MarkTypeSub


class TextSymbolizerTypeSub(supermod.TextSymbolizerType):
    def __init__(self, version=None, uom=None, Name=None, Description=None, BaseSymbolizer=None, Geometry=None, Label=None, Font=None, LabelPlacement=None, Halo=None, Fill=None):
        super(TextSymbolizerTypeSub, self).__init__(version, uom, Name, Description, BaseSymbolizer, Geometry, Label, Font, LabelPlacement, Halo, Fill, )
supermod.TextSymbolizerType.subclass = TextSymbolizerTypeSub
# end class TextSymbolizerTypeSub


class FontTypeSub(supermod.FontType):
    def __init__(self, SvgParameter=None):
        super(FontTypeSub, self).__init__(SvgParameter, )
supermod.FontType.subclass = FontTypeSub
# end class FontTypeSub


class LabelPlacementTypeSub(supermod.LabelPlacementType):
    def __init__(self, PointPlacement=None, LinePlacement=None):
        super(LabelPlacementTypeSub, self).__init__(PointPlacement, LinePlacement, )
supermod.LabelPlacementType.subclass = LabelPlacementTypeSub
# end class LabelPlacementTypeSub


class PointPlacementTypeSub(supermod.PointPlacementType):
    def __init__(self, AnchorPoint=None, Displacement=None, Rotation=None):
        super(PointPlacementTypeSub, self).__init__(AnchorPoint, Displacement, Rotation, )
supermod.PointPlacementType.subclass = PointPlacementTypeSub
# end class PointPlacementTypeSub


class AnchorPointTypeSub(supermod.AnchorPointType):
    def __init__(self, AnchorPointX=None, AnchorPointY=None):
        super(AnchorPointTypeSub, self).__init__(AnchorPointX, AnchorPointY, )
supermod.AnchorPointType.subclass = AnchorPointTypeSub
# end class AnchorPointTypeSub


class DisplacementTypeSub(supermod.DisplacementType):
    def __init__(self, DisplacementX=None, DisplacementY=None):
        super(DisplacementTypeSub, self).__init__(DisplacementX, DisplacementY, )
supermod.DisplacementType.subclass = DisplacementTypeSub
# end class DisplacementTypeSub


class LinePlacementTypeSub(supermod.LinePlacementType):
    def __init__(self, PerpendicularOffset=None, IsRepeated=None, InitialGap=None, Gap=None, IsAligned=None, GeneralizeLine=None):
        super(LinePlacementTypeSub, self).__init__(PerpendicularOffset, IsRepeated, InitialGap, Gap, IsAligned, GeneralizeLine, )
supermod.LinePlacementType.subclass = LinePlacementTypeSub
# end class LinePlacementTypeSub


class HaloTypeSub(supermod.HaloType):
    def __init__(self, Radius=None, Fill=None):
        super(HaloTypeSub, self).__init__(Radius, Fill, )
supermod.HaloType.subclass = HaloTypeSub
# end class HaloTypeSub


class RasterSymbolizerTypeSub(supermod.RasterSymbolizerType):
    def __init__(self, version=None, uom=None, Name=None, Description=None, BaseSymbolizer=None, Geometry=None, Opacity=None, ChannelSelection=None, OverlapBehavior=None, ColorMap=None, ContrastEnhancement=None, ShadedRelief=None, ImageOutline=None):
        super(RasterSymbolizerTypeSub, self).__init__(version, uom, Name, Description, BaseSymbolizer, Geometry, Opacity, ChannelSelection, OverlapBehavior, ColorMap, ContrastEnhancement, ShadedRelief, ImageOutline, )
supermod.RasterSymbolizerType.subclass = RasterSymbolizerTypeSub
# end class RasterSymbolizerTypeSub


class ChannelSelectionTypeSub(supermod.ChannelSelectionType):
    def __init__(self, RedChannel=None, GreenChannel=None, BlueChannel=None, GrayChannel=None):
        super(ChannelSelectionTypeSub, self).__init__(RedChannel, GreenChannel, BlueChannel, GrayChannel, )
supermod.ChannelSelectionType.subclass = ChannelSelectionTypeSub
# end class ChannelSelectionTypeSub


class SelectedChannelTypeSub(supermod.SelectedChannelType):
    def __init__(self, SourceChannelName=None, ContrastEnhancement=None):
        super(SelectedChannelTypeSub, self).__init__(SourceChannelName, ContrastEnhancement, )
supermod.SelectedChannelType.subclass = SelectedChannelTypeSub
# end class SelectedChannelTypeSub


class ColorMapTypeSub(supermod.ColorMapType):
    def __init__(self, Categorize=None, Interpolate=None):
        super(ColorMapTypeSub, self).__init__(Categorize, Interpolate, )
supermod.ColorMapType.subclass = ColorMapTypeSub
# end class ColorMapTypeSub


class ContrastEnhancementTypeSub(supermod.ContrastEnhancementType):
    def __init__(self, Normalize=None, Histogram=None, GammaValue=None):
        super(ContrastEnhancementTypeSub, self).__init__(Normalize, Histogram, GammaValue, )
supermod.ContrastEnhancementType.subclass = ContrastEnhancementTypeSub
# end class ContrastEnhancementTypeSub


class NormalizeTypeSub(supermod.NormalizeType):
    def __init__(self):
        super(NormalizeTypeSub, self).__init__()
supermod.NormalizeType.subclass = NormalizeTypeSub
# end class NormalizeTypeSub


class HistogramTypeSub(supermod.HistogramType):
    def __init__(self):
        super(HistogramTypeSub, self).__init__()
supermod.HistogramType.subclass = HistogramTypeSub
# end class HistogramTypeSub


class ShadedReliefTypeSub(supermod.ShadedReliefType):
    def __init__(self, BrightnessOnly=None, ReliefFactor=None):
        super(ShadedReliefTypeSub, self).__init__(BrightnessOnly, ReliefFactor, )
supermod.ShadedReliefType.subclass = ShadedReliefTypeSub
# end class ShadedReliefTypeSub


class ImageOutlineTypeSub(supermod.ImageOutlineType):
    def __init__(self, LineSymbolizer=None, PolygonSymbolizer=None):
        super(ImageOutlineTypeSub, self).__init__(LineSymbolizer, PolygonSymbolizer, )
supermod.ImageOutlineType.subclass = ImageOutlineTypeSub
# end class ImageOutlineTypeSub


class FormatNumberTypeSub(supermod.FormatNumberType):
    def __init__(self, fallbackValue=None, decimalPoint='.', groupingSeparator=',', NumericValue=None, Pattern=None, NegativePattern=None):
        super(FormatNumberTypeSub, self).__init__(fallbackValue, decimalPoint, groupingSeparator, NumericValue, Pattern, NegativePattern, )
supermod.FormatNumberType.subclass = FormatNumberTypeSub
# end class FormatNumberTypeSub


class FormatDateTypeSub(supermod.FormatDateType):
    def __init__(self, fallbackValue=None, DateValue=None, Pattern=None):
        super(FormatDateTypeSub, self).__init__(fallbackValue, DateValue, Pattern, )
supermod.FormatDateType.subclass = FormatDateTypeSub
# end class FormatDateTypeSub


class SubstringTypeSub(supermod.SubstringType):
    def __init__(self, fallbackValue=None, StringValue=None, Position=None, Length=None):
        super(SubstringTypeSub, self).__init__(fallbackValue, StringValue, Position, Length, )
supermod.SubstringType.subclass = SubstringTypeSub
# end class SubstringTypeSub


class ConcatenateTypeSub(supermod.ConcatenateType):
    def __init__(self, fallbackValue=None, StringValue=None):
        super(ConcatenateTypeSub, self).__init__(fallbackValue, StringValue, )
supermod.ConcatenateType.subclass = ConcatenateTypeSub
# end class ConcatenateTypeSub


class ChangeCaseTypeSub(supermod.ChangeCaseType):
    def __init__(self, fallbackValue=None, direction=None, StringValue=None):
        super(ChangeCaseTypeSub, self).__init__(fallbackValue, direction, StringValue, )
supermod.ChangeCaseType.subclass = ChangeCaseTypeSub
# end class ChangeCaseTypeSub


class TrimTypeSub(supermod.TrimType):
    def __init__(self, fallbackValue=None, stripOffPosition=None, stripOffChar=None, StringValue=None):
        super(TrimTypeSub, self).__init__(fallbackValue, stripOffPosition, stripOffChar, StringValue, )
supermod.TrimType.subclass = TrimTypeSub
# end class TrimTypeSub


class StringPositionTypeSub(supermod.StringPositionType):
    def __init__(self, fallbackValue=None, searchDirection=None, LookupString=None, StringValue=None):
        super(StringPositionTypeSub, self).__init__(fallbackValue, searchDirection, LookupString, StringValue, )
supermod.StringPositionType.subclass = StringPositionTypeSub
# end class StringPositionTypeSub


class StringLengthTypeSub(supermod.StringLengthType):
    def __init__(self, fallbackValue=None, StringValue=None):
        super(StringLengthTypeSub, self).__init__(fallbackValue, StringValue, )
supermod.StringLengthType.subclass = StringLengthTypeSub
# end class StringLengthTypeSub


class CategorizeTypeSub(supermod.CategorizeType):
    def __init__(self, fallbackValue=None, threshholdsBelongTo=None, LookupValue=None, Threshold=None, Value=None):
        super(CategorizeTypeSub, self).__init__(fallbackValue, threshholdsBelongTo, LookupValue, Threshold, Value, )
supermod.CategorizeType.subclass = CategorizeTypeSub
# end class CategorizeTypeSub


class InterpolateTypeSub(supermod.InterpolateType):
    def __init__(self, fallbackValue=None, mode=None, method=None, LookupValue=None, InterpolationPoint=None):
        super(InterpolateTypeSub, self).__init__(fallbackValue, mode, method, LookupValue, InterpolationPoint, )
supermod.InterpolateType.subclass = InterpolateTypeSub
# end class InterpolateTypeSub


class InterpolationPointTypeSub(supermod.InterpolationPointType):
    def __init__(self, Data=None, Value=None):
        super(InterpolationPointTypeSub, self).__init__(Data, Value, )
supermod.InterpolationPointType.subclass = InterpolationPointTypeSub
# end class InterpolationPointTypeSub


class RecodeTypeSub(supermod.RecodeType):
    def __init__(self, fallbackValue=None, LookupValue=None, MapItem=None):
        super(RecodeTypeSub, self).__init__(fallbackValue, LookupValue, MapItem, )
supermod.RecodeType.subclass = RecodeTypeSub
# end class RecodeTypeSub


class MapItemTypeSub(supermod.MapItemType):
    def __init__(self, Data=None, Value=None):
        super(MapItemTypeSub, self).__init__(Data, Value, )
supermod.MapItemType.subclass = MapItemTypeSub
# end class MapItemTypeSub


class DescriptionTypeSub(supermod.DescriptionType):
    def __init__(self, Title=None, Abstract=None):
        super(DescriptionTypeSub, self).__init__(Title, Abstract, )
supermod.DescriptionType.subclass = DescriptionTypeSub
# end class DescriptionTypeSub


class OnlineResourceTypeSub(supermod.OnlineResourceType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None):
        super(OnlineResourceTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, )
supermod.OnlineResourceType.subclass = OnlineResourceTypeSub
# end class OnlineResourceTypeSub


class InlineContentTypeSub(supermod.InlineContentType):
    def __init__(self, encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(InlineContentTypeSub, self).__init__(encoding, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.InlineContentType.subclass = InlineContentTypeSub
# end class InlineContentTypeSub


class BaseRequestTypeSub(supermod.BaseRequestType):
    def __init__(self, service='WFS', version='1.1.0', handle=None, extensiontype_=None):
        super(BaseRequestTypeSub, self).__init__(service, version, handle, extensiontype_, )
supermod.BaseRequestType.subclass = BaseRequestTypeSub
# end class BaseRequestTypeSub


class XlinkPropertyNameSub(supermod.XlinkPropertyName):
    def __init__(self, traverseXlinkDepth=None, traverseXlinkExpiry=None, valueOf_=None):
        super(XlinkPropertyNameSub, self).__init__(traverseXlinkDepth, traverseXlinkExpiry, valueOf_, )
supermod.XlinkPropertyName.subclass = XlinkPropertyNameSub
# end class XlinkPropertyNameSub


class FeatureTypeListTypeSub(supermod.FeatureTypeListType):
    def __init__(self, Operations=None, FeatureType=None):
        super(FeatureTypeListTypeSub, self).__init__(Operations, FeatureType, )
supermod.FeatureTypeListType.subclass = FeatureTypeListTypeSub
# end class FeatureTypeListTypeSub


class FeatureTypeTypeSub(supermod.FeatureTypeType):
    def __init__(self, Name=None, Title=None, Abstract=None, Keywords=None, DefaultSRS=None, OtherSRS=None, NoSRS=None, Operations=None, OutputFormats=None, WGS84BoundingBox=None, MetadataURL=None):
        super(FeatureTypeTypeSub, self).__init__(Name, Title, Abstract, Keywords, DefaultSRS, OtherSRS, NoSRS, Operations, OutputFormats, WGS84BoundingBox, MetadataURL, )
supermod.FeatureTypeType.subclass = FeatureTypeTypeSub
# end class FeatureTypeTypeSub


class OperationsTypeSub(supermod.OperationsType):
    def __init__(self, Operation=None):
        super(OperationsTypeSub, self).__init__(Operation, )
supermod.OperationsType.subclass = OperationsTypeSub
# end class OperationsTypeSub


class OutputFormatListTypeSub(supermod.OutputFormatListType):
    def __init__(self, Format=None):
        super(OutputFormatListTypeSub, self).__init__(Format, )
supermod.OutputFormatListType.subclass = OutputFormatListTypeSub
# end class OutputFormatListTypeSub


class MetadataURLTypeSub(supermod.MetadataURLType):
    def __init__(self, type_=None, format=None, valueOf_=None):
        super(MetadataURLTypeSub, self).__init__(type_, format, valueOf_, )
supermod.MetadataURLType.subclass = MetadataURLTypeSub
# end class MetadataURLTypeSub


class GMLObjectTypeListTypeSub(supermod.GMLObjectTypeListType):
    def __init__(self, GMLObjectType=None):
        super(GMLObjectTypeListTypeSub, self).__init__(GMLObjectType, )
supermod.GMLObjectTypeListType.subclass = GMLObjectTypeListTypeSub
# end class GMLObjectTypeListTypeSub


class GMLObjectTypeTypeSub(supermod.GMLObjectTypeType):
    def __init__(self, Name=None, Title=None, Abstract=None, Keywords=None, OutputFormats=None):
        super(GMLObjectTypeTypeSub, self).__init__(Name, Title, Abstract, Keywords, OutputFormats, )
supermod.GMLObjectTypeType.subclass = GMLObjectTypeTypeSub
# end class GMLObjectTypeTypeSub


class DescribeFeatureTypeTypeSub(supermod.DescribeFeatureTypeType):
    def __init__(self, service='WFS', version='1.1.0', handle=None, outputFormat='text/xml; subtype=gml/3.1.1', TypeName=None):
        super(DescribeFeatureTypeTypeSub, self).__init__(service, version, handle, outputFormat, TypeName, )
supermod.DescribeFeatureTypeType.subclass = DescribeFeatureTypeTypeSub
# end class DescribeFeatureTypeTypeSub


class GetFeatureTypeSub(supermod.GetFeatureType):
    def __init__(self, service='WFS', version='1.1.0', handle=None, resultType='results', outputFormat='text/xml; subtype=gml/3.1.1', maxFeatures=None, traverseXlinkDepth=None, traverseXlinkExpiry=None, Query=None):
        super(GetFeatureTypeSub, self).__init__(service, version, handle, resultType, outputFormat, maxFeatures, traverseXlinkDepth, traverseXlinkExpiry, Query, )
supermod.GetFeatureType.subclass = GetFeatureTypeSub
# end class GetFeatureTypeSub


class QueryTypeSub(supermod.QueryType):
    def __init__(self, handle=None, typeName=None, featureVersion=None, srsName=None, PropertyName=None, XlinkPropertyName=None, Function=None, Filter=None, SortBy=None):
        super(QueryTypeSub, self).__init__(handle, typeName, featureVersion, srsName, PropertyName, XlinkPropertyName, Function, Filter, SortBy, )
supermod.QueryType.subclass = QueryTypeSub
# end class QueryTypeSub


class GetGmlObjectTypeSub(supermod.GetGmlObjectType):
    def __init__(self, service='WFS', version='1.1.0', handle=None, outputFormat='GML3', traverseXlinkDepth=None, traverseXlinkExpiry=None, GmlObjectId=None):
        super(GetGmlObjectTypeSub, self).__init__(service, version, handle, outputFormat, traverseXlinkDepth, traverseXlinkExpiry, GmlObjectId, )
supermod.GetGmlObjectType.subclass = GetGmlObjectTypeSub
# end class GetGmlObjectTypeSub


class GetFeatureWithLockTypeSub(supermod.GetFeatureWithLockType):
    def __init__(self, service='WFS', version='1.1.0', handle=None, expiry=5, resultType='results', outputFormat='text/xml; subtype=gml/3.1.1', maxFeatures=None, traverseXlinkDepth=None, traverseXlinkExpiry=None, Query=None):
        super(GetFeatureWithLockTypeSub, self).__init__(service, version, handle, expiry, resultType, outputFormat, maxFeatures, traverseXlinkDepth, traverseXlinkExpiry, Query, )
supermod.GetFeatureWithLockType.subclass = GetFeatureWithLockTypeSub
# end class GetFeatureWithLockTypeSub


class LockFeatureTypeSub(supermod.LockFeatureType):
    def __init__(self, service='WFS', version='1.1.0', handle=None, expiry=5, lockAction='ALL', Lock=None):
        super(LockFeatureTypeSub, self).__init__(service, version, handle, expiry, lockAction, Lock, )
supermod.LockFeatureType.subclass = LockFeatureTypeSub
# end class LockFeatureTypeSub


class LockTypeSub(supermod.LockType):
    def __init__(self, handle=None, typeName=None, Filter=None):
        super(LockTypeSub, self).__init__(handle, typeName, Filter, )
supermod.LockType.subclass = LockTypeSub
# end class LockTypeSub


class LockFeatureResponseTypeSub(supermod.LockFeatureResponseType):
    def __init__(self, LockId=None, FeaturesLocked=None, FeaturesNotLocked=None):
        super(LockFeatureResponseTypeSub, self).__init__(LockId, FeaturesLocked, FeaturesNotLocked, )
supermod.LockFeatureResponseType.subclass = LockFeatureResponseTypeSub
# end class LockFeatureResponseTypeSub


class FeaturesLockedTypeSub(supermod.FeaturesLockedType):
    def __init__(self, FeatureId=None):
        super(FeaturesLockedTypeSub, self).__init__(FeatureId, )
supermod.FeaturesLockedType.subclass = FeaturesLockedTypeSub
# end class FeaturesLockedTypeSub


class FeaturesNotLockedTypeSub(supermod.FeaturesNotLockedType):
    def __init__(self, FeatureId=None):
        super(FeaturesNotLockedTypeSub, self).__init__(FeatureId, )
supermod.FeaturesNotLockedType.subclass = FeaturesNotLockedTypeSub
# end class FeaturesNotLockedTypeSub


class TransactionTypeSub(supermod.TransactionType):
    def __init__(self, service='WFS', version='1.1.0', handle=None, releaseAction=None, LockId=None, Insert=None, Update=None, Delete=None, Native=None):
        super(TransactionTypeSub, self).__init__(service, version, handle, releaseAction, LockId, Insert, Update, Delete, Native, )
supermod.TransactionType.subclass = TransactionTypeSub
# end class TransactionTypeSub


class InsertElementTypeSub(supermod.InsertElementType):
    def __init__(self, idgen='GenerateNew', handle=None, inputFormat='text/xml; subtype=gml/3.1.1', srsName=None, _Feature=None):
        super(InsertElementTypeSub, self).__init__(idgen, handle, inputFormat, srsName, _Feature, )
supermod.InsertElementType.subclass = InsertElementTypeSub
# end class InsertElementTypeSub


class UpdateElementTypeSub(supermod.UpdateElementType):
    def __init__(self, handle=None, typeName=None, inputFormat='x-application/gml:3', srsName=None, Property=None, Filter=None):
        super(UpdateElementTypeSub, self).__init__(handle, typeName, inputFormat, srsName, Property, Filter, )
supermod.UpdateElementType.subclass = UpdateElementTypeSub
# end class UpdateElementTypeSub


class PropertyTypeSub(supermod.PropertyType):
    def __init__(self, Name=None, Value=None):
        super(PropertyTypeSub, self).__init__(Name, Value, )
supermod.PropertyType.subclass = PropertyTypeSub
# end class PropertyTypeSub


class ValueSub(supermod.Value):
    def __init__(self):
        super(ValueSub, self).__init__()
supermod.Value.subclass = ValueSub
# end class ValueSub


class DeleteElementTypeSub(supermod.DeleteElementType):
    def __init__(self, handle=None, typeName=None, Filter=None):
        super(DeleteElementTypeSub, self).__init__(handle, typeName, Filter, )
supermod.DeleteElementType.subclass = DeleteElementTypeSub
# end class DeleteElementTypeSub


class NativeTypeSub(supermod.NativeType):
    def __init__(self, vendorId=None, safeToIgnore=None):
        super(NativeTypeSub, self).__init__(vendorId, safeToIgnore, )
supermod.NativeType.subclass = NativeTypeSub
# end class NativeTypeSub


class TransactionResponseTypeSub(supermod.TransactionResponseType):
    def __init__(self, version=None, TransactionSummary=None, TransactionResults=None, InsertResults=None):
        super(TransactionResponseTypeSub, self).__init__(version, TransactionSummary, TransactionResults, InsertResults, )
supermod.TransactionResponseType.subclass = TransactionResponseTypeSub
# end class TransactionResponseTypeSub


class TransactionSummaryTypeSub(supermod.TransactionSummaryType):
    def __init__(self, totalInserted=None, totalUpdated=None, totalDeleted=None):
        super(TransactionSummaryTypeSub, self).__init__(totalInserted, totalUpdated, totalDeleted, )
supermod.TransactionSummaryType.subclass = TransactionSummaryTypeSub
# end class TransactionSummaryTypeSub


class TransactionResultsTypeSub(supermod.TransactionResultsType):
    def __init__(self, Action=None):
        super(TransactionResultsTypeSub, self).__init__(Action, )
supermod.TransactionResultsType.subclass = TransactionResultsTypeSub
# end class TransactionResultsTypeSub


class ActionTypeSub(supermod.ActionType):
    def __init__(self, locator=None, code=None, Message=None):
        super(ActionTypeSub, self).__init__(locator, code, Message, )
supermod.ActionType.subclass = ActionTypeSub
# end class ActionTypeSub


class InsertResultsTypeSub(supermod.InsertResultsType):
    def __init__(self, Feature=None):
        super(InsertResultsTypeSub, self).__init__(Feature, )
supermod.InsertResultsType.subclass = InsertResultsTypeSub
# end class InsertResultsTypeSub


class InsertedFeatureTypeSub(supermod.InsertedFeatureType):
    def __init__(self, handle=None, FeatureId=None):
        super(InsertedFeatureTypeSub, self).__init__(handle, FeatureId, )
supermod.InsertedFeatureType.subclass = InsertedFeatureTypeSub
# end class InsertedFeatureTypeSub


class CapabilitiesBaseTypeSub(supermod.CapabilitiesBaseType):
    def __init__(self, version=None, updateSequence=None, ServiceIdentification=None, ServiceProvider=None, OperationsMetadata=None, extensiontype_=None):
        super(CapabilitiesBaseTypeSub, self).__init__(version, updateSequence, ServiceIdentification, ServiceProvider, OperationsMetadata, extensiontype_, )
supermod.CapabilitiesBaseType.subclass = CapabilitiesBaseTypeSub
# end class CapabilitiesBaseTypeSub


class GetCapabilitiesTypeSub(supermod.GetCapabilitiesType):
    def __init__(self, updateSequence=None, AcceptVersions=None, Sections=None, AcceptFormats=None, extensiontype_=None):
        super(GetCapabilitiesTypeSub, self).__init__(updateSequence, AcceptVersions, Sections, AcceptFormats, extensiontype_, )
supermod.GetCapabilitiesType.subclass = GetCapabilitiesTypeSub
# end class GetCapabilitiesTypeSub


class AcceptVersionsTypeSub(supermod.AcceptVersionsType):
    def __init__(self, Version=None):
        super(AcceptVersionsTypeSub, self).__init__(Version, )
supermod.AcceptVersionsType.subclass = AcceptVersionsTypeSub
# end class AcceptVersionsTypeSub


class SectionsTypeSub(supermod.SectionsType):
    def __init__(self, Section=None):
        super(SectionsTypeSub, self).__init__(Section, )
supermod.SectionsType.subclass = SectionsTypeSub
# end class SectionsTypeSub


class AcceptFormatsTypeSub(supermod.AcceptFormatsType):
    def __init__(self, OutputFormat=None):
        super(AcceptFormatsTypeSub, self).__init__(OutputFormat, )
supermod.AcceptFormatsType.subclass = AcceptFormatsTypeSub
# end class AcceptFormatsTypeSub


class ServiceIdentificationSub(supermod.ServiceIdentification):
    def __init__(self, Title=None, Abstract=None, Keywords=None, ServiceType=None, ServiceTypeVersion=None, Fees=None, AccessConstraints=None):
        super(ServiceIdentificationSub, self).__init__(Title, Abstract, Keywords, ServiceType, ServiceTypeVersion, Fees, AccessConstraints, )
supermod.ServiceIdentification.subclass = ServiceIdentificationSub
# end class ServiceIdentificationSub


class IdentificationTypeSub(supermod.IdentificationType):
    def __init__(self, Title=None, Abstract=None, Keywords=None, Identifier=None, BoundingBox=None, OutputFormat=None, AvailableCRS=None, Metadata=None):
        super(IdentificationTypeSub, self).__init__(Title, Abstract, Keywords, Identifier, BoundingBox, OutputFormat, AvailableCRS, Metadata, )
supermod.IdentificationType.subclass = IdentificationTypeSub
# end class IdentificationTypeSub


class MetadataTypeSub(supermod.MetadataType):
    def __init__(self, about=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, AbstractMetaData=None):
        super(MetadataTypeSub, self).__init__(about, type_, href, role, arcrole, title, show, actuate, AbstractMetaData, )
supermod.MetadataType.subclass = MetadataTypeSub
# end class MetadataTypeSub


class AbstractMetaDataSub(supermod.AbstractMetaData):
    def __init__(self):
        super(AbstractMetaDataSub, self).__init__()
supermod.AbstractMetaData.subclass = AbstractMetaDataSub
# end class AbstractMetaDataSub


class BoundingBoxTypeSub(supermod.BoundingBoxType):
    def __init__(self, crs=None, dimensions=None, LowerCorner=None, UpperCorner=None):
        super(BoundingBoxTypeSub, self).__init__(crs, dimensions, LowerCorner, UpperCorner, )
supermod.BoundingBoxType.subclass = BoundingBoxTypeSub
# end class BoundingBoxTypeSub


class WGS84BoundingBoxTypeSub(supermod.WGS84BoundingBoxType):
    def __init__(self, crs=None, dimensions=None, LowerCorner=None, UpperCorner=None):
        super(WGS84BoundingBoxTypeSub, self).__init__(crs, dimensions, LowerCorner, UpperCorner, )
supermod.WGS84BoundingBoxType.subclass = WGS84BoundingBoxTypeSub
# end class WGS84BoundingBoxTypeSub


class KeywordsTypeSub(supermod.KeywordsType):
    def __init__(self, Keyword=None, Type=None):
        super(KeywordsTypeSub, self).__init__(Keyword, Type, )
supermod.KeywordsType.subclass = KeywordsTypeSub
# end class KeywordsTypeSub


class ResponsiblePartyTypeSub(supermod.ResponsiblePartyType):
    def __init__(self, IndividualName=None, OrganisationName=None, PositionName=None, ContactInfo=None, Role=None):
        super(ResponsiblePartyTypeSub, self).__init__(IndividualName, OrganisationName, PositionName, ContactInfo, Role, )
supermod.ResponsiblePartyType.subclass = ResponsiblePartyTypeSub
# end class ResponsiblePartyTypeSub


class ResponsiblePartySubsetTypeSub(supermod.ResponsiblePartySubsetType):
    def __init__(self, IndividualName=None, PositionName=None, ContactInfo=None, Role=None):
        super(ResponsiblePartySubsetTypeSub, self).__init__(IndividualName, PositionName, ContactInfo, Role, )
supermod.ResponsiblePartySubsetType.subclass = ResponsiblePartySubsetTypeSub
# end class ResponsiblePartySubsetTypeSub


class ContactTypeSub(supermod.ContactType):
    def __init__(self, Phone=None, Address=None, OnlineResource=None, HoursOfService=None, ContactInstructions=None):
        super(ContactTypeSub, self).__init__(Phone, Address, OnlineResource, HoursOfService, ContactInstructions, )
supermod.ContactType.subclass = ContactTypeSub
# end class ContactTypeSub


class TelephoneTypeSub(supermod.TelephoneType):
    def __init__(self, Voice=None, Facsimile=None):
        super(TelephoneTypeSub, self).__init__(Voice, Facsimile, )
supermod.TelephoneType.subclass = TelephoneTypeSub
# end class TelephoneTypeSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, DeliveryPoint=None, City=None, AdministrativeArea=None, PostalCode=None, Country=None, ElectronicMailAddress=None):
        super(AddressTypeSub, self).__init__(DeliveryPoint, City, AdministrativeArea, PostalCode, Country, ElectronicMailAddress, )
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class ServiceProviderSub(supermod.ServiceProvider):
    def __init__(self, ProviderName=None, ProviderSite=None, ServiceContact=None):
        super(ServiceProviderSub, self).__init__(ProviderName, ProviderSite, ServiceContact, )
supermod.ServiceProvider.subclass = ServiceProviderSub
# end class ServiceProviderSub


class OperationsMetadataSub(supermod.OperationsMetadata):
    def __init__(self, Operation=None, Parameter=None, Constraint=None, ExtendedCapabilities=None):
        super(OperationsMetadataSub, self).__init__(Operation, Parameter, Constraint, ExtendedCapabilities, )
supermod.OperationsMetadata.subclass = OperationsMetadataSub
# end class OperationsMetadataSub


class OperationSub(supermod.Operation):
    def __init__(self, name=None, DCP=None, Parameter=None, Constraint=None, Metadata=None):
        super(OperationSub, self).__init__(name, DCP, Parameter, Constraint, Metadata, )
supermod.Operation.subclass = OperationSub
# end class OperationSub


class DCPSub(supermod.DCP):
    def __init__(self, HTTP=None):
        super(DCPSub, self).__init__(HTTP, )
supermod.DCP.subclass = DCPSub
# end class DCPSub


class RequestMethodTypeSub(supermod.RequestMethodType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, Constraint=None):
        super(RequestMethodTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, Constraint, )
supermod.RequestMethodType.subclass = RequestMethodTypeSub
# end class RequestMethodTypeSub


class DomainTypeSub(supermod.DomainType):
    def __init__(self, name=None, Value=None, Metadata=None):
        super(DomainTypeSub, self).__init__(name, Value, Metadata, )
supermod.DomainType.subclass = DomainTypeSub
# end class DomainTypeSub


class ExceptionReportSub(supermod.ExceptionReport):
    def __init__(self, version=None, language=None, Exception=None):
        super(ExceptionReportSub, self).__init__(version, language, Exception, )
supermod.ExceptionReport.subclass = ExceptionReportSub
# end class ExceptionReportSub


class ExceptionTypeSub(supermod.ExceptionType):
    def __init__(self, exceptionCode=None, locator=None, ExceptionText=None):
        super(ExceptionTypeSub, self).__init__(exceptionCode, locator, ExceptionText, )
supermod.ExceptionType.subclass = ExceptionTypeSub
# end class ExceptionTypeSub


class GetMapTypeSub(supermod.GetMapType):
    def __init__(self, version=None, StyledLayerDescriptor=None, CRS=None, BoundingBox=None, Output=None, Exceptions=None, Time=None, Elevation=None):
        super(GetMapTypeSub, self).__init__(version, StyledLayerDescriptor, CRS, BoundingBox, Output, Exceptions, Time, Elevation, )
supermod.GetMapType.subclass = GetMapTypeSub
# end class GetMapTypeSub


class OutputTypeSub(supermod.OutputType):
    def __init__(self, Size=None, Format=None, Transparent=None, BGcolor=None):
        super(OutputTypeSub, self).__init__(Size, Format, Transparent, BGcolor, )
supermod.OutputType.subclass = OutputTypeSub
# end class OutputTypeSub


class ElevationTypeSub(supermod.ElevationType):
    def __init__(self, Value=None, Interval=None):
        super(ElevationTypeSub, self).__init__(Value, Interval, )
supermod.ElevationType.subclass = ElevationTypeSub
# end class ElevationTypeSub


class IntervalTypeSub(supermod.IntervalType):
    def __init__(self, Min=None, Max=None):
        super(IntervalTypeSub, self).__init__(Min, Max, )
supermod.IntervalType.subclass = IntervalTypeSub
# end class IntervalTypeSub


class WMS_CapabilitiesSub(supermod.WMS_Capabilities):
    def __init__(self, version=None, updateSequence=None, Service=None, Capability=None):
        super(WMS_CapabilitiesSub, self).__init__(version, updateSequence, Service, Capability, )
supermod.WMS_Capabilities.subclass = WMS_CapabilitiesSub
# end class WMS_CapabilitiesSub


class KeywordListSub(supermod.KeywordList):
    def __init__(self, Keyword=None):
        super(KeywordListSub, self).__init__(Keyword, )
supermod.KeywordList.subclass = KeywordListSub
# end class KeywordListSub


class KeywordSub(supermod.Keyword):
    def __init__(self, vocabulary=None, valueOf_=None):
        super(KeywordSub, self).__init__(vocabulary, valueOf_, )
supermod.Keyword.subclass = KeywordSub
# end class KeywordSub


class OnlineResourceSub(supermod.OnlineResource):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None):
        super(OnlineResourceSub, self).__init__(type_, href, role, arcrole, title, show, actuate, )
supermod.OnlineResource.subclass = OnlineResourceSub
# end class OnlineResourceSub


class ContactInformationSub(supermod.ContactInformation):
    def __init__(self, ContactPersonPrimary=None, ContactPosition=None, ContactAddress=None, ContactVoiceTelephone=None, ContactFacsimileTelephone=None, ContactElectronicMailAddress=None):
        super(ContactInformationSub, self).__init__(ContactPersonPrimary, ContactPosition, ContactAddress, ContactVoiceTelephone, ContactFacsimileTelephone, ContactElectronicMailAddress, )
supermod.ContactInformation.subclass = ContactInformationSub
# end class ContactInformationSub


class ContactPersonPrimarySub(supermod.ContactPersonPrimary):
    def __init__(self, ContactPerson=None, ContactOrganization=None):
        super(ContactPersonPrimarySub, self).__init__(ContactPerson, ContactOrganization, )
supermod.ContactPersonPrimary.subclass = ContactPersonPrimarySub
# end class ContactPersonPrimarySub


class ContactAddressSub(supermod.ContactAddress):
    def __init__(self, AddressType=None, Address=None, City=None, StateOrProvince=None, PostCode=None, Country=None):
        super(ContactAddressSub, self).__init__(AddressType, Address, City, StateOrProvince, PostCode, Country, )
supermod.ContactAddress.subclass = ContactAddressSub
# end class ContactAddressSub


class CapabilitySub(supermod.Capability):
    def __init__(self, Request=None, Exception=None, _ExtendedCapabilities=None, Layer=None):
        super(CapabilitySub, self).__init__(Request, Exception, _ExtendedCapabilities, Layer, )
supermod.Capability.subclass = CapabilitySub
# end class CapabilitySub


class RequestSub(supermod.Request):
    def __init__(self, GetCapabilities=None, GetMap=None, GetFeatureInfo=None, _ExtendedOperation=None):
        super(RequestSub, self).__init__(GetCapabilities, GetMap, GetFeatureInfo, _ExtendedOperation, )
supermod.Request.subclass = RequestSub
# end class RequestSub


class DCPTypeSub(supermod.DCPType):
    def __init__(self, HTTP=None):
        super(DCPTypeSub, self).__init__(HTTP, )
supermod.DCPType.subclass = DCPTypeSub
# end class DCPTypeSub


class HTTPSub(supermod.HTTP):
    def __init__(self, Get=None, Post=None):
        super(HTTPSub, self).__init__(Get, Post, )
supermod.HTTP.subclass = HTTPSub
# end class HTTPSub


class GetSub(supermod.Get):
    def __init__(self, OnlineResource=None):
        super(GetSub, self).__init__(OnlineResource, )
supermod.Get.subclass = GetSub
# end class GetSub


class PostSub(supermod.Post):
    def __init__(self, OnlineResource=None):
        super(PostSub, self).__init__(OnlineResource, )
supermod.Post.subclass = PostSub
# end class PostSub


class ExceptionSub(supermod.Exception):
    def __init__(self, Format=None):
        super(ExceptionSub, self).__init__(Format, )
supermod.Exception.subclass = ExceptionSub
# end class ExceptionSub


class _ExtendedCapabilitiesSub(supermod._ExtendedCapabilities):
    def __init__(self):
        super(_ExtendedCapabilitiesSub, self).__init__()
supermod._ExtendedCapabilities.subclass = _ExtendedCapabilitiesSub
# end class _ExtendedCapabilitiesSub


class LayerSub(supermod.Layer):
    def __init__(self, queryable='0', cascaded=None, opaque='0', noSubsets='0', fixedWidth=None, fixedHeight=None, Name=None, Title=None, Abstract=None, KeywordList=None, CRS=None, EX_GeographicBoundingBox=None, BoundingBox=None, Dimension=None, Attribution=None, AuthorityURL=None, Identifier=None, MetadataURL=None, DataURL=None, FeatureListURL=None, Style=None, MinScaleDenominator=None, MaxScaleDenominator=None, Layer_member=None):
        super(LayerSub, self).__init__(queryable, cascaded, opaque, noSubsets, fixedWidth, fixedHeight, Name, Title, Abstract, KeywordList, CRS, EX_GeographicBoundingBox, BoundingBox, Dimension, Attribution, AuthorityURL, Identifier, MetadataURL, DataURL, FeatureListURL, Style, MinScaleDenominator, MaxScaleDenominator, Layer_member, )
supermod.Layer.subclass = LayerSub
# end class LayerSub


class EX_GeographicBoundingBoxSub(supermod.EX_GeographicBoundingBox):
    def __init__(self, westBoundLongitude=None, eastBoundLongitude=None, southBoundLatitude=None, northBoundLatitude=None):
        super(EX_GeographicBoundingBoxSub, self).__init__(westBoundLongitude, eastBoundLongitude, southBoundLatitude, northBoundLatitude, )
supermod.EX_GeographicBoundingBox.subclass = EX_GeographicBoundingBoxSub
# end class EX_GeographicBoundingBoxSub


class BoundingBoxSub(supermod.BoundingBox):
    def __init__(self, CRS=None, minx=None, miny=None, maxx=None, maxy=None, resx=None, resy=None):
        super(BoundingBoxSub, self).__init__(CRS, minx, miny, maxx, maxy, resx, resy, )
supermod.BoundingBox.subclass = BoundingBoxSub
# end class BoundingBoxSub


class DimensionSub(supermod.Dimension):
    def __init__(self, name=None, units=None, unitSymbol=None, default=None, multipleValues=None, nearestValue=None, current=None, valueOf_=None):
        super(DimensionSub, self).__init__(name, units, unitSymbol, default, multipleValues, nearestValue, current, valueOf_, )
supermod.Dimension.subclass = DimensionSub
# end class DimensionSub


class AttributionSub(supermod.Attribution):
    def __init__(self, Title=None, OnlineResource=None, LogoURL=None):
        super(AttributionSub, self).__init__(Title, OnlineResource, LogoURL, )
supermod.Attribution.subclass = AttributionSub
# end class AttributionSub


class LogoURLSub(supermod.LogoURL):
    def __init__(self, width=None, height=None, Format=None, OnlineResource=None):
        super(LogoURLSub, self).__init__(width, height, Format, OnlineResource, )
supermod.LogoURL.subclass = LogoURLSub
# end class LogoURLSub


class MetadataURLSub(supermod.MetadataURL):
    def __init__(self, type_=None, Format=None, OnlineResource=None):
        super(MetadataURLSub, self).__init__(type_, Format, OnlineResource, )
supermod.MetadataURL.subclass = MetadataURLSub
# end class MetadataURLSub


class AuthorityURLSub(supermod.AuthorityURL):
    def __init__(self, name=None, OnlineResource=None):
        super(AuthorityURLSub, self).__init__(name, OnlineResource, )
supermod.AuthorityURL.subclass = AuthorityURLSub
# end class AuthorityURLSub


class IdentifierSub(supermod.Identifier):
    def __init__(self, authority=None, valueOf_=None):
        super(IdentifierSub, self).__init__(authority, valueOf_, )
supermod.Identifier.subclass = IdentifierSub
# end class IdentifierSub


class DataURLSub(supermod.DataURL):
    def __init__(self, Format=None, OnlineResource=None):
        super(DataURLSub, self).__init__(Format, OnlineResource, )
supermod.DataURL.subclass = DataURLSub
# end class DataURLSub


class FeatureListURLSub(supermod.FeatureListURL):
    def __init__(self, Format=None, OnlineResource=None):
        super(FeatureListURLSub, self).__init__(Format, OnlineResource, )
supermod.FeatureListURL.subclass = FeatureListURLSub
# end class FeatureListURLSub


class StyleSub(supermod.Style):
    def __init__(self, Name=None, Title=None, Abstract=None, LegendURL=None, StyleSheetURL=None, StyleURL=None):
        super(StyleSub, self).__init__(Name, Title, Abstract, LegendURL, StyleSheetURL, StyleURL, )
supermod.Style.subclass = StyleSub
# end class StyleSub


class LegendURLSub(supermod.LegendURL):
    def __init__(self, width=None, height=None, Format=None, OnlineResource=None):
        super(LegendURLSub, self).__init__(width, height, Format, OnlineResource, )
supermod.LegendURL.subclass = LegendURLSub
# end class LegendURLSub


class StyleSheetURLSub(supermod.StyleSheetURL):
    def __init__(self, Format=None, OnlineResource=None):
        super(StyleSheetURLSub, self).__init__(Format, OnlineResource, )
supermod.StyleSheetURL.subclass = StyleSheetURLSub
# end class StyleSheetURLSub


class StyleURLSub(supermod.StyleURL):
    def __init__(self, Format=None, OnlineResource=None):
        super(StyleURLSub, self).__init__(Format, OnlineResource, )
supermod.StyleURL.subclass = StyleURLSub
# end class StyleURLSub


class UserDefinedSymbolizationSub(supermod.UserDefinedSymbolization):
    def __init__(self, SupportSLD='0', UserLayer='0', UserStyle='0', RemoteWFS='0', InlineFeature='0', RemoteWCS='0'):
        super(UserDefinedSymbolizationSub, self).__init__(SupportSLD, UserLayer, UserStyle, RemoteWFS, InlineFeature, RemoteWCS, )
supermod.UserDefinedSymbolization.subclass = UserDefinedSymbolizationSub
# end class UserDefinedSymbolizationSub


class refLocationTypeSub(supermod.refLocationType):
    def __init__(self, AffinePlacement=None):
        super(refLocationTypeSub, self).__init__(AffinePlacement, )
supermod.refLocationType.subclass = refLocationTypeSub
# end class refLocationTypeSub


class rowTypeSub(supermod.rowType):
    def __init__(self, posList=None, pos=None, pointProperty=None):
        super(rowTypeSub, self).__init__(posList, pos, pointProperty, )
supermod.rowType.subclass = rowTypeSub
# end class rowTypeSub


class rowType1Sub(supermod.rowType1):
    def __init__(self, posList=None, pos=None, pointProperty=None):
        super(rowType1Sub, self).__init__(posList, pos, pointProperty, )
supermod.rowType1.subclass = rowType1Sub
# end class rowType1Sub


class controlPointTypeSub(supermod.controlPointType):
    def __init__(self, posList=None, pos=None, pointProperty=None):
        super(controlPointTypeSub, self).__init__(posList, pos, pointProperty, )
supermod.controlPointType.subclass = controlPointTypeSub
# end class controlPointTypeSub


class NoSRSTypeSub(supermod.NoSRSType):
    def __init__(self):
        super(NoSRSTypeSub, self).__init__()
supermod.NoSRSType.subclass = NoSRSTypeSub
# end class NoSRSTypeSub


class SizeTypeSub(supermod.SizeType):
    def __init__(self, Width=None, Height=None):
        super(SizeTypeSub, self).__init__(Width, Height, )
supermod.SizeType.subclass = SizeTypeSub
# end class SizeTypeSub


class WFS_CapabilitiesTypeSub(supermod.WFS_CapabilitiesType):
    def __init__(self, version=None, updateSequence=None, ServiceIdentification=None, ServiceProvider=None, OperationsMetadata=None, FeatureTypeList=None, ServesGMLObjectTypeList=None, SupportsGMLObjectTypeList=None, Filter_Capabilities=None):
        super(WFS_CapabilitiesTypeSub, self).__init__(version, updateSequence, ServiceIdentification, ServiceProvider, OperationsMetadata, FeatureTypeList, ServesGMLObjectTypeList, SupportsGMLObjectTypeList, Filter_Capabilities, )
supermod.WFS_CapabilitiesType.subclass = WFS_CapabilitiesTypeSub
# end class WFS_CapabilitiesTypeSub


class TemporalCRSTypeSub(supermod.TemporalCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, usesTemporalCS=None, usesTemporalDatum=None):
        super(TemporalCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, usesTemporalCS, usesTemporalDatum, )
supermod.TemporalCRSType.subclass = TemporalCRSTypeSub
# end class TemporalCRSTypeSub


class ImageCRSTypeSub(supermod.ImageCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, usesCartesianCS=None, usesObliqueCartesianCS=None, usesImageDatum=None):
        super(ImageCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, usesCartesianCS, usesObliqueCartesianCS, usesImageDatum, )
supermod.ImageCRSType.subclass = ImageCRSTypeSub
# end class ImageCRSTypeSub


class EngineeringCRSTypeSub(supermod.EngineeringCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, usesCS=None, usesEngineeringDatum=None):
        super(EngineeringCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, usesCS, usesEngineeringDatum, )
supermod.EngineeringCRSType.subclass = EngineeringCRSTypeSub
# end class EngineeringCRSTypeSub


class AbstractGeneralDerivedCRSTypeSub(supermod.AbstractGeneralDerivedCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, baseCRS=None, definedByConversion=None, extensiontype_=None):
        super(AbstractGeneralDerivedCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, baseCRS, definedByConversion, extensiontype_, )
supermod.AbstractGeneralDerivedCRSType.subclass = AbstractGeneralDerivedCRSTypeSub
# end class AbstractGeneralDerivedCRSTypeSub


class GeocentricCRSTypeSub(supermod.GeocentricCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, usesCartesianCS=None, usesSphericalCS=None, usesGeodeticDatum=None):
        super(GeocentricCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, usesCartesianCS, usesSphericalCS, usesGeodeticDatum, )
supermod.GeocentricCRSType.subclass = GeocentricCRSTypeSub
# end class GeocentricCRSTypeSub


class VerticalCRSTypeSub(supermod.VerticalCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, usesVerticalCS=None, usesVerticalDatum=None):
        super(VerticalCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, usesVerticalCS, usesVerticalDatum, )
supermod.VerticalCRSType.subclass = VerticalCRSTypeSub
# end class VerticalCRSTypeSub


class GeographicCRSTypeSub(supermod.GeographicCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, usesEllipsoidalCS=None, usesGeodeticDatum=None):
        super(GeographicCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, usesEllipsoidalCS, usesGeodeticDatum, )
supermod.GeographicCRSType.subclass = GeographicCRSTypeSub
# end class GeographicCRSTypeSub


class CompoundCRSTypeSub(supermod.CompoundCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, includesCRS=None):
        super(CompoundCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, includesCRS, )
supermod.CompoundCRSType.subclass = CompoundCRSTypeSub
# end class CompoundCRSTypeSub


class UnitDefinitionTypeSub(supermod.UnitDefinitionType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, quantityType=None, catalogSymbol=None, extensiontype_=None):
        super(UnitDefinitionTypeSub, self).__init__(id, metaDataProperty, description, name, quantityType, catalogSymbol, extensiontype_, )
supermod.UnitDefinitionType.subclass = UnitDefinitionTypeSub
# end class UnitDefinitionTypeSub


class AngleTypeSub(supermod.AngleType):
    def __init__(self, uom=None, valueOf_=None):
        super(AngleTypeSub, self).__init__(uom, valueOf_, )
supermod.AngleType.subclass = AngleTypeSub
# end class AngleTypeSub


class SpeedTypeSub(supermod.SpeedType):
    def __init__(self, uom=None, valueOf_=None):
        super(SpeedTypeSub, self).__init__(uom, valueOf_, )
supermod.SpeedType.subclass = SpeedTypeSub
# end class SpeedTypeSub


class VolumeTypeSub(supermod.VolumeType):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumeTypeSub, self).__init__(uom, valueOf_, )
supermod.VolumeType.subclass = VolumeTypeSub
# end class VolumeTypeSub


class AreaTypeSub(supermod.AreaType):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaTypeSub, self).__init__(uom, valueOf_, )
supermod.AreaType.subclass = AreaTypeSub
# end class AreaTypeSub


class GridLengthTypeSub(supermod.GridLengthType):
    def __init__(self, uom=None, valueOf_=None):
        super(GridLengthTypeSub, self).__init__(uom, valueOf_, )
supermod.GridLengthType.subclass = GridLengthTypeSub
# end class GridLengthTypeSub


class TimeTypeSub(supermod.TimeType):
    def __init__(self, uom=None, valueOf_=None):
        super(TimeTypeSub, self).__init__(uom, valueOf_, )
supermod.TimeType.subclass = TimeTypeSub
# end class TimeTypeSub


class ScaleTypeSub(supermod.ScaleType):
    def __init__(self, uom=None, valueOf_=None):
        super(ScaleTypeSub, self).__init__(uom, valueOf_, )
supermod.ScaleType.subclass = ScaleTypeSub
# end class ScaleTypeSub


class LengthTypeSub(supermod.LengthType):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthTypeSub, self).__init__(uom, valueOf_, )
supermod.LengthType.subclass = LengthTypeSub
# end class LengthTypeSub


class AbstractGeometryTypeSub(supermod.AbstractGeometryType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, extensiontype_=None):
        super(AbstractGeometryTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, extensiontype_, )
supermod.AbstractGeometryType.subclass = AbstractGeometryTypeSub
# end class AbstractGeometryTypeSub


class AbstractTimeSliceTypeSub(supermod.AbstractTimeSliceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, validTime=None, dataSource=None, extensiontype_=None):
        super(AbstractTimeSliceTypeSub, self).__init__(id, metaDataProperty, description, name, validTime, dataSource, extensiontype_, )
supermod.AbstractTimeSliceType.subclass = AbstractTimeSliceTypeSub
# end class AbstractTimeSliceTypeSub


class EnvelopeWithTimePeriodTypeSub(supermod.EnvelopeWithTimePeriodType):
    def __init__(self, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, lowerCorner=None, upperCorner=None, coord=None, pos=None, coordinates=None, frame='#ISO-8601', timePosition=None):
        super(EnvelopeWithTimePeriodTypeSub, self).__init__(srsName, srsDimension, axisLabels, uomLabels, lowerCorner, upperCorner, coord, pos, coordinates, frame, timePosition, )
supermod.EnvelopeWithTimePeriodType.subclass = EnvelopeWithTimePeriodTypeSub
# end class EnvelopeWithTimePeriodTypeSub


class AbstractFeatureTypeSub(supermod.AbstractFeatureType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, extensiontype_=None):
        super(AbstractFeatureTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, extensiontype_, )
supermod.AbstractFeatureType.subclass = AbstractFeatureTypeSub
# end class AbstractFeatureTypeSub


class ObservationTypeSub(supermod.ObservationType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, validTime=None, using=None, target=None, resultOf=None, extensiontype_=None):
        super(ObservationTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, validTime, using, target, resultOf, extensiontype_, )
supermod.ObservationType.subclass = ObservationTypeSub
# end class ObservationTypeSub


class DerivedCRSTypeSub(supermod.DerivedCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, baseCRS=None, definedByConversion=None, derivedCRSType=None, usesCS=None):
        super(DerivedCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, baseCRS, definedByConversion, derivedCRSType, usesCS, )
supermod.DerivedCRSType.subclass = DerivedCRSTypeSub
# end class DerivedCRSTypeSub


class ProjectedCRSTypeSub(supermod.ProjectedCRSType):
    def __init__(self, id=None, metaDataProperty=None, srsName=None, srsID=None, remarks=None, validArea=None, scope=None, baseCRS=None, definedByConversion=None, usesCartesianCS=None):
        super(ProjectedCRSTypeSub, self).__init__(id, metaDataProperty, srsName, srsID, remarks, validArea, scope, baseCRS, definedByConversion, usesCartesianCS, )
supermod.ProjectedCRSType.subclass = ProjectedCRSTypeSub
# end class ProjectedCRSTypeSub


class GridTypeSub(supermod.GridType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, dimension=None, limits=None, axisName=None, extensiontype_=None):
        super(GridTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, dimension, limits, axisName, extensiontype_, )
supermod.GridType.subclass = GridTypeSub
# end class GridTypeSub


class AbstractCoverageTypeSub(supermod.AbstractCoverageType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, dimension=None, domainSet=None, rangeSet=None, extensiontype_=None):
        super(AbstractCoverageTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, dimension, domainSet, rangeSet, extensiontype_, )
supermod.AbstractCoverageType.subclass = AbstractCoverageTypeSub
# end class AbstractCoverageTypeSub


class AbstractRingTypeSub(supermod.AbstractRingType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, extensiontype_=None):
        super(AbstractRingTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, extensiontype_, )
supermod.AbstractRingType.subclass = AbstractRingTypeSub
# end class AbstractRingTypeSub


class RingTypeSub(supermod.RingType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, curveMember=None):
        super(RingTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, curveMember, )
supermod.RingType.subclass = RingTypeSub
# end class RingTypeSub


class AbstractGeometricAggregateTypeSub(supermod.AbstractGeometricAggregateType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, extensiontype_=None):
        super(AbstractGeometricAggregateTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, extensiontype_, )
supermod.AbstractGeometricAggregateType.subclass = AbstractGeometricAggregateTypeSub
# end class AbstractGeometricAggregateTypeSub


class GeometricComplexTypeSub(supermod.GeometricComplexType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, element=None):
        super(GeometricComplexTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, element, )
supermod.GeometricComplexType.subclass = GeometricComplexTypeSub
# end class GeometricComplexTypeSub


class ConventionalUnitTypeSub(supermod.ConventionalUnitType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, quantityType=None, catalogSymbol=None, conversionToPreferredUnit=None, roughConversionToPreferredUnit=None, derivationUnitTerm=None):
        super(ConventionalUnitTypeSub, self).__init__(id, metaDataProperty, description, name, quantityType, catalogSymbol, conversionToPreferredUnit, roughConversionToPreferredUnit, derivationUnitTerm, )
supermod.ConventionalUnitType.subclass = ConventionalUnitTypeSub
# end class ConventionalUnitTypeSub


class DerivedUnitTypeSub(supermod.DerivedUnitType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, quantityType=None, catalogSymbol=None, derivationUnitTerm=None):
        super(DerivedUnitTypeSub, self).__init__(id, metaDataProperty, description, name, quantityType, catalogSymbol, derivationUnitTerm, )
supermod.DerivedUnitType.subclass = DerivedUnitTypeSub
# end class DerivedUnitTypeSub


class BaseUnitTypeSub(supermod.BaseUnitType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, quantityType=None, catalogSymbol=None, unitsSystem=None):
        super(BaseUnitTypeSub, self).__init__(id, metaDataProperty, description, name, quantityType, catalogSymbol, unitsSystem, )
supermod.BaseUnitType.subclass = BaseUnitTypeSub
# end class BaseUnitTypeSub


class AbstractGeometricPrimitiveTypeSub(supermod.AbstractGeometricPrimitiveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, extensiontype_=None):
        super(AbstractGeometricPrimitiveTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, extensiontype_, )
supermod.AbstractGeometricPrimitiveType.subclass = AbstractGeometricPrimitiveTypeSub
# end class AbstractGeometricPrimitiveTypeSub


class DynamicFeatureTypeSub(supermod.DynamicFeatureType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, validTime=None, history=None, dataSource=None):
        super(DynamicFeatureTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, validTime, history, dataSource, )
supermod.DynamicFeatureType.subclass = DynamicFeatureTypeSub
# end class DynamicFeatureTypeSub


class MovingObjectStatusTypeSub(supermod.MovingObjectStatusType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, validTime=None, dataSource=None, location=None, speed=None, bearing=None, acceleration=None, elevation=None, status=None):
        super(MovingObjectStatusTypeSub, self).__init__(id, metaDataProperty, description, name, validTime, dataSource, location, speed, bearing, acceleration, elevation, status, )
supermod.MovingObjectStatusType.subclass = MovingObjectStatusTypeSub
# end class MovingObjectStatusTypeSub


class AbstractFeatureCollectionTypeSub(supermod.AbstractFeatureCollectionType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, featureMember=None, featureMembers=None, extensiontype_=None):
        super(AbstractFeatureCollectionTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, featureMember, featureMembers, extensiontype_, )
supermod.AbstractFeatureCollectionType.subclass = AbstractFeatureCollectionTypeSub
# end class AbstractFeatureCollectionTypeSub


class FeatureCollectionTypeSub(supermod.FeatureCollectionType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, featureMember=None, featureMembers=None, lockId=None, timeStamp=None, numberOfFeatures=None, extensiontype_=None):
        super(FeatureCollectionTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, featureMember, featureMembers, lockId, timeStamp, numberOfFeatures, extensiontype_, )
supermod.FeatureCollectionType.subclass = FeatureCollectionTypeSub
# end class FeatureCollectionTypeSub


class DirectedObservationTypeSub(supermod.DirectedObservationType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, validTime=None, using=None, target=None, resultOf=None, direction=None, extensiontype_=None):
        super(DirectedObservationTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, validTime, using, target, resultOf, direction, extensiontype_, )
supermod.DirectedObservationType.subclass = DirectedObservationTypeSub
# end class DirectedObservationTypeSub


class RectifiedGridTypeSub(supermod.RectifiedGridType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, dimension=None, limits=None, axisName=None, origin=None, offsetVector=None):
        super(RectifiedGridTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, dimension, limits, axisName, origin, offsetVector, )
supermod.RectifiedGridType.subclass = RectifiedGridTypeSub
# end class RectifiedGridTypeSub


class AbstractDiscreteCoverageTypeSub(supermod.AbstractDiscreteCoverageType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, dimension=None, domainSet=None, rangeSet=None, coverageFunction=None):
        super(AbstractDiscreteCoverageTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, dimension, domainSet, rangeSet, coverageFunction, )
supermod.AbstractDiscreteCoverageType.subclass = AbstractDiscreteCoverageTypeSub
# end class AbstractDiscreteCoverageTypeSub


class AbstractContinuousCoverageTypeSub(supermod.AbstractContinuousCoverageType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, dimension=None, domainSet=None, rangeSet=None, coverageFunction=None):
        super(AbstractContinuousCoverageTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, dimension, domainSet, rangeSet, coverageFunction, )
supermod.AbstractContinuousCoverageType.subclass = AbstractContinuousCoverageTypeSub
# end class AbstractContinuousCoverageTypeSub


class LinearRingTypeSub(supermod.LinearRingType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, pos=None, pointProperty=None, pointRep=None, posList=None, coordinates=None, coord=None):
        super(LinearRingTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, pos, pointProperty, pointRep, posList, coordinates, coord, )
supermod.LinearRingType.subclass = LinearRingTypeSub
# end class LinearRingTypeSub


class AbstractSurfaceTypeSub(supermod.AbstractSurfaceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, extensiontype_=None):
        super(AbstractSurfaceTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, extensiontype_, )
supermod.AbstractSurfaceType.subclass = AbstractSurfaceTypeSub
# end class AbstractSurfaceTypeSub


class AbstractSolidTypeSub(supermod.AbstractSolidType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, extensiontype_=None):
        super(AbstractSolidTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, extensiontype_, )
supermod.AbstractSolidType.subclass = AbstractSolidTypeSub
# end class AbstractSolidTypeSub


class OrientableSurfaceTypeSub(supermod.OrientableSurfaceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, orientation='+', baseSurface=None):
        super(OrientableSurfaceTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, orientation, baseSurface, )
supermod.OrientableSurfaceType.subclass = OrientableSurfaceTypeSub
# end class OrientableSurfaceTypeSub


class SurfaceTypeSub(supermod.SurfaceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, patches=None):
        super(SurfaceTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, patches, )
supermod.SurfaceType.subclass = SurfaceTypeSub
# end class SurfaceTypeSub


class MultiPolygonTypeSub(supermod.MultiPolygonType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, polygonMember=None):
        super(MultiPolygonTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, polygonMember, )
supermod.MultiPolygonType.subclass = MultiPolygonTypeSub
# end class MultiPolygonTypeSub


class MultiLineStringTypeSub(supermod.MultiLineStringType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, lineStringMember=None):
        super(MultiLineStringTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, lineStringMember, )
supermod.MultiLineStringType.subclass = MultiLineStringTypeSub
# end class MultiLineStringTypeSub


class MultiSolidTypeSub(supermod.MultiSolidType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, solidMember=None, solidMembers=None):
        super(MultiSolidTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, solidMember, solidMembers, )
supermod.MultiSolidType.subclass = MultiSolidTypeSub
# end class MultiSolidTypeSub


class MultiSurfaceTypeSub(supermod.MultiSurfaceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, surfaceMember=None, surfaceMembers=None):
        super(MultiSurfaceTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, surfaceMember, surfaceMembers, )
supermod.MultiSurfaceType.subclass = MultiSurfaceTypeSub
# end class MultiSurfaceTypeSub


class MultiCurveTypeSub(supermod.MultiCurveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, curveMember=None, curveMembers=None):
        super(MultiCurveTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, curveMember, curveMembers, )
supermod.MultiCurveType.subclass = MultiCurveTypeSub
# end class MultiCurveTypeSub


class MultiPointTypeSub(supermod.MultiPointType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, pointMember=None, pointMembers=None):
        super(MultiPointTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, pointMember, pointMembers, )
supermod.MultiPointType.subclass = MultiPointTypeSub
# end class MultiPointTypeSub


class MultiGeometryTypeSub(supermod.MultiGeometryType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, geometryMember=None, geometryMembers=None):
        super(MultiGeometryTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, geometryMember, geometryMembers, )
supermod.MultiGeometryType.subclass = MultiGeometryTypeSub
# end class MultiGeometryTypeSub


class CompositeSolidTypeSub(supermod.CompositeSolidType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, solidMember=None):
        super(CompositeSolidTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, solidMember, )
supermod.CompositeSolidType.subclass = CompositeSolidTypeSub
# end class CompositeSolidTypeSub


class CompositeSurfaceTypeSub(supermod.CompositeSurfaceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, surfaceMember=None):
        super(CompositeSurfaceTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, surfaceMember, )
supermod.CompositeSurfaceType.subclass = CompositeSurfaceTypeSub
# end class CompositeSurfaceTypeSub


class AbstractCurveTypeSub(supermod.AbstractCurveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, extensiontype_=None):
        super(AbstractCurveTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, extensiontype_, )
supermod.AbstractCurveType.subclass = AbstractCurveTypeSub
# end class AbstractCurveTypeSub


class PointTypeSub(supermod.PointType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, pos=None, coordinates=None, coord=None):
        super(PointTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, pos, coordinates, coord, )
supermod.PointType.subclass = PointTypeSub
# end class PointTypeSub


class DynamicFeatureCollectionTypeSub(supermod.DynamicFeatureCollectionType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, featureMember=None, featureMembers=None, lockId=None, timeStamp=None, numberOfFeatures=None, validTime=None, history=None, dataSource=None):
        super(DynamicFeatureCollectionTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, featureMember, featureMembers, lockId, timeStamp, numberOfFeatures, validTime, history, dataSource, )
supermod.DynamicFeatureCollectionType.subclass = DynamicFeatureCollectionTypeSub
# end class DynamicFeatureCollectionTypeSub


class DirectedObservationAtDistanceTypeSub(supermod.DirectedObservationAtDistanceType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, boundedBy=None, location=None, validTime=None, using=None, target=None, resultOf=None, direction=None, distance=None):
        super(DirectedObservationAtDistanceTypeSub, self).__init__(id, metaDataProperty, description, name, boundedBy, location, validTime, using, target, resultOf, direction, distance, )
supermod.DirectedObservationAtDistanceType.subclass = DirectedObservationAtDistanceTypeSub
# end class DirectedObservationAtDistanceTypeSub


class PolygonTypeSub(supermod.PolygonType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, exterior=None, interior=None):
        super(PolygonTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, exterior, interior, )
supermod.PolygonType.subclass = PolygonTypeSub
# end class PolygonTypeSub


class SolidTypeSub(supermod.SolidType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, exterior=None, interior=None):
        super(SolidTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, exterior, interior, )
supermod.SolidType.subclass = SolidTypeSub
# end class SolidTypeSub


class OrientableCurveTypeSub(supermod.OrientableCurveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, orientation='+', baseCurve=None):
        super(OrientableCurveTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, orientation, baseCurve, )
supermod.OrientableCurveType.subclass = OrientableCurveTypeSub
# end class OrientableCurveTypeSub


class CurveTypeSub(supermod.CurveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, segments=None):
        super(CurveTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, segments, )
supermod.CurveType.subclass = CurveTypeSub
# end class CurveTypeSub


class CompositeCurveTypeSub(supermod.CompositeCurveType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, curveMember=None):
        super(CompositeCurveTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, curveMember, )
supermod.CompositeCurveType.subclass = CompositeCurveTypeSub
# end class CompositeCurveTypeSub


class LineStringTypeSub(supermod.LineStringType):
    def __init__(self, id=None, metaDataProperty=None, description=None, name=None, gid=None, srsName=None, srsDimension=None, axisLabels=None, uomLabels=None, pos=None, pointProperty=None, pointRep=None, coord=None, posList=None, coordinates=None):
        super(LineStringTypeSub, self).__init__(id, metaDataProperty, description, name, gid, srsName, srsDimension, axisLabels, uomLabels, pos, pointProperty, pointRep, coord, posList, coordinates, )
supermod.LineStringType.subclass = LineStringTypeSub
# end class LineStringTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DescribeLayerResponseType'
        rootClass = supermod.DescribeLayerResponseType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:sld="http://www.opengis.net/sld"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DescribeLayerResponseType'
        rootClass = supermod.DescribeLayerResponseType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DescribeLayerResponseType'
        rootClass = supermod.DescribeLayerResponseType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:sld="http://www.opengis.net/sld"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DescribeLayerResponseType'
        rootClass = supermod.DescribeLayerResponseType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
