""" Interfaces
"""
from zope import schema
from eea.app.visualization.facets.interfaces import IVisualizationEditFacet
from eea.app.visualization.config import EEAMessageFactory as _

class ISliderProperties(IVisualizationEditFacet):
    """ Edit facet
    """
    ex_scroll = schema.Bool(
        title=_(u"Scroll"),
        description=_(u"if true, facet values are in a scrollable window "
                      "of fixed size. If false, all facet values are shown "
                      "in as much space as needed, without a scroll bar."),
        required=False,
        default=True
    )

    ex_height = schema.TextLine(
        title=_(u"Height"),
        description=_(u"height of the facet's body, e.g., '20em', '200px'"),
        required=False,
        default=u""
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
