# perform queries on 2D matrix .
# query type 1: "R i x" (i--> Position) (R--> Row) (x--> Value) update value at position in row.
# query type 2: "C i x" (i--> Position) (C--> Coloum) (x--> Value) update value at position in coloum.

## so the approch is create two array R[] and C[] of size N  which holds all the value 
## then find max from both and tham to get maximum value 
## 

def huge_matrix(N, queries):
    R = [0] * N
    C = [0] * N
    for  k, i, x in queries:
        if k == "R":
            R[i] += x
        elif k == "C":
            C[i] += x
    return max(R) + max(C)
    
queries = [["R", 1, 7], ["C", 2, 6], ["R", 0, 3]]
N = 3
print(huge_matrix(N, queries))