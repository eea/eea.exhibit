""" View tabular views
"""
from zope import schema
from zope.interface import implements
from zope.component import queryAdapter
from eea.app.visualization.interfaces import IVisualizationConfig
from eea.app.visualization.views.view import ViewForm
from eea.exhibit.views.tabular.interfaces import IExhibitTabularView
from eea.exhibit.views.tabular.interfaces import IExhibitTabularEdit

class View(ViewForm):
    """ Tabular view
    """
    label = 'Tabular View'
    implements(IExhibitTabularView)

    ex_template = (
        '%(lens)s'
        '<div ex:role="view" ex:viewClass="Tabular" id="%(id)s" %(extra)s>'
        '</div>'
    )


    @property
    def details(self):
        """ Show details column?
        """
        return self.data.get('details', False)

    @property
    def columns(self):
        """ Returns columns property for tabular view
        """
        columns = self.data.get('columns', [])
        for column in columns:
            yield '.%s' % column

        if self.details:
            yield '!label'

    @property
    def formats(self):
        """ Column formats
        """
        accessor = queryAdapter(self.context, IVisualizationConfig)
        columns = self.data.get('columns', [])
        for column in columns:
            facet = accessor.facet(column, {})
            itype = facet.get('item_type', 'text')
            yield itype

        if self.details:
            yield "item {title: expression('more')}"

    @property
    def labels(self):
        """ Returns labels property for tabular view
        """
        accessor = queryAdapter(self.context, IVisualizationConfig)
        columns = self.data.get('columns', [])

        for column in columns:
            facet = accessor.facet(column, {})
            label = facet.get('label', column)
            yield label

        if self.details:
            yield 'Details'

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
        for name, field in schema.getFieldsInOrder(IExhibitTabularEdit):
            if name == u"lens":
                continue
            elif name == u"columns":
                extra.append('ex:columns="%s"' % ", ".join(self.columns))
                extra.append('ex:columnLabels="%s"' % ", ".join(self.labels))
                extra.append('ex:columnFormats="%s"' % ", ".join(self.formats))
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
