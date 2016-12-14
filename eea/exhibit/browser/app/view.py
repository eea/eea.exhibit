""" Browser views
"""
import json
import logging
from zope.component import queryAdapter, queryUtility
from Products.Five.browser import BrowserView
from eea.app.visualization.interfaces import IVisualizationConfig
from eea.app.visualization.zopera import getToolByName
from eea.app.visualization.zopera import IPropertiesTool
from eea.app.visualization.interfaces import IDavizSettings

logger = logging.getLogger('eea.exhibit')

class View(BrowserView):
    """ Custom header
    """
    def __init__(self, context, request):
        super(View, self).__init__(context, request)
        self._settings = None
        self._accessor = None
        self._available = None
        self._bundle = None
        self._exhibit3 = None

    @property
    def settings(self):
        """ Persistent utility for site_properties
        """
        if self._settings is None:
            ds = queryUtility(IDavizSettings)
            settings = ds.settings if ds else {}
            self._settings = {
                'version': settings.get('exhibit.framework', 3),
                'ieExhibit2': settings.get(
                    'exhibit.ieForceExhibit2', True)
            }
        return self._settings

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
    def exhibit3(self):
        """ Browser is Internet Explorer
        """
        if self._exhibit3 is not None:
            return self._exhibit3

        # Force Exhibit 2 for IE as Exhibit 3 is not supported yet
        if (self.settings['ieExhibit2'] and
            'MSIE ' in getattr(self.request, 'HTTP_USER_AGENT', '')):
            self._exhibit3 = False
            return self._exhibit3

        # Get Exhibit version from @@daviz-settings
        try:
            version = int(self.settings['version'])
        except Exception:
            version = 3

        self._exhibit3 = False
        if version == 3:
            self._exhibit3 = True

        return self._exhibit3

    @property
    def gmapkey(self):
        """ Get Google Maps key from
            portal_properties.geographical_properties.google_key
        """
        ptool = queryUtility(IPropertiesTool)
        props = getattr(ptool, 'geographical_properties', None)
        if callable(props):
            try:
                props = props(context=self.context, request=self.request)
            except Exception, err:
                logger.debug(err)

        if getattr(props, 'getProperty', None):
            key = props.getProperty('google_key', '')
        else:
            key = getattr(props, 'google_key', '')

        return key

    @property
    def sources(self):
        """ External sources
        """
        sources = self.accessor.sources
        for source in sources:
            yield source
