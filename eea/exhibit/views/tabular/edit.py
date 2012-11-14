""" Edit tabular views
"""
from zope.formlib.form import Fields
from eea.exhibit.views.tabular.interfaces import IExhibitTabularEdit
from eea.app.visualization.views.edit import EditForm

class Edit(EditForm):
    """ Edit tabular view
    """
    label = u"Tabular view settings"
    form_fields = Fields(IExhibitTabularEdit)
    previewname = "daviz.tabular.preview.png"
