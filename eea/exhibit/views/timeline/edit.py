""" Edit timeline view module
"""
from zope.formlib.form import Fields
from eea.exhibit.views.timeline.interfaces import IExhibitTimelineEdit
from eea.app.visualization.views.edit import EditForm

class Edit(EditForm):
    """ Edit timeline view
    """
    label = u"Timeline view settings"
    form_fields = Fields(IExhibitTimelineEdit)
    previewname = "daviz.timeline.preview.png"
