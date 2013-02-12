""" Tiles view module
"""
from zope import schema
from zope.interface import implements
from eea.app.visualization.views.view import ViewForm
from eea.exhibit.views.tile.interfaces import IExhibitTileView
from eea.exhibit.views.tile.interfaces import IExhibitTileEdit

class View(ViewForm):
    """ Tile view
    """
    _label = 'Tile View'
    implements(IExhibitTileView)

    ex_template = (
        '%(lens)s'
        '<div ex:role="exhibit-view" id="%(id)s" %(extra)s>'
        '</div>'
    )

    @property
    def label(self):
        """ View title
        """
        return self.data.get('title', '') or self._label

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
        for name, field in schema.getFieldsInOrder(IExhibitTileEdit):
            if name == u"lens":
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
