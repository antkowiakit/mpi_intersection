import numpy as np
import sys
import time


def generate_numbers_list(number):
    sets = []
    for x in range(0, number):
        numbers_list = np.random.randint(0, 50, 100)
        numbers_list = np.append(numbers_list, [4000])
        sets.append(numbers_list)

    return sets

start_time = time.time()

number = int(sys.argv[1])

sets = generate_numbers_list(number)

# sets = []
# for x in range(0, number):
#     sets.append(np.loadtxt('sets/' + str(x) + '.txt', dtype=int))

intersect = []
for idx, item in enumerate(sets):
    if len(sets) == 1:
        intersect = sets[idx]
    elif idx == 0:
        intersect = np.intersect1d(sets[idx], sets[idx + 1])
    elif idx == 1:
        pass
    else:
        intersect = np.intersect1d(sets[idx], intersect)

print('intersect: {:s}'.format(str(intersect)))
print('--- {:f} seconds ---'.format(time.time() - start_time))
