import numpy as np
import Math
import Topologies.TestTopology
import Modelling
# LLVM compiler
from numba import njit


if __name__ == "__main__":
    MA, next = Math.FloydPathReconstruct(Topologies.TestTopology.cluster)
    print(next)
    betw = Math.Betweeness(next)
    print(betw)
    Math.PrintProperties(1, Topologies.TestTopology.cluster)
    print(np.argmax(betw))
    MB = Modelling.DropAndTest(Topologies.TestTopology.cluster, betw)
    print(MB)