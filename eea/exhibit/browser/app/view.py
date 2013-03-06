""" Browser views
"""
from zope.component import queryAdapter
from Products.Five.browser import BrowserView
from eea.app.visualization.interfaces import IVisualizationConfig


class View(BrowserView):
    """ Custom header
    """
    def __init__(self, context, request):
        super(View, self).__init__(context, request)
        self._accessor = None

    @property
    def accessor(self):
        """ Get config
        """
        if not self._accessor:
            self._accessor = queryAdapter(self.context, IVisualizationConfig)
        return self._accessor

    @property
    def sources(self):
        """ External sources
        """
        sources = self.accessor.sources
        for source in sources:
            yield source
