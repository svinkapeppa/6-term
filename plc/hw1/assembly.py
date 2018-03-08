import sys

import numpy as np

code = np.array([11, 0, 2, 0, 0,
                 11, 1, 2, 0, 0,
                 6, 1, 2, 0, 2,
                 0, 0, 2, 0, 3,
                 8, 1, 3, 0, 0,
                 2, 0, 0, 0, 0], dtype=np.int32)

code.tofile(sys.argv[1])
print(code)
