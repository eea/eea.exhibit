""" Facet view module
"""
from eea.app.visualization.facets.view import ViewForm
from eea.exhibit.facets.text.interfaces import ITextProperties

class View(ViewForm):
    """ View
    """
    facetType = u"TextSearch"
    facetInterface = ITextProperties
