import numpy as np
import Math
import Topologies.TestTopology
# LLVM compiler
from numba import njit

def DropAndTest(MA, betweeness):
    max = np.argmax(betweeness)
    MA = np.delete(MA, max, 0)
    MA = np.delete(MA, max, 1)
    Math.PrintProperties(-1, MA)
    return MA

#TODO: Automate drops and tests until certain point
'''
:parameter MA - graph matrix
:returns res - Resulting string
'''
def TestScenarios(MA, betweeness, ceiling=0.1):
    res = []
    for i in range(np.int(np.ceil(len(MA) * ceiling))):
        max = np.argmax(betweeness)
        MA = np.delete(MA, max, 0)
        MA = np.delete(MA, max, 1)
        betweeness = np.delete(betweeness, max, 0)
        res.append(Math.GetPropertiesString(-1, MA))
    return res