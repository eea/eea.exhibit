""" Browser views
"""
import json
from zope.component import queryAdapter
from Products.Five.browser import BrowserView
from eea.app.visualization.interfaces import IVisualizationConfig
from eea.app.visualization.zopera import getToolByName

class View(BrowserView):
    """ Custom header
    """
    def __init__(self, context, request):
        super(View, self).__init__(context, request)
        self._accessor = None
        self._available = None
        self._bundle = None

    @property
    def accessor(self):
        """ Get config
        """
        if not self._accessor:
            self._accessor = queryAdapter(self.context, IVisualizationConfig)
        return self._accessor

    @property
    def available(self):
        """ Is this view available
        """
        if self._available is None:
            for view in self.accessor.views:
                name = view.get('name', '')
                if name == u'daviz.properties':
                    continue
                if name.startswith('daviz.') or name.startswith('exhibit.'):
                    self._available = True
                    break
        return self._available

    @property
    def bundle(self):
        """ Enable bundle
        """
        if self._bundle is not None:
            return self._bundle

        self.jstool = getToolByName(self.context, 'portal_javascripts', None)
        if self.jstool:
            self._bundle = not self.jstool.getDebugMode()
        else:
            self._bundle = True
        return json.dumps(self._bundle)

    @property
    def sources(self):
        """ External sources
        """
        sources = self.accessor.sources
        for source in sources:
            yield source
