import numpy as np
import sys

description_phrase = 'This program calculates the n-th number in fibonacci sequence [1, 1, 2, 3, 5, 8, ...].'
enter_phrase = 'Enter a number:'

code = np.array([1, len(description_phrase)], dtype=np.int32)

for char in description_phrase:
    code = np.append(code, ord(char))

code = np.append(code, [1, len(enter_phrase)])

for char in enter_phrase:
    code = np.append(code, ord(char))

code = np.append(code, [0, 2, 0,
                        2, 0, 0])

code.tofile(sys.argv[1])
print(code)
