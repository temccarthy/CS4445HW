from problem1 import *
import numpy as np
import sys

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 1 (22 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

#---------------------------------------------------
def test_compute_BA():
    ''' (3 points) compute_BA'''
    BA = compute_BA(3, 17)
    assert np.allclose(BA, .1765, atol = 1e-3)
    BA = compute_BA(672, 9079)
    assert np.allclose(BA, .074, atol = 1e-3)
#---------------------------------------------------
def test_compute_OBP():
    ''' (3 points) compute_OBP'''
    OBP = compute_OBP(3, 37, 29, 5, 2)
    assert np.allclose(OBP, .507, atol = 1e-3)
    OBP = compute_OBP(2, 35, 28, 6, 1)
    assert np.allclose(OBP, .514, atol = 1e-3)
#---------------------------------------------------
def test_compute_B1():
    ''' (3 points) compute_B1'''
    B1 = compute_B1(10,3,2,1)
    assert B1==4
    B1 = compute_B1(20,8,7,2)
    assert B1==3
#---------------------------------------------------
def test_compute_TB():
    ''' (3 points) compute_TB'''
    TB = compute_TB(4,3,2,1)
    assert TB==20
    TB = compute_TB(8,5,4,3)
    assert TB==42
#---------------------------------------------------
def test_compute_SLG():
    ''' (3 points) compute_SLG'''
    SLG = compute_SLG(5, 10)
    assert np.allclose(SLG, .5, atol = 1e-3)
    SLG = compute_SLG(15,24)
    assert np.allclose(SLG, .625, atol = 1e-3)
#---------------------------------------------------
def test_compute_runs():
    ''' (3 points) compute_runs'''
    RC = compute_runs(15, 5, 12, 20)
    assert np.allclose(RC, 9.6, atol = 1e-2)
    RC = compute_runs(20, 3, 15, 30)
    assert np.allclose(RC, 10.4545, atol = 1e-2)
#---------------------------------------------------
def test_compute_wins():
    ''' (4 points) compute_wins'''
    W = compute_wins(884,645) # this is the goal of OAK team in year 2002.
    assert np.allclose(W, .6526, atol = 1e-3)

