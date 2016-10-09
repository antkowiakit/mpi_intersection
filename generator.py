import numpy as np
import sys

number = int(sys.argv[1])

for x in range(0, number):
    arr = np.random.randint(0, 30, 100)
    arr = np.append(arr, [4000])
    np.savetxt('sets/' + str(x) + '.txt', arr, fmt='%i', delimiter=",")
