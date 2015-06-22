""" Views exhibit tile interfaces
"""
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from eea.app.visualization.views.interfaces import IVisualizationView
from eea.exhibit import EEAMessageFactory as _

class IExhibitTileView(IVisualizationView):
    """ Exhibit tile view
    """

class IExhibitTileEdit(Interface):
    """ Edit tile view
    """
    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Friendly name for this visualization"),
        default=u"Tile View",
        required=True,
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
    ex_orders = schema.TextLine(
        title=_(u"Orders"),
        description=_(u"comma separated list of one or more expressions, "
                      "e.g., '.age, .job'"),
        required=False,
        default=u".label"
    )

    ex_directions = schema.Choice(
        title=_(u"Directions"),
        description=_(u"how to sort each of the expressions in the "
                      "'Orders' setting"),
        required=False,
        default=u"ascending",
        vocabulary=SimpleVocabulary([
            SimpleTerm(u"ascending", u"ascending", u"Ascending"),
            SimpleTerm(u"descending", u"descending", u"Descending"),
        ])
    )

    ex_possibleOrders = schema.TextLine(
        title=_(u"Possible orders"),
        description=_(u"comma separated list of other expressions "
                      "that the user can choose for sorting"),
        required=False,
        default=u""
    )

    ex_possibleDirections = schema.Choice(
        title=_(u"Possible directions"),
        description=_(u"how each of the expressions in the 'Possible orders' "
                      "setting should be sorted when the user picks it"),
        required=False,
        default=u"ascending",
        vocabulary=SimpleVocabulary([
            SimpleTerm(u"ascending", u"ascending", u"Ascending"),
            SimpleTerm(u"descending", u"descending", u"Descending"),
        ])
    )

    ex_showAll = schema.Bool(
        title=_(u"Show all"),
        description=_(u"whether to show all items (or just the first few); "
                      "this is forced to true if 'Grouped' is true and the "
                      "items can be grouped"),
        required=False,
        default=True
    )

    ex_grouped = schema.Bool(
        title=_(u"Grouped"),
        description=_(u"whether to show items in groups if they are 'equal'"
                      " in the current sorting order"),
        required=False,
        default=True
    )

    ex_showDuplicates = schema.Bool(
        title=_(u"Show duplicates"),
        description=_(u"hwhether to ide or show multiple copies of the same "
                      "item if it fits in multiple positions in the "
                      "sort/group order"),
        required=False,
        default=True
)

    ex_abbreviatedCount = schema.Int(
        title=_(u"Abbreviated Count"),
        description=_(u"how many items to show if 'Show all' is false"),
        required=False,
        default=10
    )

    ex_showHeader = schema.Bool(
        title=_(u"Show header"),
        description=_(u"hide or show the header"),
        required=False,
        default=True
    )

    ex_showSummary = schema.Bool(
        title=_(u"Show summary"),
        description=_(u"hide or show the # of results"),
        required=False,
        default=True
    )

    ex_showControls = schema.Bool(
        title=_(u"Show controls"),
        description=_(u"hide or show the controls"),
        required=False,
        default=True
    )

    ex_showFooter = schema.Bool(
        title=_(u"Show footer"),
        description=_(u"hide or show the Footer"),
        required=False,
        default=True
    )

    ex_paginate = schema.Bool(
        title=_(u"Paginate"),
        description=_(u"Group results into pages, that can be navigated"
                      " backward or forward"),
        required=False,
        default=False
    )

    ex_pageSize = schema.Int(
        title=_(u"Page size"),
        description=_(u"Number of results to show on each page, if "
                      "Paginate = true"),
        required=False,
        default=20
    )

    ex_pageWindow = schema.Int(
        title=_(u"Page window"),
        description=_(u"page window"),
        required=False,
        default=2
    )

    ex_page = schema.Int(
        title=_(u"Page"),
        description=_(u"page"),
        required=False,
        default=0
    )

    ex_alwaysShowPagingControls = schema.Bool(
        title=_(u"Always show paging controls"),
        description=_(u"show paging controls"),
        required=False,
        default=False
    )

    ex_pagingControlLocations = schema.Choice(
        title=_(u"Paging control locations"),
        description=_(u"location of page controls"),
        required=False,
        default=u"topbottom",
        vocabulary=SimpleVocabulary([
            SimpleTerm(u"top", u"top", u"Top"),
            SimpleTerm(u"bottom", u"bottom", u"Bottom"),
            SimpleTerm(u"topbottom", u"topbottom", u"Top and Bottom"),
        ])
    )

    ex_showToolbox = schema.Bool(
        title=_(u"Show toolbox"),
        description=_(u"whether to show the toolbox"),
        required=False,
        default=False
    )
