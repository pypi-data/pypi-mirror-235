#!/usr/bin/env python3
#
# Tests the importers for various formats
#
# This file is part of Myokit.
# See http://myokit.org for copyright, sharing, and licensing details.
#
import os
import unittest

import myokit
import myokit.formats as formats

from myokit.tests import DIR_FORMATS


class ImporterTest(unittest.TestCase):
    """ Test shared importer functionality. """

    def test_importer_interface(self):
        # Test listing and creating importers.
        ims = myokit.formats.importers()
        self.assertTrue(len(ims) > 0)
        for i in ims:
            self.assertIsInstance(i, str)
            i = myokit.formats.importer(i)
            self.assertTrue(isinstance(i, myokit.formats.Importer))

    def test_unknown(self):
        # Test requesting an unknown importer.
        # Test fetching using importer method
        self.assertRaisesRegex(
            KeyError, 'Importer not found', myokit.formats.importer, 'blip')


class AxonTest(unittest.TestCase):
    """ Partially tests Axon formats importing. """

    def test_capability_reporting(self):
        # Test if the right capabilities are reported.
        i = formats.importer('abf')
        self.assertFalse(i.supports_component())
        self.assertFalse(i.supports_model())
        self.assertTrue(i.supports_protocol())

    def test_protocol(self):
        i = formats.importer('abf')
        self.assertTrue(i.supports_protocol())
        i.protocol(os.path.join(DIR_FORMATS, 'abf-v1.abf'))


if __name__ == '__main__':
    unittest.main()
