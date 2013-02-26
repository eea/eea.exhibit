""" Interfaces
"""
from zope import schema
from eea.app.visualization.facets.interfaces import IVisualizationEditFacet
from eea.app.visualization.config import EEAMessageFactory as _

class INumericProperties(IVisualizationEditFacet):
    """ Edit numeric facet
    """
    ex_height = schema.TextLine(
        title=_(u"Height"),
        description=_(u"height of the facet's body, e.g., '20em', '200px'"),
        required=False,
        default=u""
    )

    ex_interval = schema.Int(
        title=_(u'Interval'),
        description=_(u"The interval in number ranges"),
        required=True,
        default=10
    )

    ex_collapsible = schema.Bool(
        title=_(u"Collapsible"),
        description=_(u"Collapsible"),
        required=False,
        default=False
    )

    ex_collapsed = schema.Bool(
        title=_(u"Collapsed"),
        description=_(u"Collapsed"),
        required=False,
        default=False
    )
