#!/bin/bash 
#SBATCH -N 1
#SBATCH -n 64
 
source /public9/soft/module.sh
module load intel/18.0.2
export PATH=/public9/home/sc54385/software/VASP5.4.4/vasp.5.4.4/bin:$PATH
#module load mpi/intel/18.0.2
srun vasp_std_zrelax

