import numpy as np
import Math
# LLVM compiler
from numba import njit

@njit(parallel=True)
def TernaryDebrujin(step):
  debrujin_cluster = np.zeros(shape=((3**step), (3**step)), dtype=np.int64)
  for i in range(0, 3 ** step):
    shl = Math.ternary_shl(i, step)
    for s in shl:
      debrujin_cluster[i, s] = 1
      debrujin_cluster[s, i] = 1
  return debrujin_cluster