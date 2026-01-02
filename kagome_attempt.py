
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np

def symmetric_kagome(m, n, in_hop, in_hop_opp, out_hop, out_hop_opp):
    # m x n unit cells
    length = 3 * m * n
    H = np.zeros((length, length), dtype=complex)
    for i in range(m):
        for j in range(n):
            a = 3 * n * i + 3 * j + 0
            b = 3 * n * i + 3 * j + 1
            c = 3 * n * i + 3 * j + 2
            
            ca = 3 * n * i + 3 * ((j + 1) % n) + 0
            ba = 3 * n * ((i + 1) % m) + 3 * j + 0
            cb = 3 * n * ((i - 1) % m) + 3 * ((j + 1) % n) + 1
            
            H[a, b] += in_hop
            H[b, a] += in_hop_opp
            H[b, c] += in_hop
            H[c, b] += in_hop_opp
            H[c, a] += in_hop
            H[a, c] += in_hop_opp
            
            H[c, ca] += out_hop
            H[c, cb] += np.conjugate(out_hop)
            H[b, ba] += np.conjugate(out_hop)
            H[ca, c] += out_hop_opp
            H[cb, c] += np.conjugate(out_hop_opp)
            H[ba, b] += np.conjugate(out_hop_opp)
            
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