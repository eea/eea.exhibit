""" Tests setup
"""
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure

PRODUCTS = ['FiveSite', 'eea.exhibit']

@onsetup
def setup_eea_exhibit():
    """ Setup
    """
    fiveconfigure.debug_mode = True
    import Products.Five
    import eea.exhibit
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.Five)
    zcml.load_config('configure.zcml', eea.exhibit)
    fiveconfigure.debug_mode = False

    PloneTestCase.installProduct('Five')
    for i in PRODUCTS:
        PloneTestCase.installProduct(i)

setup_eea_exhibit()
PloneTestCase.setupPloneSite(products=PRODUCTS)


class EEAExhibitFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """ Functional test case
    """
