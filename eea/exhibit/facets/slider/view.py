""" Facet view module
"""
from eea.app.visualization.facets.view import ViewForm
from eea.exhibit.facets.slider.interfaces import ISliderProperties

class View(ViewForm):
    """ View
    """
    facetType = u"Slider"
    facetInterface = ISliderProperties
