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

'''
:parameter MA - graph matrix
:returns res - Resulting string
'''
def TestScenarios(MA, betweeness, ceiling=0.1, coding=3):
    res = []
    for i in range(np.int(np.ceil(len(MA) * ceiling))):
        max = np.argmax(betweeness)
        betw = betweeness[max]
        MA = np.delete(MA, max, 0)
        MA = np.delete(MA, max, 1)
        betweeness = np.delete(betweeness, max, 0)
        res.append(Math.GetPropertiesString(-1, MA))
        if coding == 3:
            res.append(" Removed node: {}, that has betweeness parameter of {}".format(Math.ConvertFromBaseThreeToExcessive(Math.ConvertToBase(max, 3)), betw))
        if coding == 5:
            res.append(" Removed node: {}, that has betweeness parameter of {}".format(Math.ConvertFromBaseFiveToExcessive(Math.ConvertToBase(max, 5)), betw))
        if coding == 7:
            res.append(" Removed node: {}, that has betweeness parameter of {}".format(Math.ConvertFromBaseSevenToExcessive(Math.ConvertToBase(max, 7)), betw))
    return res