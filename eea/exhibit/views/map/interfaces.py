""" Exhibit map view interfaces
"""
from zope import schema
from zope.interface import Interface
from eea.app.visualization.views.interfaces import IVisualizationView

class IExhibitMapView(IVisualizationView):
    """ Exhibit map view
    """

class IExhibitMapEdit(Interface):
    """ Exhibit map edit
    """
    latlng = schema.Choice(
        title=u'Latitude and Longitude column',
        description=u"Specify which column should be used to get latitude " \
                                                            "and longitude.",
        required=False,
        vocabulary="eea.daviz.vocabularies.FacetsVocabulary"
    )
