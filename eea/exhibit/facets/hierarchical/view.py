""" Facet view module
"""
from eea.app.visualization.facets.view import ViewForm
from eea.exhibit.facets.hierarchical.interfaces import IHierarchicalProperties

class View(ViewForm):
    """ View
    """
    facetType = u"Hierarchical"
    facetInterface = IHierarchicalProperties
