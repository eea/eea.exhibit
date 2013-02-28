""" Facet view module
"""
from eea.app.visualization.facets.view import ViewForm
from eea.exhibit.facets.numeric.interfaces import INumericProperties

class View(ViewForm):
    """ View
    """
    facetType = u"NumericRange"
    facetInterface = INumericProperties
