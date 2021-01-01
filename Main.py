import numpy as np
import Math
import Topologies.TestTopology
import Topologies.MassivelyExcessDeBrujin
import Modelling
# LLVM compiler
from numba import njit

def PrintResults(resArray):
    for res in resArray:
        print(res)


if __name__ == "__main__":
    cluster = Topologies.MassivelyExcessDeBrujin.MassivelyExcessDeBruijn(3)
    Math.PrintProperties(3, cluster)
    betweeness = Math.Betweeness(cluster)
    res = Modelling.TestScenarios(cluster, betweeness, ceiling=0.2)
    PrintResults(res)