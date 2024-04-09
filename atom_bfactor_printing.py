from Bio.PDB.PDBParser import PDBParser

from Bio import __version__

print('########## Biopython  VERSION #####################################')
print('\n BIOPYTHON_VERSION : ', __version__, '\n')
print('###################################################################')

structure = PDBParser(PERMISSIVE=False, QUIET=False).get_structure('X', 'test.pdb')

print('\n---------------------------------------------------\n')

atom_list = structure.get_atoms()  ## its actually a generator , that get emptied when cycled

print('atom_list : \n ', [i for i in atom_list], '\n\n')

atom_list = structure.get_atoms()  ## its actually a generator , that get emptied when cycled

print('atom      ----------------> bfactor')

for atom in atom_list:
    print(atom, ' : ', atom.get_serial_number(), ' -----------> ', atom.get_bfactor())