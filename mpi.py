from mpi4py import MPI
import numpy as np
import math
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

TAG = 101
ROOT = 0

comm = MPI.COMM_WORLD
tid = comm.Get_rank()
size = comm.Get_size()
# print('Tid: %s' % tid)

number = int(sys.argv[1])

if tid == ROOT:
    # Generate random lists
    list = generate_numbers_list(number)

    # list = []
    # for x in range(0, number):
    #     list.append(np.loadtxt('sets/' + str(x) + '.txt', dtype=int))

    lists_for_process = len(list) / (size - 1)
    additional_for_last_process = len(list) % (size - 1)

    for i in range(1, size):
        list_to_send = []
        for j in range(0, math.floor(lists_for_process)):
            list_to_send.append(list.pop())

        data = {'sets': list_to_send, 'len': len(list_to_send)}
        comm.send(data, dest=i, tag=TAG)
    recev = 0
    recev_list = []
    while True:
        data = comm.recv(source=-1, tag=TAG)
        if data:
            recev += 1
            if not data['empty']:
                recev_list.append(data['intersect'])
        if recev == (size-1):
            while len(list) > 0:
                recev_list.append(list.pop())
            intersect = []
            for idx, item in enumerate(recev_list):
                if len(recev_list) == 1:
                    intersect = recev_list[idx]
                elif idx == 0:
                    intersect = np.intersect1d(recev_list[idx], recev_list[idx + 1])
                elif idx == 1:
                    pass
                else:
                    intersect = np.intersect1d(recev_list[idx], intersect)
            print('intersect: {:s}'.format(str(intersect)))
            print('--- {:f} seconds ---'.format(time.time() - start_time))
            MPI.Finalize()
            exit(0)
else:
    data = comm.recv(source=0, tag=TAG)
    sets = data['sets']
    intersect = []
    if data['len'] > 0:
        empty = False
        for idx, item in enumerate(sets):
            if len(sets) == 1:
                intersect = sets[idx]
            elif idx == 0:
                intersect = np.intersect1d(sets[idx], sets[idx + 1])
            elif idx == 1:
                pass
            else:
                intersect = np.intersect1d(sets[idx], intersect)
    else:
        empty = True
    comm.send({'intersect': intersect, 'empty': empty}, dest=0, tag=TAG)

MPI.Finalize()
