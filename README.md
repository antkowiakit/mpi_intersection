# Multiple arrays intersection in Python using MPI
* File **single.py** calculate intersection on single core and theard 
* File **mpi.py** calculate intersection on multiple machines. Root machine send parts of input array to children. Children send result do root. Root make intersection of receive arrays.
* File **mpi_pre_loaded.py** calculate intersection on multiple machines. Children generate his own arrays and send result do root. Root make intersection of receive arrays.