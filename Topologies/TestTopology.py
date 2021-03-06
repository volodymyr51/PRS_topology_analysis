import numpy as np
import Math
# LLVM compiler
from numba import njit
'''
cluster = [
                [0,1,1,0,0],
                [1,0,0,1,0],
                [1,0,0,1,1],
                [0,1,1,0,1],
                [0,0,1,1,0]
]
'''
cluster = [#   0,1,2,3
                [0,1,1,0], #0
                [1,0,1,1], #1
                [1,1,0,1], #2
                [0,1,1,0]  #3
]

cluster_1 = [#   0,1,2,3,4,5,6,7
                [0,1,0,0,1,0,0,0], #0
                [1,0,1,1,1,0,0,0], #1
                [0,1,0,0,1,1,0,0], #2
                [0,1,0,0,0,1,1,1], #3
                [1,1,1,0,0,0,1,0], #4
                [0,0,1,1,0,0,1,0], #5
                [0,0,0,1,1,1,0,1], #0
                [0,0,0,1,0,0,1,0] #0

]