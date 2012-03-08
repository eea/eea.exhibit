""" Views exhibit tile interfaces
"""
from zope import schema
from zope.interface import Interface
from eea.app.visualization.views.interfaces import IVisualizationView

class IExhibitTileView(IVisualizationView):
    """ Exhibit tile view
    """

class IExhibitTileEdit(Interface):
    """ Edit tile view
    """
    lens = schema.Text(
        title=u"Lens template",
        description=(u""
            "Edit custom exhibit lens. Leave it blank to use the default one. "
            "See more details "
            "http://www.simile-widgets.org/wiki/Exhibit/Lens_Templates"),
        required=False
    )
