""" Timeplot view
"""
from zope.interface import implements
from eea.app.visualization.views.view import ViewForm
from eea.exhibit.views.timeplot.interfaces import IExhibitTimeplotView

class View(ViewForm):
    """ Timeplot view
    """
    label = 'Timeplot View'
    implements(IExhibitTimeplotView)
