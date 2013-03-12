""" Thumbnail view map module
"""
from zope import schema
from zope.interface import implements
from eea.exhibit.views.map.interfaces import IExhibitMapView, IExhibitMapEdit
from eea.app.visualization.views.view import ViewForm

class View(ViewForm):
    """ Thumbnail view
    """
    _label = 'Map View'
    implements(IExhibitMapView)

    ex_template = (
        '%(lens)s'
        '<div ex:role="view" ex:viewClass="Map" '
          'id="%(id)s" %(extra)s>'
        '</div>'
    )

    @property
    def label(self):
        """ View title
        """
        return self.data.get('title', '') or self._label

    @property
    def latlng(self):
        """ Return latitude longitude column
        """
        if self.data.get('lat', '') and self.data.get('lng', ''):
            return ''
        return self.data.get('latlng', '')

    @property
    def lat(self):
        """ Return latitude column
        """
        if self.latlng:
            return ''
        return self.data.get('lat', '')

    @property
    def lng(self):
        """ Return longitude column
        """
        if self.latlng:
            return ''
        return self.data.get('lng', '')

    @property
    def lens(self):
        """ View custom lens
        """
        lens = self.data.get('lens', '')
        return lens if lens else ''

    def render(self, **kwargs):
        """ Render exhibit view
        """
        options = {
            'lens': self.lens,
            'id': self.__name__.replace('.', '-'),
            'extra': ""
        }

        # Add extra stuff
        extra = []
        for name, field in schema.getFieldsInOrder(IExhibitMapEdit):
            if name == u'lens':
                continue
            elif name == u'latlng' and self.latlng:
                extra.append('ex:latlng=".%s"' % self.latlng)
                continue
            elif name == u'lat' and self.lat:
                extra.append('ex:lat=".%s"' % self.lat)
                continue
            elif name == u'lng' and self.lng:
                extra.append('ex:lng=".%s"' % self.lng)
                continue
            elif not name.startswith('ex_'):
                continue

            # Extra
            value = self.data.get(name, field.default)
            if value is None:
                continue

            ex_name = name.replace('ex_', 'ex:')
            extra.append('%s="%s"' % (ex_name, value))
        options['extra'] = " ".join(extra)

        return self.ex_template % options
