import numpy as np
from sympy import Matrix
from sympy import solve_linear_system
from sympy.matrices import Matrix as SYMatrix

#problem 1

A =np.array([
    [1,0,1],
    [1,1,-1],
    [4,2,0],
    [3,-1,-1]
])

M = Matrix(A)
M_rref, pviotCols = M.rref()

dimension = len(pviotCols)
basis_vectors = [A[:, i] for i in pviotCols]

print("1)")
print(f"\nThe dimension of the set W is {dimension}")
print("A basis for the set W is:")
for vector in basis_vectors:
    print(vector)

print("----------------------------------------------")

def transformVector(P_matrix, vector, direction='to_standard'):
    if direction== 'to_standard':
        transformVector = P_matrix @ vector
    elif direction=='from_standard':
        P_inv = np.linalg.inv(P_matrix)
        transformVector=P_inv@vector
    else:
        raise ValueError("invalid")
    
    return transformVector

def solve():
    b1=np.array([0, -1, -1])
    b2=np.array([-4, 0, 0])
    b3=np.array([6, 6, 3])
    x=np.array([-18, 8, 5])
    xB=np.array([-2, 6, 1])

    pb = np.column_stack((b1,b2,b3))
    print("change of basis matrix:", pb)

    xToB = transformVector(pb,x, direction='from_standard')
    print("vector x transformed to basis b : ")
    print(np.round(xToB, 6))

    xBToE = transformVector(pb, xB, direction='to_standard')
    print("vector [x]B transformed to standard : ")
    print(xBToE)

solve()

print("----------------------------------------------")
P =np.array([
    [4,-9,5],
    [-3,-1,6],
    [9,-2,-6]
])

b1=np.array([0, -1, 3])
b2=np.array([4, 5, -4])
b3=np.array([3, 3, -6])

B=np.column_stack((b1,b2,b3))
Pinv=np.linalg.inv(P)
A_matrix =B@ Pinv

a1 = A_matrix[:,0] 
a2 = A_matrix[:,1] 
a3 = A_matrix[:,2] 

print("matrix p \n: ", P)
print("matrix b \n: ", B)
print("calcluated inverse of p : ",Pinv)
print ("matirx a :", A_matrix)
print("\nVerified basis vectors are :")
print(f"\na1: {np.round(a1,6)}")
print(f"\na2: {np.round(a2,6)}")
print(f"\na3: {np.round(a3,6)}")