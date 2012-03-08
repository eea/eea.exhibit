""" Tiles view module
"""
from zope.interface import implements
from eea.app.visualization.views.view import ViewForm
from eea.exhibit.views.tile.interfaces import IExhibitTileView

class View(ViewForm):
    """ Tile view
    """
    label = 'Tile View'
    implements(IExhibitTileView)

    @property
    def lens(self):
        """ View custom lens
        """
        return self.data.get('lens', '')
