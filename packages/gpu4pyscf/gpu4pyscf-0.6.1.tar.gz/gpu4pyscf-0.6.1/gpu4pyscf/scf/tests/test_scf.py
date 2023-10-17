# Copyright 2023 The GPU4PySCF Authors. All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import numpy as np
import cupy
import pyscf
from pyscf import lib
from gpu4pyscf import scf
from gpu4pyscf.dft import rks

lib.num_threads(8)

atom = '''
O       0.0000000000    -0.0000000000     0.1174000000
H      -0.7570000000    -0.0000000000    -0.4696000000
H       0.7570000000     0.0000000000    -0.4696000000
'''
bas='def2-qzvpp'
mol = pyscf.M(atom=atom, basis=bas, max_memory=32000)
mol.verbose = 4

def tearDownModule():
    global mol
    del mol

class KnownValues(unittest.TestCase):
    '''
    known values are obtained by Q-Chem
    '''
    def test_rhf(self):
        mf = scf.RHF(mol)
        mf.max_cycle = 10
        mf.conv_tol = 1e-9
        e_tot = mf.kernel()
        assert np.allclose(e_tot, -76.0667232412)

if __name__ == "__main__":
    print("Full Tests for SCF")
    unittest.main()