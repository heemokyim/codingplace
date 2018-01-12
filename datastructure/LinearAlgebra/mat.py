# Copyright 2013 Philip N. Klein
from vec import Vec

def efficient_rowdict2mat(rowdict):
    col_labels = value(rowdict).D
    M = Mat((set(keys(rowdict)), col_labels), {})
    for r in rowdict:
        for c in rowdict[r].f:
            M[r,c] = rowdict[r][c]
    return M

def identity(D, one):
    return Mat((D,D), {(d,d):one for d in D})

def keys(d):
    return d.keys() if isinstance(d, dict) else range(len(d))

def value(d):
    return next(iter(d.values())) if isinstance(d, dict) else d[0]

def mat2rowdict(A):
    return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}

def mat2coldict(A):
    return {col:Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}

def coldict2mat(coldict):
    row_labels = value(coldict).D
    return Mat((row_labels, set(keys(coldict))), {(r,c):coldict[c][r] for c in keys(coldict) for r in row_labels})

def rowdict2mat(rowdict):
    col_labels = value(rowdict).D
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})

def listlist2mat(L):
    m,n = len(L), len(L[0])
    return Mat((set(range(m)),set(range(n))), {(r,c):L[r][c] for r in range(m) for c in range(n)})

def submatrix(M, rows, cols):
    return Mat((M.D[0]&rows, M.D[1]&cols), {(r,c):val for (r,c),val in M.f.items() if r in rows and c in cols})

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

def getitem(M, k):
    """
        Returns the value of entry k in M, where k is a 2-tuple
        >>> M = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})
        >>> M[1,'a']
        4
        >>> M[3,'a']
        0
        """
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return M.f[k] if k in M.f else 0

def equal(A, B):
    """
    Returns true iff A is equal to B.

    Consider using brackets notation A[...] and B[...] in your procedure
    to access entries of the input matrices.  This avoids some sparsity bugs.

    >>> Mat(({'a','b'}, {'A','B'}), {('a','B'):0}) == Mat(({'a','b'}, {'A','B'}), {('b','B'):0})
    True
    >>> A = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1})
    >>> B = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1, ('b','B'):0})
    >>> C = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1, ('b','B'):5})
    >>> A == B
    True
    >>> B == A
    True
    >>> A == C
    False
    >>> C == A
    False
    >>> A == Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1})
    True
    """
    assert A.D == B.D

    a=0
    b=0

    for key in A.f.keys():
        if A[key] != B[key]:
            a+=1

    for key in B.f.keys():
        if B[key] != A[key]:
            b+=1

    return True if a+b==0 else False

def setitem(M, k, val):
    """
    Set entry k of Mat M to val, where k is a 2-tuple.
    >>> M = Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):7})
    >>> M['b', 5] = 9
    >>> M['c', 5] = 13
    >>> M == Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):9, ('c',5):13})
    True

    Make sure your operations work with bizarre and unordered keys.

    >>> N = Mat(({((),), 7}, {True, False}), {})
    >>> N[(7, False)] = 1
    >>> N[(((),), True)] = 2
    >>> N == Mat(({((),), 7}, {True, False}), {(7,False):1, (((),), True):2})
    True
    """
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k]=val

def add(A, B):
    """
        Return the sum of Mats A and B.

        Consider using brackets notation A[...] or B[...] in your procedure
        to access entries of the input matrices.  This avoids some sparsity bugs.

        >>> A1 = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3})
        >>> A2 = Mat(({3, 6}, {'x','y'}), {(3,'y'):4})
        >>> B = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (3,'y'):4, (6,'y'):3})
        >>> A1 + A2 == B
        True
        >>> A2 + A1 == B
        True
        >>> A1 == Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3})
        True
        >>> zero = Mat(({3,6}, {'x','y'}), {})
        >>> B + zero == B
        True
        >>> C1 = Mat(({1,3}, {2,4}), {(1,2):2, (3,4):3})
        >>> C2 = Mat(({1,3}, {2,4}), {(1,4):1, (1,2):4})
        >>> D = Mat(({1,3}, {2,4}), {(1,2):6, (1,4):1, (3,4):3})
        >>> C1 + C2 == D
        True
        """
    assert A.D == B.D
    return Mat((A.D),{key:A[key]+B[key] for key in set(A.f.keys()).union(set(B.f.keys())) })

def scalar_mul(M, x):
    """
    Returns the result of scaling M by x.

    >>> M = Mat(({1,3,5}, {2,4}), {(1,2):4, (5,4):2, (3,4):3})
    >>> 0*M == Mat(({1, 3, 5}, {2, 4}), {})
    True
    >>> 1*M == M
    True
    >>> 0.25*M == Mat(({1,3,5}, {2,4}), {(1,2):1.0, (5,4):0.5, (3,4):0.75})
    True
    """
    return Mat(M.D,{key:x*value for (key,value) in M.f.items()})

def transpose(M):
    """
    Returns the matrix that is the transpose of M.

    >>> M = Mat(({0,1}, {0,1}), {(0,1):3, (1,0):2, (1,1):4})
    >>> M.transpose() == Mat(({0,1}, {0,1}), {(0,1):2, (1,0):3, (1,1):4})
    True
    >>> M = Mat(({'x','y','z'}, {2,4}), {('x',4):3, ('x',2):2, ('y',4):4, ('z',4):5})
    >>> Mt = Mat(({2,4}, {'x','y','z'}), {(4,'x'):3, (2,'x'):2, (4,'y'):4, (4,'z'):5})
    >>> M.transpose() == Mt
    True
    """
    return Mat((M.D[1], M.D[0]), {(col, row): M.f[row, col] for row, col in M.f.keys()})

def vector_matrix_mul(v, M):
    """
    returns the product of vector v and matrix M

    Consider using brackets notation v[...] in your procedure
    to access entries of the input vector.  This avoids some sparsity bugs.

    >>> v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
    >>> M1 = Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7})
    >>> v1*M1 == Vec({'a', 'b', 'c'},{'a': -8, 'b': 2, 'c': 0})
    True
    >>> v1 == Vec({1, 2, 3}, {1: 1, 2: 8})
    True
    >>> M1 == Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7})
    True
    >>> v2 = Vec({'a','b'}, {})
    >>> M2 = Mat(({'a','b'}, {0, 2, 4, 6, 7}), {})
    >>> v2*M2 == Vec({0, 2, 4, 6, 7},{})
    True
    >>> v3 = Vec({'a','b'},{'a':1,'b':1})
    >>> M3 = Mat(({'a', 'b'}, {0, 1}), {('a', 1): 1, ('b', 1): 1, ('a', 0): 1, ('b', 0): 1})
    >>> v3*M3 == Vec({0, 1},{0: 2, 1: 2})
    True
    """
    assert M.D[0] == v.D
    # 5.17.15
    # return Vec(M.D[1], {key: v * col_v for (key, col_v) in mat2coldict(M).items()})

    # 5.17.13
    # return Vec(M.D[1],
    #            {col: sum(M.f[row, col] * v.f[row] for row in M.D[0]
    #                      if (row, col) in M.f.keys() and row in v.f.keys())
    #             for col in M.D[1]})
    # doesn't consider sparse entry

    vec = Vec(M.D[1], {})

    not_sparse = set(M.f.keys())

    for each in not_sparse:
        vec[each[1]] = vec[each[1]] + v[each[0]] * M[each]

    return vec


def matrix_vector_mul(M, v):
    """
        Returns the product of matrix M and vector v.

        Consider using brackets notation v[...] in your procedure
        to access entries of the input vector.  This avoids some sparsity bugs.

        >>> N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
        >>> u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
        >>> N1*u1 == Vec({1, 3, 5, 7},{1: 3, 3: 9, 5: -2, 7: 3})
        True
        >>> N1 == Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
        True
        >>> u1 == Vec({'a', 'b'}, {'a': 1, 'b': 2})
        True
        >>> N2 = Mat(({('a', 'b'), ('c', 'd')}, {1, 2, 3, 5, 8}), {})
        >>> u2 = Vec({1, 2, 3, 5, 8}, {})
        >>> N2*u2 == Vec({('a', 'b'), ('c', 'd')},{})
        True
        >>> M3 = Mat(({0,1},{'a','b'}),{(0,'a'):1, (0,'b'):1, (1,'a'):1, (1,'b'):1})
        >>> v3 = Vec({'a','b'},{'a':1,'b':1})
        >>> M3*v3 == Vec({0, 1},{0: 2, 1: 2})
        True
        """
    assert M.D[1] == v.D
    # 5.17.14
    # return Vec(M.D[0],{key: v*row_v for (key,row_v) in mat2rowdict(M).items()})

    # 5.17.12
    # return Vec(M.D[0],
    #            {row: sum(M.f[row,col]*v.f[col] for col in M.D[1]
    #                      if (row,col) in M.f.keys() and col in v.f.keys())
    #             for row in M.D[0]})
    # doesn't consider sparse entry

    vec=Vec(M.D[0],{})

    not_sparse=set(M.f.keys())

    for each in not_sparse:
        vec[each[0]]=vec[each[0]]+M[each]*v[each[1]]

    return vec


def matrix_matrix_mul(A, B):
    """
        Returns the result of the matrix-matrix multiplication, A*B.

        Consider using brackets notation A[...] and B[...] in your procedure
        to access entries of the input matrices.  This avoids some sparsity bugs.

        >>> A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
        >>> B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
        >>> A*B == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})
        True
        >>> C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
        >>> D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
        >>> C*D == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})
        True
        >>> M = Mat(({0, 1}, {'a', 'c', 'b'}), {})
        >>> N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})
        >>> M*N == Mat(({0,1}, {(1,1), (2,2)}), {})
        True
        >>> E = Mat(({'a','b'},{'A','B'}), {('a','A'):1,('a','B'):2,('b','A'):3,('b','B'):4})
        >>> F = Mat(({'A','B'},{'c','d'}),{('A','d'):5})
        >>> E*F == Mat(({'a', 'b'}, {'d', 'c'}), {('b', 'd'): 15, ('a', 'd'): 5})
        True
        >>> F.transpose()*E.transpose() == Mat(({'d', 'c'}, {'a', 'b'}), {('d', 'b'): 15, ('d', 'a'): 5})
        True
        """
    assert A.D[1] == B.D[0]

    # 5.17.16
    # return coldict2mat({key : A*vector for (key,vector) in mat2coldict(B).items()})
    # 5.17.17
    # return rowdict2mat( {key: vector*B  for(key,vector) in mat2rowdict(A).items()})

    not_sparse_B=set(B.f.keys())
    B_cols=set({each[1] for each in not_sparse_B})
    coldict=dict()

    for col in B_cols:
        vec=Vec(B.D[0],{dom[0]: B[dom] for dom in not_sparse_B if col == dom[1]})
        coldict[col]=vec

    return coldict2mat({k:A*v for k,v in coldict.items()})

################################################################################

class Mat:
    def __init__(self, labels, function):
        assert isinstance(labels, tuple)
        assert isinstance(labels[0], set) and isinstance(labels[1], set)
        assert isinstance(function, dict)
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose
    __add__ = add
    __eq__ = equal


    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will
            # only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    def __radd__(self, other):
        "Hack to allow sum(...) to work with matrices"
        if other == 0:
            return self

    def __sub__(a,b):
        return a+(-b)



    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None: rows = sorted(M.D[0], key=repr)
        if cols == None: cols = sorted(M.D[1], key=repr)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(str(c),colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(str(r), pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"

    def __iter__(self):
        raise TypeError('%r object is not iterable' % self.__class__.__name__)
