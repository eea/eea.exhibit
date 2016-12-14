""" Babel translator
"""
import logging
from zope.component import queryUtility
from Products.Five.browser import BrowserView
from eea.exhibit.babel.interfaces import IBabelReader, IBabelWriter

logger = logging.getLogger('eea.exhibit.babel')

class Translator(BrowserView):
    """ Translate
    """
    def __call__(self, **kwargs):
        if self.request:
            kwargs.update(self.request.form)

        abs_url = self.context.absolute_url()
        url = kwargs.get('url', '')
        if not url:
            logger.warn('Empty Babel URL: "%s" at "%s"', url, abs_url)
            return ""

        reader = kwargs.get('reader', '')
        reader = queryUtility(IBabelReader, name=reader)
        if not reader:
            logger.warn('Unknown babel reader: "%s" at "%s"', reader, abs_url)
            return ""

        write = kwargs.get('writer', '')
        writer = queryUtility(IBabelWriter, name=write)
        if not writer:
            logger.warn('Unknown babel writer: "%s" at "%s"', writer, abs_url)
            return ""

        try:
            items = reader(url)
        except Exception as err:
            logger.exception(err)
            return ""

        try:
            output = writer(items)
        except Exception as err:
            logger.exception(err)
            return ""

        callback = kwargs.get('callback', '')
        if not callback or callback == '?':
            return output

        if self.request and 'jsonp' in write:
            self.request.response.setHeader('Content-Type', 'application/jsonp')
        return "%s(%s)" % (callback, output)
