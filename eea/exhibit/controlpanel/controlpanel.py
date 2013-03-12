""" Control Panel Section
"""
from zope.interface import implements
from eea.app.visualization.controlpanel.interfaces import IDavizSection
from zope.formlib.form import FormFields
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from eea.app.visualization.config import EEAMessageFactory as _

class ExhibitSection(object):
    """ Simile Exhibit Settings Section
    """
    implements(IDavizSection)

    prefix = 'exhibit'
    title = 'Simile Exhibit Settings'
    form_fields = FormFields(
        schema.Choice(
            __name__='exhibit.framework',
            title=_(u'Version'),
            description=_(u"use the following version of Simile Exhibit "
                          "Framework"),
            required=True,
            default=3,
            vocabulary=SimpleVocabulary([
                SimpleTerm(2, 2, u"2.2.0"),
                SimpleTerm(3, 3, u"3.0.0"),
            ])
        ),
    )
