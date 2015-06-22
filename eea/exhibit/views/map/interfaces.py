""" Exhibit map view interfaces
"""
from zope import schema
from zope.interface import Interface
from eea.app.visualization.views.interfaces import IVisualizationView
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from eea.exhibit import EEAMessageFactory as _

class IExhibitMapView(IVisualizationView):
    """ Exhibit map view
    """

class IExhibitMapEdit(Interface):
    """ Exhibit map edit
    """
    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Friendly name for this visualization"),
        default=u"Map View",
        required=True,
    )

    latlng = schema.Choice(
        title=_(u"Latitude and Longitude column"),
        description=_(u"Specify which column should be used to get latitude "
                      "and longitude. If there are separate columns for "
                      "latitude and longitude, use settings bellow."),
        required=False,
        vocabulary="eea.daviz.vocabularies.FacetsVocabulary"
    )

    lat = schema.Choice(
        title=_(u"Latitude column"),
        description=_(u"Specify which column should be used to get latitude"),
        required=False,
        vocabulary="eea.daviz.vocabularies.FacetsVocabulary"
    )

    lng = schema.Choice(
        title=_(u"Longitude column"),
        description=_(u"Specify which column should be used to get longitude"),
        required=False,
        vocabulary="eea.daviz.vocabularies.FacetsVocabulary"
    )

    lens = schema.Text(
        title=_(u"Lens template"),
        description=_(u""
            "Edit custom exhibit lens. Leave it blank to use the default one. "
            "See more details "
            "http://www.simile-widgets.org/wiki/Exhibit/Lens_Templates"),
        required=False
    )
    #
    # Advanced options
    #
    ex_center = schema.TextLine(
        title=_(u"Center"),
        description=_(
            u"latitude/longitude where the map centers at the beginning"),
        required=False,
        default=u"20,0"
    )
    ex_zoom = schema.Float(
        title=_(u"Zoom"),
        description=_(u"zoom level"),
        required=False,
        default=2.0
    )
    ex_size = schema.TextLine(
        title=_(u"Size"),
        description=_(u"size of map controls"),
        required=False,
        default=u"small"
    )
    ex_scaleControl = schema.Bool(
        title=_(u"Scale control"),
        description=_(u"whether to show the map scale control"),
        required=False,
        default=True
    )
    ex_overviewControl = schema.Bool(
        title=_(u"Overview control"),
        description=_(u"whether to show the map overview control"),
        required=False,
        default=False
    )

    ex_type = schema.Choice(
        title=_(u"Type"),
        description=_(u"the type of map"),
        required=False,
        default=u"normal",
        vocabulary=SimpleVocabulary([
            SimpleTerm(u"normal", u"normal", u"Normal"),
            SimpleTerm(u"satellite", u"satellite", u"Satellite"),
            SimpleTerm(u"hybrid", u"hybrid", u"Hybrid"),
        ])
    )

    ex_bubbleTip = schema.Choice(
        title=_(u"Bubble tip"),
        description=_(u""
                     "whether the map bubble points at the top or at the bottom"
                     " of map markers"),
        required=False,
        default=u"top",
        vocabulary=SimpleVocabulary([
            SimpleTerm(u"top", u"top", u"Top"),
            SimpleTerm(u"bottom", u"bottom", u"Bottom"),
        ])
    )

    ex_mapHeight = schema.Int(
        title=_(u"Map height"),
        description=_(u"the map's height in pixels"),
        required=False,
        default=450,
    )

    ex_mapConstructor = schema.TextLine(
        title=_(u"Map constructor"),
        description=_(u"a custom map constructor"),
        required=False,
        default=u"",
    )

    ex_color = schema.TextLine(
        title=_(u"Color"),
        description=_(u"default color for map marker"),
        required=False,
        default=u"#FF9000"
    )

    ex_colorKey = schema.TextLine(
        title=_(u"Color key"),
        description=_(u"expression for getting the keys used to color-code "
                     "the map markers"),
        required=False,
        default=u""
    )

    ex_colorCoder = schema.TextLine(
        title=_(u"Color coder"),
        description=_(u"id of a color coder"),
        required=False,
        default=u""
    )

    ex_sizeKey = schema.TextLine(
        title=_(u"Size key"),
        description=_(u"expression for getting the keys used to size-code "
                     "the map markers"),
        required=False,
        default=u""
    )

    ex_sizeCoder = schema.TextLine(
        title=_(u"Size coder"),
        description=_(u"id of a size coder"),
        required=False,
        default=u""
    )

    ex_iconKey = schema.TextLine(
        title=_(u"Icon key"),
        description=_(u"expression for getting the keys used to add icons "
                     "the map markers"),
        required=False,
        default=u""
    )

    ex_iconCoder = schema.TextLine(
        title=_(u"Icon coder"),
        description=_(u"id of an icon coder"),
        required=False,
        default=u""
    )

    ex_selectCoordinator = schema.TextLine(
        title=_(u"Select coordinator"),
        description=_(u"id of a coordinator"),
        required=False,
        default=u""
    )

    ex_iconSize = schema.Int(
        title=_(u"Icon size"),
        description=_(u"icon size"),
        required=False,
        default=0
    )

    ex_iconFit = schema.Choice(
        title=_(u"Icon fit"),
        description=_(u"how to fit icon images into map markers"),
        required=False,
        default=u"smaller",
        vocabulary=SimpleVocabulary([
            SimpleTerm(u"smaller", u"smaller", u"Smaller"),
            SimpleTerm(u"larger", u"larger", u"Larger"),
            SimpleTerm(u"none", u"none", u"None"),
            SimpleTerm(u"both", u"both", u"Both"),
        ])
    )

    ex_iconScale = schema.Float(
        title=_(u"Icon scale"),
        description=_(u"scaling adjustment to icon images after fitting them"),
        required=False,
        default=1.0
    )

    ex_iconOffsetX = schema.Float(
        title=_(u"Icon offset X"),
        description=_(u"translational adjustment to icon images (in pixels)"),
        required=False,
        default=0.0
    )

    ex_iconOffsetY = schema.Float(
        title=_(u"Icon offset Y"),
        description=_(u"translational adjustment to icon images (in pixels)"),
        required=False,
        default=0.0
    )

    ex_shape = schema.TextLine(
        title=_(u"Shape"),
        description=_(u"shape of map markers"),
        required=False,
        default=u"circle"
    )

    ex_shapeWidth = schema.Int(
        title=_(u"Shape width"),
        description=_(u"width of shape of map markers (in pixels)"),
        required=False,
        default=24
    )

    ex_shapeHeight = schema.Int(
        title=_(u"Shape height"),
        description=_(u"height of shape of map markers (in pixels)"),
        required=False,
        default=24
    )

    ex_shapeAlpha = schema.Float(
        title=_(u"Shape alpha"),
        description=_(u"alpha of shape of map markers"),
        required=False,
        default=0.7
    )

    ex_pin = schema.Bool(
        title=_(u"Pin"),
        description=_(u"whether map markers have pins"),
        required=False,
        default=True
    )

    ex_pinHeight = schema.Int(
        title=_(u"Pin height"),
        description=_(u"height of pins of map markers (in pixels)"),
        required=False,
        default=6
    )

    ex_pinWidth = schema.Int(
        title=_(u"Pin width"),
        description=_(u"width of pins of map markers (in pixels)"),
        required=False,
        default=6
    )

    ex_borderOpacity = schema.Float(
        title=_(u"Border Opacity"),
        description=_(u"when drawing polygons or polylines, the default "
                      "opacity of the border or line"),
        required=False,
        default=0.5
    )

    ex_borderWidth = schema.Int(
        title=_(u"Border width"),
        description=_(u"when drawing polygons or polylines, the default "
                      "width of the border or line"),
        required=False,
        default=1
    )

    ex_borderColor = schema.TextLine(
        title=_(u"Border color"),
        description=_(u"when drawing polygons or polylines, the default "
                      "color of the border"),
        required=False,
        default=u""
    )

    ex_opacity = schema.Float(
        title=_(u"Opacity"),
        description=_(u"opacity"),
        required=False,
        default=0.7
    )

    ex_sizeLegendLabel = schema.TextLine(
        title=_(u"Legend label"),
        description=_(u"legend label"),
        required=False,
        default=u""
    )

    ex_colorLegendLabel = schema.TextLine(
        title=_(u"Color legend label"),
        description=_(u"color of the legend's label"),
        required=False,
        default=u""
    )

    ex_iconLegendLabel = schema.TextLine(
        title=_(u"Icon legend label"),
        description=_(u"Icon of the legend's label"),
        required=False,
        default=u""
    )

    ex_markerScale = schema.TextLine(
        title=_(u"Marker scale"),
        description=_(u"marker scale"),
        required=False,
        default=u""
    )

    ex_showHeader = schema.Bool(
        title=_(u"Show header"),
        description=_(u"whether or not to show the header of the view"),
        required=False,
        default=True
    )

    ex_showSummary = schema.Bool(
        title=_(u"Show summary"),
        description=_(u"whether or not to show the summary "
                      "information of the view"),
        required=False,
        default=True
    )

    ex_showFooter = schema.Bool(
        title=_(u"Show footer"),
        description=_(u"whether or not to show the footer of the view"),
        required=False,
        default=True
    )

    ex_proxy = schema.TextLine(
        title=_(u"Proxy"),
        description=_(
            u"expression for getting an item containing a latitude "
            "an longitude (specified by ex:lat and ex:long expressions). "
            "Needed in the complex case where an item needs to be plotted in "
            "multiple locations and you need to be clear which latitude goes "
            "with which longitude."),
        required=False,
        default=u""
    )

    ex_latlngOrder = schema.Choice(
        title=_(u"Lat lng order"),
        description=_(u"whether the data is provided in the form of "
                      "(latitude, longitude) or the reverse"),
        required=False,
        default=u"latlng",
        vocabulary=SimpleVocabulary([
            SimpleTerm(u"latlng", u"latlng", u"(latitude, longitude)"),
            SimpleTerm(u"lnglat", u"lnglat", u"(longitude, latitude)"),
        ])
    )

    ex_latlngPairSeparator = schema.TextLine(
        title=_(u"Lat lng pair separator"),
        description=_(u"character used to separate location "
                      "pairs in a line or polygon"),
        required=False,
        default=u";"
    )

    ex_showToolbox = schema.Bool(
        title=_(u"Show toolbox"),
        description=_(u"whether to show the toolbox"),
        required=False,
        default=False
    )
