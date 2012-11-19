""" Edit map view module
"""
from zope.formlib.form import Fields
from eea.exhibit.views.map.interfaces import IExhibitMapEdit
from eea.app.visualization.views.edit import EditForm

class Edit(EditForm):
    """ Edit map view
    """
    label = u"Map view settings"
    form_fields = Fields(IExhibitMapEdit)
    previewname = "daviz.map.preview.png"
