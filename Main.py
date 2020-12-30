import numpy as np
import Math
import Topologies.TestTopology
# LLVM compiler
from numba import njit


if __name__ == "__main__":
    MA, next = Math.FloydPathReconstruct(Topologies.TestTopology.cluster)
    print(next)
    print(Math.Betweeness(next))