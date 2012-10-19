""" Thumbnail view map module
"""
from zope import schema
from zope.interface import implements
from eea.exhibit.views.map.interfaces import IExhibitMapView, IExhibitMapEdit
from eea.app.visualization.views.view import ViewForm

class View(ViewForm):
    """ Thumbnail view
    """
    label = 'Map View'
    implements(IExhibitMapView)

    ex_template = (
        '%(lens)s'
        '<div ex:role="view" ex:viewClass="Map" id="%(id)s" %(extra)s>'
        '</div>'
    )

    @property
    def latlng(self):
        """ Return latitude longitude column
        """
        return self.data.get('latlng', '')

    @property
    def lens(self):
        """ View custom lens
        """
        return self.data.get('lens', '')

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
            elif name == u'latlng':
                extra.append('ex:latlng=".%s"' % self.latlng)
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
