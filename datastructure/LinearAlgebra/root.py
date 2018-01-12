import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one
from vec import Vec
from mat import Mat
from echelon import *

from vecutil import *
from matutil import *

# only works when field is GF(2), or small R number


# 8.9.6
def echelon_solve(rowlist, label_list, b):
    # Return x that A * x = b
    # A is echelon from list of row-vectors(rowlist)
    # rowlist = list that vectors
    # label_list = list that column labels
    # b = vector

    '''
    >>> rowlist=[list2vec(v) for v in [[2,0,1,3],[0,0,5,3],[0,0,0,1]]]
    >>> b=list2vec([1,-1,3])
    >>> x=echelon_solve(rowlist,rowlist[0].D,b)
    >>> print(x)
    <BLANKLINE>
      0 1  2 3
    ----------
     -3 0 -2 3

     >>> rowlist=[list2vec(v) for v in [[1,2,-8,-4,0],[0,0,2,12,0],[0,0,0,0,0],[0,0,0,0,0]]]
     >>> b=list2vec([5,4,0,0])
     >>> x=echelon_solve(rowlist,rowlist[0].D,b)
     >>> print(x)
     <BLANKLINE>
       0 1 2 3 4
     -----------
      21 0 2 0 0

      >>> rowlist=[list2vec(v) for v in [[1,3,-2,1,0],[0,0,2,-3,0],[0,0,0,0,0]]]
      >>> b=list2vec([5,3,2])
      >>> x=echelon_solve(rowlist,rowlist[0].D,b)
      No root exists
    '''
    x=zero_vec(label_list)


    for idx,row in enumerate(reversed(rowlist)):
        b_idx=len(rowlist)-(1+idx)

        for col in label_list:
            if row[col] != 0:
                x[col] = (b[b_idx] - row * x) / row[col]
                # below 'break' is important
                # This means eliminating irrelevant column.
                break

        # if b[b_idx] exists but responsive row is 0-Vector,
        # There is no roots
        # For example, 0 * 2 = 3 doesn't happen.
        # Refer to 8.9.5.(a) at page 369
                                    # When responsive Vec is 0-Vector
        if b[b_idx] != 0 and row == Vec(rowlist[0].D,{ }):
            print('No root exists')
            return

    return x

# ----------------------------------------------------------------------------------------
# After understanding 8.9.6, we can code solver.solve
# 8.9.7
def solve(A,b, field=1):
    # Return x that A * x = b
    # Let say M * A is echelon,
    # If x is root for A * x = b,
    # Also x is root for M*A *x = M*b

    M = transformation(A,field=field)

    rowlist_U=[each for each in mat2rowdict(M*A).values()]

    x = echelon_solve(rowlist_U,rowlist_U[0].D, M*b)

    return x

# test-case for 8.9.7
# A=listlist2mat([[2,0,-1],[4,-3,1],[0,2,3]])
# b=list2vec([1,2,5])
# x = solve(A,b)
#
# print(x)

# 8.9.8
def null_space_root(A,field=1):
    # Return u that u * A = 0
    # Refer to page 351

    M=transformation(A,field=field)

    U=M*A

    rowlist_U=[each for each in mat2rowdict(U).values()]
    rowlist_M=[each for each in mat2rowdict(M).values()]

    # what we want to know
    null_generator=[]

    for idx,each in enumerate(rowlist_U):
        if each == Vec(M.D[1],{ }):
            null_generator.append(rowlist_M[idx])

    return null_generator

# test-case for 8.9.8
# A=listlist2mat([[0,0,0,one,0],[0,0,0,one,one],[one,0,0,one,0],[one,0,0,0,one],[one,0,0,0,0]])
# x=null_space_root(A,field=0)
# for each in x:
#     print(each)

# A=listlist2mat([[0,0,0,one,0],[0,0,0,one,one],[one,0,0,one,0],[one,one,one,0,one],[one,0,0,one,0]])
# x=null_space_root(A,field=0)
# for each in x:
#     print(each)