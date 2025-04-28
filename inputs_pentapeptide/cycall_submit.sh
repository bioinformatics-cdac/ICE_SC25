#!/bin/sh
#SBATCH -N 1
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=61560
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out
#SBATCH --partition=compute
#SBATCH --export=ALL
export OMP_NUM_THREADS=1
module load apps/gromacs/2021.4/mpi/gcc_openmpi libs/openblas/0.3.27


mpirun -n 16 gmx_mpi mdrun -deffnm nvt

gmx_mpi grompp -f ../../inputs/npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p ../../inputs/topol.top -o npt.tpr -n ../../inputs/index.ndx -maxwarn 2

mpirun -n 16 gmx_mpi mdrun -deffnm npt

gmx_mpi grompp -f ../../inputs/md.mdp -c npt.gro -r npt.gro -t npt.cpt -p ../../inputs/topol.top -o md.tpr -n ../../inputs/index.ndx -maxwarn 2

mpirun -n 16 gmx_mpi mdrun -deffnm md

gmx_mpi trjconv -s md.tpr -f  md.xtc -o md_nowat.xtc -n ../../inputs/index.ndx  << EOF
1
EOF
gmx_mpi convert-tpr -s md.tpr  -o md_nowat.tpr  -n ../../inputs/index.ndx   << EOF
1
EOF
gmx_mpi trjconv -s md.gro -f md.gro -o md_nowat.gro -n ../../inputs/index.ndx << EOF
1
EOF
gmx_mpi trjconv -f md_nowat.xtc -s  md_nowat.tpr -o md_nowat_wh.xtc -pbc whole -n ../../inputs/index.ndx << EOF
1
EOF
gmx_mpi trjconv -f md_nowat_wh.xtc -s md_nowat.tpr -o md_nowat_wh_nojump.xtc -pbc nojump -n ../../inputs/index.ndx << EOF
1
EOF
