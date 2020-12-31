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