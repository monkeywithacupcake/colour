#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour.volume.macadam_limits` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from colour.volume import is_within_macadam_limits

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestIsWithinMacadamLimits']


class TestIsWithinMacadamLimits(unittest.TestCase):
    """
    Defines :func:`colour.volume.macadam_limits.is_within_macadam_limits`
    definition unit tests methods.
    """

    def test_is_within_macadam_limits(self):
        """
        Tests :func:`colour.volume.macadam_limits.is_within_macadam_limits`
        definition.
        """

        self.assertTrue(
            is_within_macadam_limits(np.array([0.3205, 0.4131, 0.51]), 'A'))

        self.assertFalse(
            is_within_macadam_limits(np.array([0.0005, 0.0031, 0.001]), 'A'))

        self.assertTrue(
            is_within_macadam_limits(np.array([0.4325, 0.3788, 0.1034]), 'C'))

        self.assertFalse(
            is_within_macadam_limits(np.array([0.0025, 0.0088, 0.034]), 'C'))

    def test_n_dimensional_is_within_macadam_limits(self):
        """
        Tests :func:`colour.volume.macadam_limits.is_within_macadam_limits`
        definition n-dimensional arrays support.
        """

        a = np.array([0.3205, 0.4131, 0.51])
        b = np.array([True])
        np.testing.assert_almost_equal(
            is_within_macadam_limits(a, 'A'),
            b)

        a = np.tile(a, (6, 1))
        b = np.tile(b, 6)
        np.testing.assert_almost_equal(
            is_within_macadam_limits(a, 'A'),
            b)

        a = np.reshape(a, (2, 3, 3))
        b = np.reshape(b, (2, 3))
        np.testing.assert_almost_equal(
            is_within_macadam_limits(a, 'A'),
            b)


if __name__ == '__main__':
    unittest.main()
