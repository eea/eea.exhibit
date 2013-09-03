""" Tabular views interfaces
"""
from zope import schema
from zope.interface import Interface
from eea.app.visualization.views.interfaces import IVisualizationView
from eea.exhibit import EEAMessageFactory as _

class IExhibitTabularView(IVisualizationView):
    """ Exhibit tabular view
    """

class IExhibitTabularEdit(Interface):
    """ Exhibit tabular edit
    """
    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Friendly name for this visualization"),
        default=u"Tabular View",
        required=True,
    )

    columns = schema.List(
        title=_(u"Columns"),
        description=_(u"Select columns to be shown in table view"),
        required=False,
        unique=True,
        value_type=schema.Choice(
            vocabulary="eea.daviz.vocabularies.FacetsVocabulary")
    )
    details = schema.Bool(
        title=_(u"Display details column"),
        description=_(u"Select this if you want to display a column with "
                      "a 'more' link to item details"),
        required=False
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
    # Skip computed fields
    #
    #ex_columnLabels
    #ex_columnFormats

    #
    # Advanced options
    #
    ex_sortColumn = schema.Int(
        title=_(u"Sort column"),
        description=_(u"zero-based index of column to sort"),
        required=False,
        default=0
    )

    ex_sortAscending = schema.Bool(
        title=_(u"Sort ascending"),
        description=_(u"whether to sort ascending or descending"),
        required=False,
        default=True
    )

    ex_rowStyler = schema.TextLine(
        title=_(u"Row styler"),
        description=_(u"function that takes 3 arguments (item, database, tr) "
                      "and is called to style each row"),
        required=False,
        default=u"DavizTableRowStyler"
    )

    ex_tableStyler = schema.TextLine(
        title=_(u"Table styler"),
        description=_(u"function that takes 2 arguments (table, database) and "
                      "is called to style the table"),
        required=False,
        default=u"DavizTableStyler"
    )

    ex_border = schema.TextLine(
        title=_(u"Border"),
        description=_(u"whatever you would normally use to set the border of"
                      " a <table> element"),
        required=False,
        default=u"1"
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

    ex_cellSpacing = schema.Int(
        title=_(u"Cell spacing"),
        description=_(u"whatever you would normally use to set the cell "
                      "spacing of a <table> element"),
        required=False,
        default=0
    )

    ex_cellPadding = schema.Int(
        title=_(u"Cell padding"),
        description=_(u"whatever you would normally use to set the cell "
                      "padding of a <table> element"),
        required=False,
        default=0
    )

    ex_showToolbox = schema.Bool(
        title=_(u"Show toolbox"),
        description=_(u"whether to show the toolbox"),
        required=False,
        default=False
    )
