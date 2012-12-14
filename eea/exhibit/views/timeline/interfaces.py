""" Views exhibit timeline interfaces
"""
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from eea.app.visualization.views.interfaces import IVisualizationView
from eea.exhibit import EEAMessageFactory as _

UNITS = SimpleVocabulary([
    SimpleTerm(u"millisecond", u"millisecond", u"Millisecond"),
    SimpleTerm(u"second", u"second", u"Second"),
    SimpleTerm(u"minute", u"minute", u"Minute"),
    SimpleTerm(u"hour", u"hour", u"Hour"),
    SimpleTerm(u"day", u"day", u"Day"),
    SimpleTerm(u"week", u"week", u"Week"),
    SimpleTerm(u"month", u"month", u"Month"),
    SimpleTerm(u"year", u"year", u"Year"),
    SimpleTerm(u"decade", u"decade", u"Decade"),
    SimpleTerm(u"century", u"century", u"Century"),
    SimpleTerm(u"millennium", u"millennium", u"Millennium"),
])

class IExhibitTimelineView(IVisualizationView):
    """ Exhibit timeline view
    """

class IExhibitTimelineEdit(Interface):
    """ Exhibit timeline edit
    """
    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Friendly name for this visualization"),
        default=u"Timeline View",
        required=True,
    )

    start = schema.Choice(
        title=_(u'Start date'),
        description=_(u"Specify date or starting date"),
        required=False,
        vocabulary="eea.daviz.vocabularies.FacetsVocabulary"
    )
    end = schema.Choice(
        title=_(u'End date'),
        description=_(u"Specify end date if it is the case"),
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
    ex_timelineHeight = schema.Int(
        title=_(u"Timeline height"),
        description=_(u"height of the timeline in pixels"),
        required=False,
        default=400
    )

    ex_timelineConstructor = schema.TextLine(
        title=_(u"Timeline constructor"),
        description=_(u"custom constructor for the timeline"),
        required=False,
        default=u""
    )

    ex_colorKey = schema.TextLine(
        title=_(u"Color key"),
        description=_(u"expression for getting the keys used to "
                      "color-code the map markers"),
        required=False,
        default=u""
    )

    ex_colorCoder = schema.TextLine(
        title=_(u"Color coder"),
        description=_(u"id of a color coder"),
        required=False,
        default=u""
    )

    ex_iconKey = schema.TextLine(
        title=_(u"Icon key"),
        description=_(u"expression for getting the keys used to add "
                      "icons to immediate events"),
        required=False,
        default=u""
    )

    ex_iconCoder = schema.TextLine(
        title=_(u"Icon coder"),
        description=_(u"id of a icon coder"),
        required=False,
        default=u""
    )

    ex_selectCoordinator = schema.TextLine(
        title=_(u"Select coordinator"),
        description=_(u"id of a coordinator"),
        required=False,
        default=u""
    )

    ex_topBandHeight = schema.Int(
        title=_(u"Top band height"),
        description=_(u"percents that the top band takes up"),
        required=False,
        default=75
    )

    ex_topBandUnit = schema.Choice(
        title=_(u"Top band unit"),
        description=_(u"unit of the top band"),
        required=False,
        default=u"year",
        vocabulary=UNITS
    )

    ex_topBandPixelsPerUnit = schema.Int(
        title=_(u"Top band pixels per unit"),
        description=_(u"how wide each interval in the top band is (in pixels)"),
        required=False,
        default=200
    )

    ex_bottomBandHeight = schema.Int(
        title=_(u"Bottom band height"),
        description=_(u"percents that the bottom band takes up"),
        required=False,
        default=25
    )

    ex_bottomBandUnit = schema.Choice(
        title=_(u"Bottom band unit"),
        description=_(u"unit of the bottom band"),
        required=False,
        default=u"decade",
        vocabulary=UNITS
    )

    ex_bottomBandPixelsPerUnit = schema.Int(
        title=_(u"Bottom band pixels per unit"),
        description=_(u"how wide each interval in the bottom"
                      " band is (in pixels)"),
        required=False,
        default=200
    )

    ex_showHeader = schema.Bool(
        title=_(u"Show header"),
        description=_(u"whether or not to show the header of the view"),
        required=False,
        default=True
    )

    ex_showSummary = schema.Bool(
        title=_(u"Show summary"),
        description=_(u"whether or not to show the summary"
                      " information of the view"),
        required=False,
        default=True
    )

    ex_showFooter = schema.Bool(
        title=_(u"Show footer"),
        description=_(u"whether or not to show the footer of the view"),
        required=False,
        default=True
    )

    ex_showToolbox = schema.Bool(
        title=_(u"Show toolbox"),
        description=_(u"whether to show the toolbox"),
        required=False,
        default=False
    )
