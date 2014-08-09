# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CIE Constants
=============

Defines *CIE* constants.
"""

from __future__ import unicode_literals

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["CIE_E",
           "CIE_K"]

CIE_E = 216. / 24389.0
"""
*CIE* :math:`\epsilon` constant.

CIE_E : float

Notes
-----
-   The original *CIE* value for :math:`\epsilon` is :math:`\epsilon=0.008856`,
    **Bruce Lindbloom** has shown that this value is causing a discontinuity
    a the junction point of the two functions grafted together to create the
    *Lightness* :math:`L^*` function.

    That discontinuity can be avoided by using the rational representation as
    follows: :math:`\epsilon=216/24389`.

References
----------
.. [1]  http://brucelindbloom.com/index.html?LContinuity.html
        (Last accessed 24 February 2014)

"""

CIE_K = 24389. / 27.0
"""
*CIE* :math:`k` constant.

CIE_K : float

Notes
-----
-   The original *CIE* value for :math:`k` is :math:`k=903.3`,
    **Bruce Lindbloom** has shown that this value is causing a discontinuity
    a the junction point of the two functions grafted together to create the
    *Lightness* :math:`L^*` function.

    That discontinuity can be avoided by using the rational representation as
    follows: :math:`k=24389/27`.

References
----------
.. [2]  http://brucelindbloom.com/index.html?LContinuity.html
        (Last accessed 24 February 2014)

"""