from matutil import *
from vecutil import *
from solver import *
from simplex import *
import itertools

def enum(A,b,c):
    # Steps
    # 0. Find sub-system's vertex
    # 1. Check whether A*x >= b
    # 2. Put it in verdices-set
    # 3. After finishing verdices-set,
    #       return max-objective-value(c*x)

    verdices=[]
    feasible_verdices=[]
    objective_values=[]

    n=A.D[1]
    A_rows=A.D[0]

    for i in itertools.combinations(A_rows,2):
        verdices.append({i[0],i[1]})

    for i in verdices:
        R_square=i
        A_square = Mat((R_square, A.D[1]), {(r, c): A[r, c] for r, c in A.f if r in R_square})
        b_square = Vec(R_square, {k: b[k] for k in R_square})
        x=solve(A_square,b_square)

        A_x=A*x

        flag=True


        for d,val in A_x.f.items():
            # min c*x |A*x >= b -> if val < b[d]
            # max c*x |A*x <= b -> if val > b[d]

            residual=abs(val-b[d])
            if residual <= abs(1E-10):
                val=b[d]

            if val < b[d]:
                print('this is not feasible'+str(i))
                flag=False
                break


        # if flag:
        #     y_square=solve(transpose(A_square),c)
        #     y=Vec(A.D[0],y_square.f)
        #     if min(y.f.values())>=0:
        #         print(i)
        #         return x

    return 'no proper root'




A=listlist2mat([[2,10],[2,1],[8,1],[0,1],[1,0]])
b=list2vec([5,1,2,0,0])
c=list2vec([1,1.7])
print(enum(A,b,c))