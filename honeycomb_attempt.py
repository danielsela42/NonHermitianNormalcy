
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np

def symmetric_kagome(m, n, ihop, ihop_opp, ohop1, ohop1_opp, ohop2, ohop2_opp):
    # m x n unit cells
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
    
H = symmetric_kagome(5, 5, 2, 1, 2, 1)
            
        
eigvals, eigvects = np.linalg.eig(H)

P = eigvects
Pinv = np.linalg.inv(eigvects)

D = np.zeros(np.shape(H), dtype=complex)
for i in range(len(eigvals)):
    D[i, i] = eigvals[i]
    
Dc= np.conjugate(D)

Hp = np.dot(np.dot(P, Dc), Pinv)
t_diff= Hp - np.transpose(Hp)

commutator = np.dot(H, Hp) - np.dot(Hp, H)

# print("Dc computed")
# print(np.dot(np.dot(Pinv, Hp), P))

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