from vec import Vec
from mat import Mat
import itertools

def efficient_rowdict2mat(rowdict):
    col_labels = value(rowdict).D
    M = Mat((set(keys(rowdict)), col_labels), {})
    for r in rowdict:
        for c in rowdict[r].f:
            M[r,c] = rowdict[r][c]
    return M

def identity(D, one):
    return Mat((D,D), {(d,d):one for d in D})

def transpose(M):
    return Mat((M.D[1],M.D[0]),{(col,row):M.f[row,col] for row,col in M.f.keys()})

def keys(d):
    return d.keys() if isinstance(d, dict) else range(len(d))

def value(d):
    return next(iter(d.values())) if isinstance(d, dict) else d[0]

def mat2vec(A):
    return Vec({d for d in itertools.product(A.D[0],A.D[1])},{d:A[d] for d in itertools.product(A.D[0],A.D[1])})

def vec2mat(v):
    return 0

def mat2rowdict(A):
    return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}

def mat2coldict(A):
    return {col:Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}

def coldict2mat(coldict):
    # any input that has 'value'
    # e.g. list, dict etc
    row_labels = value(coldict).D
    return Mat((row_labels, set(keys(coldict))), {(r,c):coldict[c][r] for c in keys(coldict) for r in row_labels})

def rowdict2mat(rowdict):
    # any input that has 'value'
    # e.g. list, dict etc
    col_labels = value(rowdict).D
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})

def listlist2mat(L):
    m,n = len(L), len(L[0])
    return Mat((set(range(m)),set(range(n))), {(r,c):L[r][c] for r in range(m) for c in range(n)})

def submatrix(M, rows, cols):
    return Mat((M.D[0]&rows, M.D[1]&cols), {(r,c):val for (r,c),val in M.f.items() if r in rows and c in cols})