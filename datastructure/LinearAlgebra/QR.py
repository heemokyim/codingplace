# Copyright 2013 Philip N. Klein
from orthonormalization import *
from dictutil import *
from matutil import *
from triangular import *

def QR_factor(A):
    # A = matrix

    coldicts=mat2coldict(A)
    Acols=dict2list(coldicts,coldicts.keys())

    # Qlist, Rlist are lists that vectors
    Qlist, Rlist = aug_orthonormalize(Acols)

    col_labels = sorted(A.D[1], key=repr)
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist,col_labels))

    return Q,R

def QR_solve(A,b):
    # A * x = b
    # R * x = transpose(Q)*b

    Q,R=factor(A)

    Qtb=transpose(Q)*b

    R_rowlist=[val for val in mat2rowdict(R).values()]
    label_list=sorted(R.D[1],key=repr)

    x=triangular_solve(R_rowlist, label_list , Qtb)

    return x