
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np

def checkerboard(m, n, t, t_opp):
    ''' Generate a checkerboard hopping Hamiltonian.

    Inputs: m - number of unit cells in x direction
            n - number of unit cells in y direction
            t - hopping along a counterclockwise loop
            t_opp - hopping along a clockwise loop
    '''
    # m x n unit cells
    length = 2 * m * n
    H = np.zeros((length, length), dtype=complex)
    for i in range(m):
        for j in range(n):
            a = 2 * n * i + 2 * j + 0
            b = 2 * n * i + 2 * j + 1
            
            ab = 2 * n * i + 2 * ((j + 1) % n) + 1
            ba = 2 * n * ((i + 1) % m) + 2 * j + 0
            
            H[a, b] += t
            H[b, a] += t_opp
        
            H[b, ba] += t
            H[ba, ab] += t
            H[ab, a] += t

            H[ba, b] += t_opp
            H[ab, ba] += t_opp
            H[a, ab] += t_opp

    return H
    
# Test the checkerboard Hamiltonian
if __name__ == "__main__":
    H = checkerboard(10, 10, 1, 1) # Hamiltonian

    # Get eigenvalus and diagonalizing matrix P
    eigvals, eigvects = np.linalg.eig(H)
    P = eigvects
    Pinv = np.linalg.inv(eigvects)

    # Diagonalize H
    D = np.zeros(np.shape(H), dtype=complex)
    for i in range(len(eigvals)):
        D[i, i] = eigvals[i]
    
    # Conjugate of diagonal matrix
    Dc = np.conjugate(D)

    # Construct H' as the matrix with the same eigenvectors but conjugate eigenvalues
    Hp = np.dot(np.dot(P, Dc), Pinv)
    t_diff = Hp - np.transpose(Hp)

    # Commutator [H, H']
    commutator = np.dot(H, Hp) - np.dot(Hp, H)

    print("Printing where H[i, j] = 0 but Hp[i, j] or Hp[j, i] nonzero")

    for i in range(len(H)):
        for j in range(len(H)):
            if H[i, j] == 0 or H[j, i] == 0: 
                assert(H[j, i] == 0)
                # assert(t_diff[i, j] * np.conjugate(t_diff[i, j]) < 10**(-8))
                if not Hp[i, j] * np.conjugate(Hp[i, j]) < 10**(-6) or not Hp[j, i] * np.conjugate(Hp[j, i]) < 10**(-6):
                    print(i, j, Hp[i, j], Hp[j, i])
                assert(commutator[i, j] * np.conjugate(commutator[i, j]) < 10**(-8))
        
    print("Print H, Hp component wise")  
    for i in range(len(H)):
        for j in range(i, len(H)):
            if H[i, j] == 0: continue
            print(i, j)
            print(H[i, j], H[j, i])
            print(Hp[i, j], Hp[j, i])