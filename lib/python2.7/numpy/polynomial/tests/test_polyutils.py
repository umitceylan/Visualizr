"""Tests for polyutils module.

"""
from __future__ import division

import numpy as np
import numpy.polynomial.polyutils as pu
from numpy.testing import *

class TestMisc(TestCase) :

    def test_trimseq(self) :
        for i in range(5) :
            tgt = [1]
            res = pu.trimseq([1] + [0]*5)
            assert_equal(res, tgt)

    def test_as_series(self) :
        # check exceptions
        assert_raises(ValueError, pu.as_series, [[]])
        assert_raises(ValueError, pu.as_series, [[[1,2]]])
        assert_raises(ValueError, pu.as_series, [[1],['a']])
        # check common types
        types = ['i', 'd', 'O']
        for i in range(len(types))  :
            for j in range(i) :
                ci = np.ones(1, types[i])
                cj = np.ones(1, types[j])
                [resi, resj] = pu.as_series([ci, cj])
                assert_(resi.dtype.char == resj.dtype.char)
                assert_(resj.dtype.char == types[i])

    def test_trimcoef(self) :
        coef = [2, -1, 1, 0]
        # Test exceptions
        assert_raises(ValueError, pu.trimcoef, coef, -1)
        # Test results
        assert_equal(pu.trimcoef(coef), coef[:-1])
        assert_equal(pu.trimcoef(coef, 1), coef[:-3])
        assert_equal(pu.trimcoef(coef, 2), [0])


class TestDomain(TestCase) :

    def test_getdomain(self) :
        # test for real values
        x = [1, 10, 3, -1]
        tgt = [-1,10]
        res = pu.getdomain(x)
        assert_almost_equal(res, tgt)

        # test for complex values
        x = [1 + 1j, 1 - 1j, 0, 2]
        tgt = [-1j, 2 + 1j]
        res = pu.getdomain(x)
        assert_almost_equal(res, tgt)

    def test_mapdomain(self) :
        # test for real values
        dom1 = [0,4]
        dom2 = [1,3]
        tgt = dom2
        res = pu. mapdomain(dom1, dom1, dom2)
        assert_almost_equal(res, tgt)

        # test for complex values
        dom1 = [0 - 1j, 2 + 1j]
        dom2 = [-2, 2]
        tgt = dom2
        x = dom1
        res = pu.mapdomain(x, dom1, dom2)
        assert_almost_equal(res, tgt)

        # test for multidimensional arrays
        dom1 = [0,4]
        dom2 = [1,3]
        tgt = np.array([dom2, dom2])
        x = np.array([dom1, dom1])
        res = pu.mapdomain(x, dom1, dom2)
        assert_almost_equal(res, tgt)

        # test that subtypes are preserved.
        dom1 = [0,4]
        dom2 = [1,3]
        x = np.matrix([dom1, dom1])
        res = pu.mapdomain(x, dom1, dom2)
        assert_(isinstance(res, np.matrix))

    def test_mapparms(self) :
        # test for real values
        dom1 = [0,4]
        dom2 = [1,3]
        tgt = [1, .5]
        res = pu. mapparms(dom1, dom2)
        assert_almost_equal(res, tgt)

        # test for complex values
        dom1 = [0 - 1j, 2 + 1j]
        dom2 = [-2, 2]
        tgt = [-1 + 1j, 1 - 1j]
        res = pu.mapparms(dom1, dom2)
        assert_almost_equal(res, tgt)
