
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np

def symmetric_square(m, n, hhop, hhop_opp, vhop, vhop_opp):
    ''' Construct a symmetric square lattice Hamiltonian with given hopping parameters.

    Inputs: m - number of unit cells in x direction
            n - number of unit cells in y direction
            hhop - horizontal hopping
            hhop_opp - horizontal hopping (opposite direction)
            vhop - vertical hopping
            vhop_opp - vertical hopping (opposite direction)
    '''
    length = m * n
    H = np.zeros((length, length), dtype=complex)
    for i in range(m):
        for j in range(n):
            site = n * i + j
            
            horizontal = n * ( (i + 1) % m) + j
            vertical = n * i + ( (j + 1) % n )
            
            H[site, horizontal] += hhop
            H[horizontal, site] += hhop_opp
            H[site, vertical] += vhop
            H[vertical, site] += vhop_opp
            
    return H

if __name__ == "__main__":
    # Create a symmetric square Hamiltonian 
    H = symmetric_square(2, 2, 2, 1, 2, 1)    
    # Compute eigenvalues and eigenvectors
    eigvals, eigvects = np.linalg.eig(H)

    # Construct H' using the conjugate of the eigenvalues
    P = eigvects
    Pinv = np.linalg.inv(eigvects)

    D = np.zeros(np.shape(H), dtype=complex)
    for i in range(len(eigvals)):
        D[i, i] = eigvals[i]
        
    Dc= np.conjugate(D)

    Hp = np.dot(np.dot(P, Dc), Pinv)
    t_diff= Hp - np.transpose(Hp) # Difference between Hp and its transpose

    # Check the normalcy condition [H, Hp] = 0
    commutator = np.dot(H, Hp) - np.dot(Hp, H)

    print("Printing where H[i, j] = 0 but Hp[i, j] or Hp[j, i] nonzero")

    for i in range(len(H)):
        for j in range(len(H)):
            if H[i, j] == 0 or H[j, i] == 0: 
                assert(H[j, i] == 0)
                # assert(t_diff[i, j] * np.conjugate(t_diff[i, j]) < 10**(-8))
                if not Hp[i, j] * np.conjugate(Hp[i, j]) < 10**(-6) or Hp[j, i] * np.conjugate(Hp[j, i]) < 10**(-6):
                    print(i, j, Hp[i, j], Hp[j, i])
                assert(commutator[i, j] * np.conjugate(commutator[i, j]) < 10**(-8))
        
    print("Print H, Hp component wise")  
    for i in range(len(H)):
        for j in range(i, len(H)):
            if H[i, j] == 0: continue
            print(i, j)
            print(H[i, j], H[j, i])
            print(Hp[i, j], Hp[j, i])