#%%
import numpy as np
import zebra

# Test case 1: Identity matrix
print("Test case 1:")
mol1 = np.eye(3)
qc = zebra.QuantumCalculator()
energy1, eigenvectors1 = qc.hartree_fock(mol1)

# Test case 2: Random matrix
print("\nTest case 2:")
mol2 = np.random.rand(3, 3)
energy2, eigenvectors2 = qc.hartree_fock(mol2)

# Test case 3: Zero matrix
print("\nTest case 3:")
mol3 = np.zeros((3, 3))
energy3, eigenvectors3 = qc.hartree_fock(mol3)

# Test case 4: H2 molecule
print("\nTest case 4:")
mol4 = np.array([[1.0, 0.5], [0.5, 1.0]])
energy4, eigenvectors4 = qc.hartree_fock(mol4)

#%%
import numpy as np
import zebra

# Test case 5: CIS calculation test
print("\nTest case 5:")
mol5 = np.array([[1.0, 0.5, 0.2], [0.5, 1.0, 0.8], [0.1, 0.7, 0.4]])
qc = zebra.QuantumCalculator()
energy5, eigenvectors5 = qc.cis(mol5)

# %%

