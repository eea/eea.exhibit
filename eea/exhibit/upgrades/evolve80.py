""" Cleanup
"""
import logging
from zope.component.interface import interfaceToName
from Products.CMFCore.utils import getToolByName
from eea.app.visualization.interfaces import IVisualizationEnabled
logger = logging.getLogger('eea.exhibit')

CLEANUP = [
    'daviz.map.preview.png',
    'daviz.tabular.preview.png',
    'daviz.tile.preview.png',
    'daviz.timeline.preview.png'
]

def cleanup_fallback_images(context):
    """ Migrate exhibit image charts"""
    ctool = getToolByName(context, 'portal_catalog')
    iface = interfaceToName(context, IVisualizationEnabled)
    brains = ctool(
        object_provides=iface,
        show_inactive=True, Language='all'
    )


    count = 0
    for brain in brains:
        doc = brain.getObject()
        clean = []
        for item in CLEANUP:
            if item in doc.objectIds():
                clean.append(item)

        if not clean:
            continue

        length = len(clean)
        logger.info('Removing %s exhibit fallback images from %s',
                    length, doc.absolute_url())
        doc.manage_delObjects(clean)
        count += length

    logger.info('Removed %s exhibit fallback images', count)
