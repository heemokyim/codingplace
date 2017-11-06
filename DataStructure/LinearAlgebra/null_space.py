import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one

from math import *
from vecutil import *
from matutil import *
from inverse_matrix import *
from echelon import *
from orthonormalization import *

def find_null_space(A):
    # find basis of null-space using Grem-Schmit orthogonalization
    # Refer to page 416
    # note that row * col, that's why mat2rowdict

    # 2017.8.13
    # modified to work for complex-field

    # n = length of row-vectors
    n=A.D[1]

    # W that U + V = W
    # standard basis vectors
    W=[list2vec([1 if each==i else 0 for each in range(len(n))]) for i in range(len(n))]

    U=[row_vec for row_vec in mat2rowdict(A).values()]

    # A_rows = U
    ortho_input = U + W
    V_idx=len(U)

    ortho_result=orthogonalize(ortho_input)

    V=ortho_result[V_idx:]

    # remove 0-vectors of V
    remove_idx=[]
    for idx,vec in enumerate(V):
        v_norm = sum(val.real**2 + val.imag**2 for val in vec.f.values())
        if v_norm <= 1E-20:
            remove_idx.append(idx)

    remove_entry=[V[i] for i in remove_idx]

    for each in remove_entry:
        V.remove(each)

    if len(V) == 0:
        print('No null-space exists')
        return None

    # remove 0-entry of V
    for vec in V:
        for d,v in vec.f.items():
            vhat=v.conjugate()
            if (vhat*v).real < 1E-20:
                vec[d]=0

    return V


def find_null_space_echelon(A):
    # find null-space using Gauss-elimination
    # Refer to page 352
    # basis v that v*A=0, not A*v

    M=transformation(A)

    # U = echelon
    U=M*A

    # row-vectors of U
    Urows=[each for each in mat2rowdict(U).values()]

    basis_idx=[]
    for idx,vec in enumerate(Urows):
        v_norm = sum(val.real ** 2 + val.imag ** 2 for val in vec.f.values())
        if v_norm <=1E-20:
            basis_idx.append(idx)

    if len(basis_idx) == 0:
        print('No null-space exists')
        return None

    # row-vectors of M
    Mrows=[each for each in mat2rowdict(M).values()]
    null_basis=[Mrows[idx] for idx in basis_idx]

    # A*v=0, v*A=0 example
    # print(list2vec([1,-1,1])*A)
    # print(transpose(A)*list2vec([1,-1,1]))

    return null_basis


# script example
# U=listlist2mat([[1,0,0],[1,1,0],[0,1,0]])
# V=find_null_space(U)

def find_biggest_eigval(A):

    assert A.D[0] == A.D[1]

    xt=list2vec([1 for d in range(len(A.D[0]))])

    for each in range(1000):
        xt=A*xt

    validate_idx=0

    for idx,val in xt.f.items():
        if val*val > 1E-20:
            break

    return (A*xt)[idx]/xt[idx]


def find_smallest_eigval(A):

    assert A.D[0] == A.D[1]

    inv=find_matrix_invertible(A)

    return find_biggest_eigval(inv)