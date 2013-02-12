""" Timeline View
"""
from zope import schema
from zope.interface import implements
from eea.exhibit.views.timeline.interfaces import IExhibitTimelineView
from eea.exhibit.views.timeline.interfaces import IExhibitTimelineEdit
from eea.app.visualization.views.view import ViewForm

class View(ViewForm):
    """ Timeline view
    """
    _label = 'Timeline View'
    implements(IExhibitTimelineView)

    ex_template = (
        '%(lens)s'
        '<div ex:role="exhibit-view" ex:viewClass="Timeline" '
          'id="%(id)s" %(extra)s>'
        '</div>'
    )

    @property
    def label(self):
        """ View title
        """
        return self.data.get('title', '') or self._label

    @property
    def start(self):
        """ Start property of timeline view
        """
        start = self.data.get('start', None)
        if start:
            return '.%s' % start
        return None

    @property
    def end(self):
        """ End property of timeline view
        """
        end = self.data.get('end', None)
        if end:
            return '.%s' % end
        return None

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
        for name, field in schema.getFieldsInOrder(IExhibitTimelineEdit):
            if name == u"lens":
                continue
            elif name == u"start" and self.start:
                extra.append('ex:start="%s"' % self.start)
                continue
            elif name == u"end" and self.end:
                extra.append('ex:end="%s"' % self.end)
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
