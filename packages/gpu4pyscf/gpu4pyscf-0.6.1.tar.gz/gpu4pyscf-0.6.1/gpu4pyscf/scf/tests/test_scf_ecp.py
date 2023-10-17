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
import pyscf
from pyscf import lib
from gpu4pyscf import scf

lib.num_threads(8)
atom = '''
I 0 0 0 
I 1 0 0
'''
bas='def2-svp'
mol = pyscf.M(atom=atom, basis=bas, ecp=bas)
mol.verbose = 4

def tearDownModule():
    global mol
    del mol

class KnownValues(unittest.TestCase):
    def test_rhf(self):
        mf = scf.RHF(mol)
        mf.max_cycle = 10
        mf.conv_tol = 1e-9
        e_tot = mf.kernel()
        assert np.allclose(e_tot, -578.9674228876)

if __name__ == "__main__":
    print("Full Tests for SCF")
    unittest.main()