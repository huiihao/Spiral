#!/usr/bin/python
import dpdata
d_poscar = dpdata.System('POSCAR')
d_poscar.to('lammps/lmp','conf.lmp')
