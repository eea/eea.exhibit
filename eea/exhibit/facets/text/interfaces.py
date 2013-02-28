""" Interfaces
"""
from zope import schema
from eea.app.visualization.facets.interfaces import IVisualizationEditFacet
from eea.app.visualization.config import EEAMessageFactory as _

class ITextProperties(IVisualizationEditFacet):
    """ Edit facet
    """
    ex_queryParamName = schema.TextLine(
        title=_(u"Query param name"),
        description=_(u"query param name"),
        required=False,
        default=u""
    )

    ex_requiresEnter = schema.Bool(
        title=_(u"Requires Enter"),
        description=_(u"requires enter"),
        required=False,
        default=False
    )
