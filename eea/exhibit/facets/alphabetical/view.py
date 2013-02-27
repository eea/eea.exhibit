""" Facet view module
"""
from eea.app.visualization.facets.view import ViewForm
from eea.exhibit.facets.alphabetical.interfaces import IAlphabeticalProperties

class View(ViewForm):
    """ View
    """
    facetType = u"AlphaRange"
    facetInterface = IAlphabeticalProperties
