""" Doctests
"""
import doctest
import unittest
from eea.exhibit.tests.base import EEAExhibitFunctionalTestCase
from Testing.ZopeTestCase import FunctionalDocFileSuite


OPTIONFLAGS = (
        doctest.REPORT_ONLY_FIRST_FAILURE |
        doctest.ELLIPSIS |
        doctest.NORMALIZE_WHITESPACE
)

def test_suite():
    """ Tests
    """
    return unittest.TestSuite((
            FunctionalDocFileSuite('README.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.exhibit',
                  test_class=EEAExhibitFunctionalTestCase),
              ))


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
