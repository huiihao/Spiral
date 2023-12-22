#!/bin/bash -l
#SBATCH -N 1
#SBATCH --ntasks-per-node 4
#SBATCH -t 200:0:0
#SBATCH --partition v100
#SBATCH --mem=64G
#SBATCH --qos gpu-huge
#SBATCH --gres=gpu:1
/storage/liushiLab/huyihao/DPMD/Version2.0.1/bin/lmp -in input_npt.lammps > lmp.log


