from mpi4py import *

comm = MPI.COMM_WORLD

world_size = comm.Get_size()
world_rank = comm.Get_rank()
processor_name = MPI.Get_processor_name()

print("MPI Hello World Program")
print("Processor Name:", processor_name)
print("Processor Rank:", world_rank)
print("World Size:", world_size)

MPI.Finalize()