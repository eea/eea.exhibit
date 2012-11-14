""" Edit
"""
from zope.formlib.form import Fields
from eea.exhibit.views.tile.interfaces import IExhibitTileEdit
from eea.app.visualization.views.edit import EditForm

class Edit(EditForm):
    """ Edit tabular view
    """
    label = u"Tile view settings"
    form_fields = Fields(IExhibitTileEdit)
    previewname = "daviz.tile.preview.png"
