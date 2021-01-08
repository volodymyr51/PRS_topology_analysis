import numpy as np
import Math
from Topologies import TestTopology, MassivelyExcessDeBrujin, TernaryDebrujin
import Modelling
# LLVM compiler
from numba import njit

def PrintResults(resArray):
    for res in resArray:
        print(res)


if __name__ == "__main__":
    Math.PrintProperties(1, MassivelyExcessDeBrujin.MassivelyExcessDeBruijn(4))

    cluster = MassivelyExcessDeBrujin.MassivelyExcessDeBruijn(4)
    Math.PrintProperties(8, cluster)
    betweeness = Math.Betweeness(cluster)
    res = Modelling.TestScenarios(cluster, betweeness, ceiling=0.1)
    PrintResults(res)