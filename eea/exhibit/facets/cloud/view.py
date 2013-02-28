""" Facet view module
"""
from eea.app.visualization.facets.view import ViewForm
from eea.exhibit.facets.cloud.interfaces import ICloudProperties

class View(ViewForm):
    """ View
    """
    facetType = u"Cloud"
    facetInterface = ICloudProperties
