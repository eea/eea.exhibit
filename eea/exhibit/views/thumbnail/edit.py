""" Edit thumbnail views
"""
from zope.formlib.form import Fields
from eea.exhibit.views.thumbnail.interfaces import IExhibitThumbnailEdit
from eea.app.visualization.views.edit import EditForm

class Edit(EditForm):
    """ Edit thumbnail view
    """
    label = u"Thumbnail view settings"
    form_fields = Fields(IExhibitThumbnailEdit)
