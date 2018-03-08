import numpy as np
import sys

code = np.fromfile(sys.argv[1], dtype=np.int32)
print(code[::2])
