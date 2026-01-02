# Non-Hermitian Lattice Hamiltonians (Exploratory Work)

This repository contains **exploratory / scratch work** investigating classes of **non-Hermitian lattice Hamiltonians** on 2D lattices (square, checkerboard, honeycomb, kagome). The goal was to identify structural patterns that would allow **spectral information**—in particular the **density of states**—to be estimated from **operator moments** alone.

Although the specific Hamiltonians explored here ultimately **do not exhibit a non-Hermitian skin effect**, the code documents systematic tests of normality, hopping structure, and spectral consistency that were part of this search.

---

## Scientific Motivation

For non-Hermitian Hamiltonians <img src="svgs/5fde7705b9890304582d9021bfb5160a.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/>, direct diagonalization can be expensive or impractical in large systems. A motivating idea behind this project was:

> **Can spectral properties (e.g. density of states) be inferred from moments of the form**
> <p align="center"><img src="svgs/dd46d1afc94698b8f4cea7e59b7227b2.svg?invert_in_darkmode" align=middle width=83.07855765000001pt height=18.88772655pt/></p>
> **without full diagonalization?**

When <img src="svgs/5fde7705b9890304582d9021bfb5160a.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/> is Hermitian, these moments can be computed **combinatorially**, by counting closed loops on the lattice with direction-dependent hopping amplitudes. However, the typically distinct eigenspaces of non-Hermitian Hamiltonians poses a challenge to this combinatorial approach. Therefore, in this attempt, we replace <img src="svgs/1ef2080f67f60c3c050d205e3df6135c.svg?invert_in_darkmode" align=middle width=21.02739704999999pt height=27.91243950000002pt/> with the matrix <img src="svgs/2a01fb54eb9d47b4e26dce39b616d11c.svg?invert_in_darkmode" align=middle width=18.78993104999999pt height=24.7161288pt/> that shares eigenvectors with H but with conjugate eigenvalues. We attempted to identify a class of non-Hermitian Hamiltonians, some of which may have skin effect, that would permit a combinatorial closed loop counting approach to computing the spectral moments.

If successful, this would allow:

* Efficient estimation of spectral properties
* Identification of topological or non-Hermitian features
* Possible detection of the **non-Hermitian skin effect** using only local information

---

## Skin Effect and Why It Matters

The **non-Hermitian skin effect** refers to the accumulation of eigenstates at system boundaries due to asymmetric hopping. It is a hallmark of genuinely non-Hermitian physics and cannot be captured by Hermitian or normal operators.

A key objective was:

* To determine whether the presence (or absence) of the skin effect could be inferred **purely from moments**, without computing eigenstates explicitly.

However, for the Hamiltonians explored here, <img src="svgs/2a01fb54eb9d47b4e26dce39b616d11c.svg?invert_in_darkmode" align=middle width=18.78993104999999pt height=24.7161288pt/> had a different combinatorially structure than <img src="svgs/5fde7705b9890304582d9021bfb5160a.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/>, leading to difficulty applying the loop counting method.

---

## Lattice Models Implemented

### Square Lattice (`square_attempt.py`)

* Two sites per unit cell
* Distinct hoppings in x and y directions
* Periodic boundary conditions

### Checkerboard Lattice (`checkerboard_attempt.py`)

* Two sites per unit cell
* Direction-dependent hopping around plaquettes
* Periodic boundary conditions

### Honeycomb Lattice (`honeycomb_attempt.py`)

* Two sublattices (A/B)
* Asymmetric intra- and inter-cell hopping

### Kagome Lattice (`kagome_attempt.py`)

* Three sites per unit cell
* Frustrated geometry with flat-band structure
* Direction-dependent complex hopping

Each lattice is constructed in **real space** with explicit hopping matrices.

---

## What the Code Tests

Each file performs the following diagnostic checks:

1. **Hamiltonian construction** with asymmetric hopping
2. **Exact diagonalization** using NumPy
3. **Reconstruction of a conjugate-eigenvalue Hamiltonian**
   $$
   H' = P \overline{D} P^{-1}
   $$
4. **Commutating verification**
   $$
   [H, H'] = 0
   $$

5. **Hopping consistency checks**

   * Ensures no new matrix elements appear under conjugation
   * Confirms loop structure preservation

These tests were used to rule out candidate Hamiltonians that *look* non-Hermitian but behave spectrally like Hermitian ones.

---

## Why This Work Is Still Useful

Even though the original goal was not achieved, this work:

* Provides reusable lattice construction templates
* Demonstrates systematic testing of non-Hermitian normality
* Helps narrow the search space for genuinely normal non-Hermitian Hamiltonians with skin effect

Negative results are informative in exploratory research, and this repository documents one such path.

---

## Requirements

```bash
pip install numpy
```

---

## How to Run

Each file is self-contained:

```bash
python square_attempt.py
python checkerboard_attempt.py
python honeycomb_attempt.py
python kagome_attempt.py
```

Each script prints diagnostic output checking algebraic and spectral properties.

---

## Disclaimer

This repository represents **research scratch work**, not a finalized method or model. Code structure and performance were not optimized; clarity and testing were prioritized.
