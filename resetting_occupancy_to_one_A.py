from Bio import *
from Bio.PDB import PDBIO
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder

structure = PDBParser().get_structure('x', 'test.pdb')


def occ_modification():
    chain_id = structure.get_chains()
    for i in chain_id:
        for j in i.get_residues():
            for k in j.get_atoms():
                 if k.get_occupancy() < 1.0:
                    
                    print(j.get_resname(), ' :  \n')
                    print('before :', k.get_occupancy())
                    k.set_occupancy(1.0) # only resets occupancy for alt conf A by default
                    print('after :', k.get_occupancy())


#occ_modification()

io = PDBIO()
io.set_structure(structure)
io.save("occ_modified.pdb", write_end =False, preserve_atom_numbering=  True)
