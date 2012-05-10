""" Thumbnail view map module
"""
from zope.interface import implements
from eea.exhibit.views.map.interfaces import IExhibitMapView
from eea.app.visualization.views.view import ViewForm

class View(ViewForm):
    """ Thumbnail view
    """
    label = 'Map View'
    implements(IExhibitMapView)

    @property
    def latlng(self):
        """ Return latitude longitude column
        """
        return self.data.get('latlng', '')

    @property
    def lens(self):
        """ View custom lens
        """
        return self.data.get('lens', '')
