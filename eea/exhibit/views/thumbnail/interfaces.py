""" Views exhibit thumbnail interfaces
"""
from zope import schema
from zope.interface import Interface
from eea.app.visualization.views.interfaces import IVisualizationView

class IExhibitThumbnailView(IVisualizationView):
    """ Exhibit thumbnail view
    """

class IExhibitThumbnailEdit(Interface):
    """ Exhibit thumbnail edit
    """
    thumbnail = schema.Choice(
        title=u'Thumbnail',
        description=u"Specify which column should be used to get " \
                                                    "thumbnail url.",
        required=True,
        vocabulary="eea.daviz.vocabularies.FacetsVocabulary"
    )

    columns = schema.List(
        title=u'Columns',
        description=u'Select columns to be shown under thumbnail',
        required=False,
        value_type=schema.Choice(
            vocabulary="eea.daviz.vocabularies.FacetsVocabulary")
    )
