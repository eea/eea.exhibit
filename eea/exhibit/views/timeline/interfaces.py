""" Views exhibit timeline interfaces
"""
from zope import schema
from zope.interface import Interface
from eea.app.visualization.views.interfaces import IVisualizationView

class IExhibitTimelineView(IVisualizationView):
    """ Exhibit timeline view
    """

class IExhibitTimelineEdit(Interface):
    """ Exhibit timeline edit
    """
    start = schema.Choice(
        title=u'Start date',
        description=u"Specify date or starting date",
        required=False,
        vocabulary="eea.daviz.vocabularies.FacetsVocabulary"
    )

    end = schema.Choice(
        title=u'End date',
        description=u"Specify end date if it is the case",
        required=False,
        vocabulary="eea.daviz.vocabularies.FacetsVocabulary"
    )
