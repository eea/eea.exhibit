""" Timeline View
"""
from zope.interface import implements
from eea.exhibit.views.timeline.interfaces import IExhibitTimelineView
from eea.app.visualization.views.view import ViewForm

class View(ViewForm):
    """ Timeline view
    """
    label = 'Timeline View'
    implements(IExhibitTimelineView)

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
        return self.data.get('lens', '')
