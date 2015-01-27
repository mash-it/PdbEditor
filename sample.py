# sample: output shifted structure (x direction, 100 AA)
from PdbEditor import Molecule

mol = Molecule("pdbfile/1SRL.pdb")
mol.shift('x', 100)
mol.output("shifted.pdb")

