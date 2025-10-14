# assignment3.py

import numpy as np
from sympy import Matrix
from sympy import solve_linear_system
from sympy.matrices import Matrix as SYMatrix

#this is the given matrix and vector
a = np.array([
    [4, 8, -5],
    [-3, -6, -7],
    [2, 4, 2]
], dtype =float)

b = np.array([
    [-1],
    [-1],
    [3]
], dtype =float)

# Compute the reduced echelon form of A and convert the result back to a numpy
# array. You will need sympy to compute the reduced echelon form.
ASym = SYMatrix(a);
RREFa, piviotIndicies = ASym.rref()
RREFa = np.array(RREFa, dtype=float)
print("a)");
print(RREFa)
print("----------------------------------------------")

# Find the column space of A.
piviotIndicies=[0,2]
piviotCols = a[:, piviotIndicies]

print("b)");
for col in piviotCols.T:
    print(col.reshape(-1,1))
print("----------------------------------------------")
# Solve the matrix equation Ax = b.
augmentNP = np.hstack((a,b))
augmentSY = SYMatrix(augmentNP)
RREFaugmentSY, _=augmentSY.rref()
RREFaugmentNP=np.array(RREFaugmentSY, dtype = float)


print("c)");
print(RREFaugmentNP)
if RREFaugmentSY[-1, -1]==1 and all (RREFaugmentSY[-1,i]==0 for i in range(a.shape[1])):
    print("\n System is inconsistent as 0 is equal to 1, so Ax=b has no solution")
else:
    print("\n There is a solution")

print("----------------------------------------------")
# Compute Nul A.
nullSpace = ASym.nullspace()
print("d)");

if not nullSpace:
    print(" null space is {0}")
else:
    for vector in nullSpace:
        print(np.array(vector, dtype=float))
print("----------------------------------------------")
