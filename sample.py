# sample: output shifted structure to avoid collision
from PdbEditor import Molecule

mol = Molecule("pdbfile/1SRL.pdb")

xs,ys,zs =  mol.get_boxsize()
print "BOX:", xs, ys, zs
print "x-length:", xs[1] - xs[0]

mol.shift('x', xs[1] - xs[0])
mol.output("shifted.pdb")

