""" Interfaces
"""
from zope import schema
from eea.app.visualization.facets.interfaces import IVisualizationEditFacet
from eea.app.visualization.config import EEAMessageFactory as _

class ICloudProperties(IVisualizationEditFacet):
    """ Edit facet
    """
    ex_height = schema.TextLine(
        title=_(u"Height"),
        description=_(u"height of the facet's body, e.g., '20em', '200px'"),
        required=False,
        default=u""
    )

    ex_showMissing = schema.Bool(
        title=_(u"Show missing"),
        description=_(u"whether to provide a selection for items missing "
                      "the facet -- this will suppress the "
                      "'(missing this field)' text"),
        required=False,
        default=True
    )

    ex_missingLabel = schema.TextLine(
        title=_(u"Missing label"),
        description=_(u"missing label"),
        required=False,
        default=u""
    )

    ex_minimumCount = schema.Int(
        title=_("Minimum count"),
        description=_(u"minimum count"),
        required=False,
        default=1
    )
