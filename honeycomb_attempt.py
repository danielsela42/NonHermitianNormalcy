import numpy as np

def symmetric_honeycomb(m, n, ihop, ihop_opp, ohop1, ohop1_opp, ohop2, ohop2_opp):
    ''' Construct a symmetric honeycomb lattice Hamiltonian with given hopping parameters.

    Inputs: m - number of unit cells in x direction
            n - number of unit cells in y direction
            ihop - hopping from a to b within unit cell
            ihop_opp - hopping from b to a within unit cell
            ohop1 - hopping from a to b in neighboring unit cell (direction 1)
            ohop1_opp - hopping from b to a in neighboring unit cell (direction 1)
            ohop2 - hopping from b to a in neighboring unit cell (direction 2)
            ohop2_opp - hopping from a to b in neighboring unit cell (direction 2)
    '''
    length = 2 * m * n
    H = np.zeros((length, length), dtype=complex)
    for i in range(m):
        for j in range(n):
            a = 2 * n * i + 2 * j + 0
            b = 2 * n * i + 2 * j + 1
            
            ab = 2 * n * i + 2 * ((j + 1) % n) + 1
            ba = 2 * n * ((i + 1) % m) + 2 * j + 0

            H[a, b] += ihop
            H[b, a] += ihop_opp
            
            H[a, ab] += ohop1
            H[ab, a] += ohop1_opp
            H[b, ba] += ohop2
            H[ba, b] += ohop2_opp
            
    return H

# Test the symmetric_honeycomb function and the normalcy condition
if __name__ == "__main__":
    #  Create a symmetric honeycomb Hamiltonian
    H = symmetric_honeycomb(5, 5, 2, 1, 2, 1)
    
    # Compute eigenvalues and eigenvectors
    eigvals, eigvects = np.linalg.eig(H)

    # Construct Hp using the conjugate of the eigenvalues
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